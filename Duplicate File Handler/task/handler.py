# write your code here
import hashlib
import sys
from collections import defaultdict
from pathlib import Path

if len(sys.argv) == 1:
    print("Directory is not specified")
    sys.exit(0)

file_format = input("Enter file format:\n")

while True:
    volgorde = input("Size sorting options:\n1. Descending\n2. Ascending\n")

    if volgorde in ["1", "2"]:
        break
    else:
        print("Wrong option")

root_folder = sys.argv[1]

if file_format == "":
    windows_paths = list(Path(root_folder).rglob("*"))
else:
    windows_paths = list(Path(root_folder).rglob(f"*.{file_format}"))

dictonary = defaultdict(list)
for path in windows_paths:
    if not path.is_dir():
        dictonary[path.stat().st_size].append(path)

if volgorde == "1":
    dictonary = dict(sorted(dictonary.items(), reverse=True))
else:
    dictonary = dict(sorted(dictonary.items(), reverse=False))

for size, path in dictonary.items():
    if len(path) > 1:
        print(f'\n{path[0].stat().st_size} bytes')

        for path3 in path:
            print(path3)

# ask yes/no
while True:
    check_duplicates = input("\nCheck for duplicates?\n")

    if check_duplicates not in ["no", "yes"]:
        print("Wrong option")

    elif check_duplicates == "no":
        sys.exit(0)
    else:
        break

dictonary_hex = defaultdict(lambda: defaultdict(list))


def bereken_hash(file: Path) -> str:
    hash = hashlib.md5()

    with open(file, "rb") as f:
        hash.update(f.read())

    return hash.hexdigest()


for size, size_paths in dictonary.items():
    if len(size_paths) <= 1:
        continue

    for path in size_paths:
        dictonary_hex[size][bereken_hash(path)].append(path)


counter = 1
for size, hexes in dictonary_hex.items():
    size_written = False
    for hex, hex_paths in hexes.items():
        if len(hex_paths) <= 1:
            continue

        if not size_written:
            print(f'\n{size} bytes')
            size_written = True

        print(f'Hash: {hex}\n')
        for path in hex_paths:
            print(f"{counter}. {path}")
            counter += 1
# ask yes/no
while True:
    yes_or_no = input("Delete files?\n")

    if len(yes_or_no.split()) != 3:
        print("\nWrong format")
    else:
        break

