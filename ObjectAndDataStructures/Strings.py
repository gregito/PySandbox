

print('Hello World' + " | Hello World 2")

# általában mindegy melyiket használjuk, azonban ahol pl I'm van, ott muszáj a " jelet használni, hogy a ' ne zárja le
# a Stringet:

print("I'm")


# fordítva ha a " jelet szeretnénk megjeleníteni a szövegben, akkor ' jelek közé kell foglalni
print('"alma"')


"""
Fontos!
Python 3-ban a print már nem egy statement, hanem egy függvény.
print 'alma'
  helyett
print('alma)

ha a 3.0 alatt szeretnénk használni a függvényt, akkor importálni kell a print_function -t
a __future__ modulból

from __future__ import print_function
"""



hw = 'Hello World'
print(len(hw))          # 11  –  szöveghossz

print(hw[1])            # 'e'  –  a szekvencia 2. betűje (szintén 0-tól történik az indexelés)

print(hw[1:])           # 'ello World'  –  tól-ig visszaadja a szekvencia (szöveg) tartalmát

print(hw[:3])           # 'Hel'

print(hw[:3] + hw[3:])  # 'Hello World'  –  egyenlő a print(hw[:]) -vel

print(hw[-1])           # 'd'  –  ha negatív számot adunk meg, visszaloopol a végére és onnan számol

print(hw[:-1])          # 'Hello Worl'

print(hw[::1])          # 'Hello World'  –  :: jelöli hogy az egész szövegre értjük, a szám pedig a lépésközt

print(hw[::2])          # 'HloWrd'

print(hw[2:len(hw):2])  # 'loWrd'  –  a 2. indexen levő karaktertől a szöveg hosszának megfelelő indexű karakterig 2 lépésközzel

print(hw[::-1])         # 'dlroW olleH'  -  a step itt -1, azaz fordított sorrendben adja vissza a tartalmat

print(hw * 2)           # 'Hello WorldHello World'  –  stringet szorozva annyiszor írja ki ahánnyal megszorozzuk

print(hw.upper())       # 'HELLO WORLD'

print(hw.lower())       # 'hello world'

print(hw.split('e'))    # ['H', 'llo World']  –  a megadott elem kivetlével egyszerre szétválasztja és visszaad x listát

