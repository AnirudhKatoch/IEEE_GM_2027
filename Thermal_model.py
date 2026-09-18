import numpy as np
from scipy.integrate import solve_ivp
import numpy as np
from scipy.signal import lfilter
from functools import lru_cache


def simulate_igbt_diode_cauer_transient(r_I, cap_I,r_D, cap_D,r_paste, cap_paste, r_sink, cap_sink,P_I, P_D,T_env, dt,method, rtol, atol,debug, T0_init):
    """
    Simulate coupled IGBT + Diode junction temperatures using a Cauer-type RC network.

    Parameters
    ----------
    r_I : 1D array
        IGBT ladder thermal resistances [K/W], junction -> case.
    cap_I : 1D array
        IGBT ladder thermal capacitances [J/K], same length as r_I.
    r_D : 1D array
        Diode ladder thermal resistances [K/W], junction -> case.
    cap_D : 1D array
        Diode ladder thermal capacitances [J/K].
    r_paste : 1D array of length 1
        Case-to-sink resistance [K/W].
    cap_paste : 1D array of length 1
        Case node capacitance [J/K].
    r_sink : 1D array of length 1
        Sink-to-ambient resistance [K/W].
    cap_sink : 1D array of length 1
        Sink node capacitance [J/K].
    P_I : 1D array
        IGBT power loss profile [W].
    P_D : 1D array
        Diode power loss profile [W].
    T_env : 1D array
        Ambient temperature profile [K].
    dt : float
        Time resolution of the profiles [s].
    method : str
        SciPy solve_ivp method ("BDF", "Radau", "RK45", ...).
    rtol, atol : float
        Relative and absolute tolerances for solve_ivp.

    Returns
    -------
    t : 1D array
        Time vector [s].
    Tj_igbt : 1D array
        IGBT junction temperature [°C] vs time.
    Tj_diode : 1D array
        Diode junction temperature [°C] vs time.
    T_case : 1D array
        Case (package) temperature [°C] vs time.
    T_sink : 1D array
        Sink temperature [°C] vs time.
    """

    # --- basic checks ---
    P_I  = np.asarray(P_I, dtype=float)
    P_D  = np.asarray(P_D, dtype=float)

    n_steps = len(P_I)
    mission_duration_s = n_steps * dt

    n_i = len(r_I)
    n_d = len(r_D)
    n_p = len(r_paste)   # should be 1
    n_s = len(r_sink)  # should be 1


    # --- profile sampler (piecewise constant) ---
    def profile_step(t, values):
        idx = int(np.floor(t / dt))
        if idx < 0:
            idx = 0
        if idx >= len(values):
            idx = len(values) - 1
        return values[idx]

    def P_igbt(t):
        return profile_step(t, P_I)

    def P_diode(t):
        return profile_step(t, P_D)

    def T_amb(t):
        return profile_step(t, T_env)

    # --- indexing in state vector T ---
    idx_i_start = 0
    idx_d_start = n_i
    idx_p_start = n_i + n_d
    idx_s_start = n_i + n_d + n_p
    total_nodes = n_i + n_d + n_p + n_s

    # optional debug counter
    step_counter = {"n": 0}

    # --- RHS of ODE ---
    def rhs(t, T):

        if debug== True:
            step_counter["n"] += 1
            if step_counter["n"] % 1000 == 0:
               print(f"Internal solver step {step_counter['n']}, t = {t:.6f}")

        dTdt = np.zeros_like(T)

        P_i = P_igbt(t)
        P_d = P_diode(t)
        T_env = T_amb(t)

        # views
        T_i = T[idx_i_start:idx_i_start + n_i]
        T_d = T[idx_d_start:idx_d_start + n_d]
        T_p = T[idx_p_start:idx_p_start + n_p]  # case node(s)
        T_s = T[idx_s_start:idx_s_start + n_s]  # sink node(s)

        # --- IGBT ladder ---
        # junction node
        if n_i == 1:
            # single RC from junction to case
            Tj = T_i[0]
            T_case = T_p[0]
            q_to_case = (Tj - T_case) / r_I[0]
            dTdt[idx_i_start + 0] = (P_i - q_to_case) / cap_I[0]

        else:

            q_i_0_to_1 = (T_i[0] - T_i[1]) / r_I[0]
            dTdt[idx_i_start + 0] = (P_i - q_i_0_to_1) / cap_I[0]

            # internal nodes
            for j in range(1, n_i - 1):
                q_from_prev = (T_i[j - 1] - T_i[j]) / r_I[j - 1]
                q_to_next   = (T_i[j] - (T_p[0] if j == n_i - 1 else T_i[j + 1])) / r_I[j]
                dTdt[idx_i_start + j] = (q_from_prev - q_to_next) / cap_I[j]

            # last IGBT node -> case
            if n_i > 1:
                j = n_i - 1
                q_from_prev = (T_i[j - 1] - T_i[j]) / r_I[j - 1]
                q_to_case   = (T_i[j] - T_p[0]) / r_I[j]
                dTdt[idx_i_start + j] = (q_from_prev - q_to_case) / cap_I[j]

        # --- Diode ladder ---
        # junction node
        if n_d == 1:
            # single RC from junction directly to case
            Tj_d = T_d[0]  # diode junction temperature
            T_case = T_p[0]
            q_to_case = (Tj_d - T_case) / r_D[0]
            dTdt[idx_d_start + 0] = (P_d - q_to_case) / cap_D[0]

        else:

            q_d_0_to_1 = (T_d[0] - T_d[1]) / r_D[0]
            dTdt[idx_d_start + 0] = (P_d - q_d_0_to_1) / cap_D[0]

            # internal nodes
            for j in range(1, n_d - 1):
                q_from_prev = (T_d[j - 1] - T_d[j]) / r_D[j - 1]
                q_to_next   = (T_d[j] - (T_p[0] if j == n_d - 1 else T_d[j + 1])) / r_D[j]
                dTdt[idx_d_start + j] = (q_from_prev - q_to_next) / cap_D[j]

            # last Diode node -> case
            if n_d > 1:
                j = n_d - 1
                q_from_prev = (T_d[j - 1] - T_d[j]) / r_D[j - 1]
                q_to_case   = (T_d[j] - T_p[0]) / r_D[j]
                dTdt[idx_d_start + j] = (q_from_prev - q_to_case) / cap_D[j]

        # --- Case node (package) ---
        T_i_last = T_i[-1]
        T_d_last = T_d[-1]
        T_case   = T_p[0]
        T_sink   = T_s[0]

        q_i_to_case = (T_i_last - T_case) / r_I[-1]
        q_d_to_case = (T_d_last - T_case) / r_D[-1]

        # --- Paste / Case ladder ---

        if n_p == 1:
            # Single case/paste node directly connected to first sink node
            T_case = T_p[0]
            T_sink0 = T_s[0]

            q_case_to_next = (T_case - T_sink0) / r_paste[0]
            dTdt[idx_p_start + 0] = (q_i_to_case + q_d_to_case - q_case_to_next) / cap_paste[0]

        else:
            # j = 0: Case node -> Paste node 1
            T_case = T_p[0]
            q_case_to_next = (T_case - T_p[1]) / r_paste[0]
            dTdt[idx_p_start + 0] = (q_i_to_case + q_d_to_case - q_case_to_next) / cap_paste[0]

            # internal paste nodes 1 .. n_p-2
            for j in range(1, n_p - 1):
                T_j = T_p[j]
                T_jm = T_p[j - 1]  # previous
                T_jp = T_p[j + 1]  # next

                q_from_prev = (T_jm - T_j) / r_paste[j - 1]
                q_to_next = (T_j - T_jp) / r_paste[j]
                dTdt[idx_p_start + j] = (q_from_prev - q_to_next) / cap_paste[j]

            # last paste node j = n_p - 1 -> first sink node T_s[0]
            j = n_p - 1
            T_last_p = T_p[j]
            T_prev_p = T_p[j - 1]
            T_sink0 = T_s[0]

            q_from_prev = (T_prev_p - T_last_p) / r_paste[j - 1]
            q_to_sink0 = (T_last_p - T_sink0) / r_paste[j]
            dTdt[idx_p_start + j] = (q_from_prev - q_to_sink0) / cap_paste[j]

        # --- Sink ladder ---

        # Heat entering the sink ladder from paste side:
        if n_p == 1:
            # when n_p == 1, paste/case connects directly to sink[0]
            q_from_paste = q_case_to_next
        else:
            # when n_p > 1, last paste node connects to sink[0]
            q_from_paste = q_to_sink0

        if n_s == 1:
            # single sink node connected to ambient
            T_sink = T_s[0]
            q_sink_to_amb = (T_sink - T_env) / r_sink[0]
            dTdt[idx_s_start + 0] = (q_from_paste - q_sink_to_amb) / cap_sink[0]

        else:
            # first sink node: gets heat from paste, sends to sink[1]
            T_s0 = T_s[0]
            T_s1 = T_s[1]
            q_0_to_1 = (T_s0 - T_s1) / r_sink[0]
            dTdt[idx_s_start + 0] = (q_from_paste - q_0_to_1) / cap_sink[0]

            # internal sink nodes: 1 .. n_s-2
            for j in range(1, n_s - 1):
                T_j = T_s[j]
                T_jm = T_s[j - 1]
                T_jp = T_s[j + 1]

                q_from_prev = (T_jm - T_j) / r_sink[j - 1]
                q_to_next = (T_j - T_jp) / r_sink[j]
                dTdt[idx_s_start + j] = (q_from_prev - q_to_next) / cap_sink[j]

            # last sink node j = n_s - 1 -> ambient
            j = n_s - 1
            T_last_s = T_s[j]
            T_prev_s = T_s[j - 1]

            q_from_prev = (T_prev_s - T_last_s) / r_sink[j - 1]
            q_to_amb = (T_last_s - T_env) / r_sink[j]
            dTdt[idx_s_start + j] = (q_from_prev - q_to_amb) / cap_sink[j]

        return dTdt

    # --- initial condition ---
    if T0_init is None:
        # start from ambient for all nodes
        T0_amb = T_env[0]
        T0 = np.full(total_nodes, T0_amb)

    else:
        # reuse last state from previous chunk
        T0 = np.asarray(T0_init, dtype=float)
        if T0.size != total_nodes:
            raise ValueError(f"T0_init has wrong size {T0.size}, expected {total_nodes}")


    t_start = 0.0
    t_end   = mission_duration_s
    t_eval = np.arange(n_steps) * dt


    sol = solve_ivp(rhs, (t_start, t_end), T0, t_eval=t_eval, method=method, rtol=rtol, atol=atol )

    time_steps = sol.t
    T = sol.y

    # extract node temperatures
    T_i = T[idx_i_start:idx_i_start + n_i, :]
    T_d = T[idx_d_start:idx_d_start + n_d, :]
    T_p = T[idx_p_start:idx_p_start + n_p, :]
    T_s = T[idx_s_start:idx_s_start + n_s, :]


    return time_steps, T_i, T_d, T_p, T_s

