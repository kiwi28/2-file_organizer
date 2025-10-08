from pathlib import Path
import shutil

# from collections import defaultdict

currentPath = Path("./test/")

files = [file for file in currentPath.iterdir()]
# print(files)
grouped = {
    ext: [f for f in files if f.suffix == ext]
    for ext in set(file.suffix for file in files if file.is_file())
}
# print("grouped", grouped)

try:
    Path("./NEW").mkdir()
except FileExistsError:
    print("folder already exists")

try:
    Path("./NEW/status.txt").touch()
except FileExistsError:
    print("status file already exists")

with open("NEW/status.txt", "w") as file:
    file.write("File Organization Report\n")
    file.write("=" * 30 + "\n\n")

    for ext, files_list in grouped.items():
        file.write(f"\n{ext}: {len(files_list)} files\n")
        destPath = Path("./NEW") / ext

        try:
            destPath.mkdir()
        except FileExistsError:
            print(f"folder{ext} already exists")

        # folder exists at this point
        # sourcepath =
        for filePath in files_list:
            src = filePath.as_posix()
            shutil.copy2(src, destPath)

            file.write(f"  - {filePath.name}\n")


# with open("report.txt", "w") as file:
#     file.write("File Organization Report\n")
#     file.write("=" * 30 + "\n\n")

#     # Write multiple lines in a loop
#     for ext, files in grouped.items():
#         file.write(f"{ext}: {len(files)} files\n")
#         for f in files:
#             file.write(f"  - {f.name}\n")
