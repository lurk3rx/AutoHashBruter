import re
import os
import subprocess
import argparse

wordlist = "/usr/share/wordlists/rockyou.txt"

parser = argparse.ArgumentParser()

parser.add_argument(
    "-d", "--directory",
    type=str,
    default="./",
    help="Директория TXT файлов с хэшами"
)

parser.add_argument(
    "-o", "--output",
    type=str,
    default="cracked_hashes.txt",
    help="Вывод данных в файл"
)

args = parser.parse_args()
def get_hashcat_modes(hash_value):
    result = subprocess.run(
        ['hashcat', '--identify', hash_value],
        capture_output=True,
        text=True
    )
    modes = re.findall(r'^\s*(\d+)\s+\|', result.stdout, re.MULTILINE)

    return sorted(int(mode) for mode in modes)
def collect_hashes_from_txt_files(directory):
    hashes = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                cleaned_lines = [line.strip() for line in lines]
                hashes.extend(cleaned_lines)
    return hashes
 
hashes = collect_hashes_from_txt_files(args.directory) # Тут список хэшей

print(f"Итоговый список хешей: {hashes}")
for i in range(len(hashes)):
    mods_hashes = get_hashcat_modes(hashes[i])
    print(f"Брутим хэш {hashes[i]}")
    m = 0
    for m in range(len(mods_hashes)):     
        result = None
        output = subprocess.check_output(["hashcat",  "-m", str(mods_hashes[m]), "-a", "0", hashes[i], wordlist],  stderr=subprocess.STDOUT, text=True)
        if "--show" in output:
            with open(args.output, "a") as file:
                file.write(f"{subprocess.check_output(["hashcat", "-m", str(mods_hashes[m]), "-a", "0", hashes[i], wordlist, "--show"], stderr=subprocess.STDOUT, text=True)}")
            break
        else: 
            if "Cracked" in output:
                match = re.search(r"([a-f0-9]{32}):(.+)", output)
                if match:
                    result = match.group(0)
                with open(args.output, "a") as file:
                    file.write(f"{result}\n")
                break
            else:
                print(f"{hashes[i]} с модом {mods_hashes[m]} не взломан")

