""" Files """

import os


PACKAGE_ROOT = os.path.abspath("")
FILE_PATH = os.path.join(PACKAGE_ROOT, 'test.txt')

file = open(FILE_PATH)
print(file.read())         # kiírja a txt tartalmát

print(file.read())         # semmit nem ír ki

# miért nem ír ki semmit?
# mert az f objektum, mely tartalmazza a txt fájunk tartalmát. kiolvastuk mi van benne, és a képzeletbeli
# kurzor most a file végén van, így az f.read() utasításra nem tud további tartalmat visszaadni.
# hogy újra ki tudjuk olvasni, ismét vissza kell állítani az elejére ( vagy egy kívánt pozícióra )
# erre jó a .seek(index) parancs
file.seek(0)

print(file.read())         # kiírja a txt tartalmát

file.seek(0)
print(file.readlines())    # visszaadja a txt tartalmát egy lista formájában úgy, hogy minden sor a lista egy eleme
# [Fontos!] megjegyzés: a .readlines() függvény a visszaadásig a memóriában tárolja a tartalmát, így nagyon nagy/hosszú
# fájlok beolvasása esetén előfordulhat hogy a függvény felemészti a memóriát!


""" Soronkénti olvasás és végigjárás """
file.seek(0)
print(file.readline())     # visszatér az adott sor tartalmával

file.seek(0)
for line in file:          # sorban kiírja a file tartalmát a végéig
    print(line)

""" Fájl létrehozás és írás """
NEW_FILE_PATH = os.path.join(PACKAGE_ROOT, 'asd.rtf')

if os.path.exists(NEW_FILE_PATH):           # biztonság kedvéért leelenőrizzük hogy létezik-e a fájl
    try:
        os.remove(NEW_FILE_PATH)            # ha igen, megpróbáljuk törölni
    except Exception:
        print("Hiba a fajl torlesekor!")


new_file = open(NEW_FILE_PATH, 'w')                         # létrehozzuk a fájlt írásra
new_file.write("Oy pirates!\nLet's make some trouble!")     # beleírjuk a kívánt szövege(ke)t
new_file.close()                                            # lezárjuk a fájlt

new_file = open(NEW_FILE_PATH)              # (újból) megnyitjuk olvasásra
for line in new_file:                       # kiíratjuk soronként a tartalmát
    print(line)
