from pathlib import Path
from markitdown import MarkItDown

md = MarkItDown()

def _convert(input_folder, ext):
    input_folder = Path(input_folder)
    output_folder = input_folder / "markdown"
    output_folder.mkdir(exist_ok=True)

    files = [p for p in input_folder.rglob("*")
             if p.suffix.lower() == ext
             and not p.name.startswith("~$")
             and output_folder not in p.parents]
    print(f"Found {len(files)} {ext} files\n")

    done, skipped, failed = 0, 0, []
    for i, f in enumerate(files, start=1):
        out_file = output_folder / f.relative_to(input_folder).with_suffix(".md")
        out_file.parent.mkdir(parents=True, exist_ok=True)

        if out_file.exists():
            print(f"[{i}/{len(files)}] Skipped: {f.name}")
            skipped += 1
            continue
        try:
            out_file.write_text(md.convert(str(f)).markdown, encoding="utf-8")
            print(f"[{i}/{len(files)}] Converted: {f.name}")
            done += 1
        except Exception as e:
            print(f"[{i}/{len(files)}] FAILED: {f.name} -> {e}")
            failed.append(f.name)

    print(f"\nDone. Converted: {done}, Skipped: {skipped}, Failed: {len(failed)}")
    for name in failed:
        print("  -", name)
    print(f"Saved in: {output_folder}\n")

def convert_pdfs(input_folder):
    _convert(input_folder, ".pdf")

def convert_csvs(input_folder):
    _convert(input_folder, ".csv")

def convert_xlsx(input_folder):
    _convert(input_folder, ".xlsx")

convert_pdfs(r"C:\Users\ge26cih\Downloads")
#convert_csvs(r"C:\Users\ge26cih\Downloads")
#convert_xlsx(r"C:\Users\ge26cih\Downloads")