def simulate_igbt_diode_cauer_fast(r_I, cap_I, r_D, cap_D, r_paste, cap_paste, r_sink, cap_sink,P_I, P_D, T_env, dt,method=None, rtol=None, atol=None, debug=False, T0_init=None):
    """
    Exact solution of the same Cauer network as simulate_igbt_diode_cauer_transient,
    for piecewise-constant losses (zero-order hold), without an ODE solver.
    The network is split into independent first-order modes (eigen-decomposition),
    each solved with lfilter. Same inputs and outputs as the transient function.
    """
    r_I, cap_I = np.atleast_1d(r_I).astype(float), np.atleast_1d(cap_I).astype(float)
    r_D, cap_D = np.atleast_1d(r_D).astype(float), np.atleast_1d(cap_D).astype(float)
    r_p, c_p = np.atleast_1d(r_paste).astype(float), np.atleast_1d(cap_paste).astype(float)
    r_s, c_s = np.atleast_1d(r_sink).astype(float), np.atleast_1d(cap_sink).astype(float)
    P_I = np.asarray(P_I, float); P_D = np.asarray(P_D, float); T_env = np.asarray(T_env, float)

    n_i, n_d, n_p, n_s = len(r_I), len(r_D), len(r_p), len(r_s)
    i0, d0, p0, s0 = 0, n_i, n_i + n_d, n_i + n_d + n_p
    N = n_i + n_d + n_p + n_s
    n_steps = len(P_I)

    # ---- conductance matrix G (W/K) ----
    G = np.zeros((N, N))
    def link(a, b, R):
        g = 1.0 / R
        G[a, a] += g; G[b, b] += g; G[a, b] -= g; G[b, a] -= g

    for j in range(n_i):
        link(i0 + j, i0 + j + 1 if j < n_i - 1 else p0, r_I[j])
    for j in range(n_d):
        link(d0 + j, d0 + j + 1 if j < n_d - 1 else p0, r_D[j])
    for j in range(n_p):
        link(p0 + j, p0 + j + 1 if j < n_p - 1 else s0, r_p[j])
    for j in range(n_s - 1):
        link(s0 + j, s0 + j + 1, r_s[j])
    G[N - 1, N - 1] += 1.0 / r_s[-1]                     # last sink node -> ambient

    C = np.concatenate([cap_I, cap_D, c_p, c_s])

    # ---- symmetric eigen-decomposition: modes of C·dT/dt = -G·T + inputs ----
    S = 1.0 / np.sqrt(C)
    lam, V = np.linalg.eigh(S[:, None] * G * S[None, :])  # lam > 0 [1/s]
    to_T = S[:, None] * V                                 # mode -> node temperature
    to_z = V.T * np.sqrt(C)[None, :]                      # node temperature -> mode

    # input vectors (heat into nodes)
    bI = np.zeros(N); bI[i0] = 1.0
    bD = np.zeros(N); bD[d0] = 1.0
    bE = np.zeros(N); bE[N - 1] = 1.0 / r_s[-1]
    wI, wD, wE = (V.T @ (S * bI)), (V.T @ (S * bD)), (V.T @ (S * bE))

    # initial state
    T0 = np.full(N, T_env[0]) if T0_init is None else np.asarray(T0_init, float)
    if T0.size != N:
        raise ValueError(f"T0_init has wrong size {T0.size}, expected {N}")
    z0 = to_z @ T0

    # ---- solve each mode exactly and build node temperatures ----
    T = np.zeros((N, n_steps))
    for m in range(N):
        a = np.exp(-lam[m] * dt)
        g = (1.0 - a) / lam[m]
        w = wI[m] * P_I + wD[m] * P_D + wE[m] * T_env
        z = lfilter([0.0, g], [1.0, -a], w, zi=[z0[m]])[0]
        T += np.outer(to_T[:, m], z)

    t = np.arange(n_steps) * dt
    return t, T[i0:d0], T[d0:p0], T[p0:s0], T[s0:]

