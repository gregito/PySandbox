from __future__ import division  # a future module-ból importálja a division-t (  < python 3.0 alatt lehet szükséges )
import math

# a python figyelembe veszi a matematikai műveleti sorrend megkötéseket

""" alapműveletek """

print(2 + 5)    # 7

print(float(5) / 2)     # 2.5

print(float(5/2))       # 2.5

print(5.0 / 2)          # 2.5

print(5 / 2)            # 2.5  <– python 3.0 alatt ez csak az egész részt adja vissza, ha nincs beimportálva a fenti division

print(5 // 2)           # 2  – egészrész

print(5 % 2)            # 1  – maradék


""" hatványozás és gyök """

print(2 ** 3)           # 8  (2^3)

print(math.pow(2, 5))   # 32.0 (2^5)

print(5 ** -2)          # .004 (5^-2)

n = 6
print(5 ** (1/n))       # 1.3076604860118306 ( az 5 n-edik gyöke )


"""
- nevek (változók) nem kezdődhetnek számmal
- nem lehet space a nevekben ('_' karakter használata javasolt helyette)
- nem használhatóak ezek a karakterek: :'",<>/?|\()!@#$%^&*~-+
- a konvenciók szerint a neveket kisbetűvel írjuk
"""

my_income = 100
tax_rate = .1
my_taxes = my_income * tax_rate

print(my_taxes.__trunc__())     # 10  –  trunc nélkül 10.0 lett volna


