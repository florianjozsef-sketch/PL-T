
# PL-T Programming Language

PL-T egy egyedi programozási nyelv Python alapokon.

## Funkciók
- Interpreter (`PLT.exe`)
- Compiler (`ProC.exe`)
- VS Code Extension
- `.plt` fájl támogatás
- Egyszerű szintaxis

## Példa

```plt
print "Helló világ!"
input name
print name
```

## Fordítás EXE-vé

```bash
pip install pyinstaller
pyinstaller --onefile PLT.py --name PLT
pyinstaller --onefile ProC.py --name ProC
```

## GitHub Topics
- programming-language
- compiler
- interpreter
- plt-language
- vscode-extension