@lru_cache(maxsize=32)
def _thermal_modes(r_I, cap_I, r_D, cap_D, r_p, c_p, r_s, c_s):
    r_I, cap_I, r_D, cap_D = map(np.array, (r_I, cap_I, r_D, cap_D))
    r_p, c_p, r_s, c_s = map(np.array, (r_p, c_p, r_s, c_s))
    n_i, n_d, n_p, n_s = len(r_I), len(r_D), len(r_p), len(r_s)
    i0, d0, p0, s0 = 0, n_i, n_i + n_d, n_i + n_d + n_p
    N = n_i + n_d + n_p + n_s

    G = np.zeros((N, N))
    def link(a, b, R):
        g = 1.0 / R; G[a, a] += g; G[b, b] += g; G[a, b] -= g; G[b, a] -= g

    for j in range(n_i): link(i0 + j, i0 + j + 1 if j < n_i - 1 else p0, r_I[j])
    for j in range(n_d): link(d0 + j, d0 + j + 1 if j < n_d - 1 else p0, r_D[j])
    for j in range(n_p): link(p0 + j, p0 + j + 1 if j < n_p - 1 else s0, r_p[j])
    for j in range(n_s - 1): link(s0 + j, s0 + j + 1, r_s[j])
    G[N - 1, N - 1] += 1.0 / r_s[-1]                  # last sink node -> ambient

    C = np.concatenate([cap_I, cap_D, c_p, c_s])
    S = 1.0 / np.sqrt(C)
    lam, V = np.linalg.eigh(S[:, None] * G * S[None, :])
    to_T = S[:, None] * V                             # modes -> node temperatures
    to_z = V.T * np.sqrt(C)[None, :]                  # node temperatures -> modes
    W = np.stack([V.T[:, i0] * S[i0],                 # IGBT loss input
                  V.T[:, d0] * S[d0],                 # diode loss input
                  V.T[:, N - 1] * S[N - 1] / r_s[-1]])  # ambient input
    rows = np.array([i0, d0, p0, s0])                 # IGBT junction, diode junction, case, sink
    return lam, to_T, to_z, W, rows, N

