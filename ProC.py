
import os

print("=== PL-T Compiler ===")

source = input("Forrásfájl útvonala: ").strip()
output = input("Kimeneti fájlnév: ").strip()

if not os.path.exists(source):
    print("Forrásfájl nem található.")
    exit()

with open(source, "r", encoding="utf-8") as file:
    content = file.read()

compiled = f"""
# Compiled PL-T File

code = {repr(content)}

print("PL-T Program Indul")
exec(code)
"""

with open(output + ".py", "w", encoding="utf-8") as out:
    out.write(compiled)

print("Fordítás kész.")
