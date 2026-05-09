
import os

print("=== PL-T Interpreter ===")
filepath = input("Program fájl útvonala: ").strip()

if not os.path.exists(filepath):
    print("Nem található a fájl.")
    exit()

with open(filepath, "r", encoding="utf-8") as file:
    code = file.readlines()

variables = {}

for line in code:
    line = line.strip()

    if not line:
        continue

    if line.startswith("print "):
        content = line[6:]

        if content.startswith('"') and content.endswith('"'):
            print(content[1:-1])

        elif content in variables:
            print(variables[content])

        else:
            print(content)

    elif line.startswith("input "):
        varname = line[6:]
        variables[varname] = input(f"{varname}: ")

    elif "=" in line:
        varname, value = line.split("=", 1)
        variables[varname.strip()] = value.strip().replace('"', '')

print("=== Program vége ===")