def simulate_igbt_diode_cauer_fastest(r_I, cap_I, r_D, cap_D, r_paste, cap_paste, r_sink, cap_sink,P_I, P_D, T_env, dt, T0_init=None):
    """
    Exact Cauer network solution (piecewise-constant losses), no ODE solver.
    Returns: time, Tj_igbt, Tj_diode, T_case, T_sink, T_last (full state for the next chunk)
    """
    key = tuple(tuple(np.atleast_1d(x).astype(float))
                for x in (r_I, cap_I, r_D, cap_D, r_paste, cap_paste, r_sink, cap_sink))
    lam, to_T, to_z, W, rows, N = _thermal_modes(*key)

    P_I = np.asarray(P_I, float); P_D = np.asarray(P_D, float); T_env = np.asarray(T_env, float)
    n = len(P_I)

    T0 = np.full(N, T_env[0]) if T0_init is None else np.asarray(T0_init, float)
    if T0.size != N:
        raise ValueError(f"T0_init has wrong size {T0.size}, expected {N}")
    z0 = to_z @ T0

    A = to_T[rows]
    out = np.zeros((4, n))
    z_last = np.empty(N)

    for m in range(N):
        a = np.exp(-lam[m] * dt)
        g = (1.0 - a) / lam[m]
        w = W[0, m] * P_I + W[1, m] * P_D
        w += W[2, m] * T_env

        if a < 1e-12:                                 # mode much faster than dt
            z = np.empty(n); z[0] = z0[m]; z[1:] = g * w[:-1]
        else:
            z = lfilter([0.0, g], [1.0, -a], w, zi=[z0[m]])[0]

        z_last[m] = z[-1]
        for k in range(4):
            if A[k, m] != 0.0:
                out[k] += A[k, m] * z

    T_last = to_T @ z_last
    return np.arange(n) * dt, out[0], out[1], out[2], out[3], T_last