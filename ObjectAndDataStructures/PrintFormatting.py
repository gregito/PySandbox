""" Stringek """

s = 'String'

print('A valtozo tartalma: %s' % s)
# 'A valtozo tartalma: String'

s = True
x = 'Other String'
print('Az elso valtozo tartalma: %s. Mig a masodike: %s' % (s, x))
# 'Az elso valtozo tartalma: True. Mig a masodike: Other String'


print('Elso: %s\nMasodik: %s\nHarmadik: %d' %('alma', True, 10))
# Elso: alma
# Masodik: True
# Harmadik: 10


# %s => string esetén bármilyen típust adunk meg inputként azt string-é konvertálja

# a %s -t lehet helyettesíteni %r -el is. gyakorlatban ugyan azt csinálják, csak más függvényt használnak
# %s -> str() ,  %r -> repr()



""" Format függvény """

print('Elso: {a} Masodik: {b}'.format(a='"beszurt szoveg"', b=True))
# Elso: "beszurt szoveg" Masodik: True



""" Lebegőpontos számok """

f = 13.145
print('Ez egy ket tizedesre roviditett lebegopontos szam: %2.3f' % f)
# 'Ez egy ket tizedesre roviditett lebegopontos szam: 13.14'
# A %1.2f -ben az első szám az, hogy az egész visszaadott tartalom >minimum< milyen hosszú kell legyen,
# a második pedig hogy hány tizedes számjegyet jelenítsen meg.
# ezutóbbi valójában kerekít, 5-ig lefelé, 6-tól felfelé.
# tehát ha 13.146-ot adtam volna meg, akkor 13.15-öt adott volna vissza a kiírásban
# ha a . után nagyobb szám van mint amennyi tizedes jegy az inputban, a maradékot feltölti nullával
# pl: %1.6f (13.145)  ->  13.145000
# az első számhoz fontos infó még, hogy ha nagyobb számot adunk meg, mint ahány karakter az egész
# szám, a maradékot feltölti a szám előtt whitespace-ekkel
# pl: %10.3f (13.145)  ->  '    13.145'   (10 karakter hosszú string, melyben a tizedes értékek száma 3)


