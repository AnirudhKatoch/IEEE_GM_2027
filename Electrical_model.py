import numpy as np
from Calculation_functions import Calculation_functions_class
from functools import lru_cache

@lru_cache(maxsize=250000)
def _compute_IGBT_and_Diode_power_losses_cached(Is, phi, V_dc, pf, dt, M, omega, t_on, t_off, f_sw, I_ref, V_ref, Err_D, R_IGBT, V_0_IGBT, R_D, V_0_D, input_step, t0):

    t = t0 + np.arange(int(round(input_step / dt)), dtype=np.float64) * dt  # continues the grid phase

    m = Calculation_functions_class.Instantaneous_modulation(M=M, omega=omega, t=t, phi=phi)
    is_I, is_D = Calculation_functions_class.IGBT_and_diode_current(Is=Is, t=t, m=m, omega=omega)
    P_sw_I, P_sw_D = Calculation_functions_class.Switching_losses(V_dc=V_dc, is_I=is_I, t_on=t_on, t_off=t_off,f_sw=f_sw, is_D=is_D, I_ref=I_ref, V_ref=V_ref,Err_D=Err_D)
    P_con_I, P_con_D = Calculation_functions_class.Conduction_losses(is_I=is_I, R_IGBT=R_IGBT, V_0_IGBT=V_0_IGBT, M=M,pf=pf, is_D=is_D, R_D=R_D, V_0_D=V_0_D)
    P_I = np.ascontiguousarray(np.maximum(P_sw_I + P_con_I, 0.0), dtype=np.float64)
    P_D = np.ascontiguousarray(np.maximum(P_sw_D + P_con_D, 0.0), dtype=np.float64)

    # optional: freeze cached arrays so they can't be modified accidentally
    for arr in (P_I, P_D, is_I, is_D, P_sw_I, P_sw_D, P_con_I, P_con_D):
        arr.setflags(write=False)

    return P_I, P_D, is_I, is_D, P_sw_I, P_sw_D, P_con_I, P_con_D




def compute_IGBT_and_Diode_power_losses(Is, phi, V_dc, pf,
                                        dt, M, omega,
                                        t_on, t_off, f_sw,
                                        I_ref, V_ref, Err_D,
                                        R_IGBT, V_0_IGBT, R_D, V_0_D, input_step, t0=0.0):

    r = lambda x: float(round(float(x), 10))   # quantize for stable cache keys

    return _compute_IGBT_and_Diode_power_losses_cached(
        r(Is), r(phi), r(V_dc), r(pf),
        r(dt), r(M), r(omega),
        r(t_on), r(t_off), r(f_sw),
        r(I_ref), r(V_ref), r(Err_D),
        r(R_IGBT), r(V_0_IGBT), r(R_D), r(V_0_D),
        r(input_step), r(t0))