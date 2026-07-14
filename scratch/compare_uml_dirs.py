import os
import filecmp
import sys
import difflib

report_uml = r"d:\LapTrinhWeb\manga-workflow-report\UML"
code_uml = r"d:\LapTrinhWeb\manga-workflow-report\Manga-publishing-management-system\UML"
output_file = r"d:\LapTrinhWeb\manga-workflow-report\scratch\compare_uml_results.txt"

out = []

out.append("Comparing report UML with code UML:\n")
report_files = sorted(os.listdir(report_uml))
code_files = sorted(os.listdir(code_uml))

only_report = set(report_files) - set(code_files)
only_code = set(code_files) - set(report_files)

if only_report:
    out.append(f"Only in report UML: {only_report}\n")
if only_code:
    out.append(f"Only in code UML: {only_code}\n")

common_files = set(report_files).intersection(set(code_files))
diff_files = []
for file in common_files:
    f1 = os.path.join(report_uml, file)
    f2 = os.path.join(code_uml, file)
    if not filecmp.cmp(f1, f2, shallow=False):
        diff_files.append(file)

if diff_files:
    out.append(f"Files that differ: {diff_files}\n")
    for file in diff_files:
        out.append(f"\n--- Diff for {file} ---\n")
        with open(os.path.join(report_uml, file), "r", encoding="utf-8") as f:
            lines1 = f.readlines()
        with open(os.path.join(code_uml, file), "r", encoding="utf-8") as f:
            lines2 = f.readlines()
        diff = difflib.unified_diff(lines1, lines2, fromfile="report/"+file, tofile="code/"+file)
        out.append("".join(diff) + "\n")
else:
    out.append("All common files are identical!\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(out))

print("Done! Results written to scratch/compare_uml_results.txt")
