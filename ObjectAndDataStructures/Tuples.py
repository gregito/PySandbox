""" Tuples """

# hasonló a listához, csak elemei nem módosíthatóak
# használata akkor javasolt ha olyan értéket szeretnénk letárolni ami nem fog változni (pl naptár)

t1 = (1, 2, 3)

print(len(t1))                  # 3
print(t1[0])                    # 1
print(t1[-1])                   # 3  -  hátulról az 1. elem

# szintén keverhetőek a típusok
t2 = (1, True, "alma", .22, False)

# érdekesség: a python a logikai értékeknek is társít számértéket (ahogy az alacsony szinteken megszokott),
# tehát a t2-es listából ha kikérem a 0 értékű elemek számát, akkor 1-el fog visszatérni, mert bár nincs
# nullás elem, de a False értéke 0. Ugyan ez, ha az 1 értékű elemek számosságát kérjük ki, 2-vel fog visszatérni,
# mert ott az 1, és a True
print(t2.count(0))              # 1
print(t2.count(1))              # 2



# adott elem indexének visszaadása:
t3 = ("szilva", "korte", "alma", "barack", "alma")
print(t3.index("alma"))         # 2

# megjegyzés: a listához, ha az index keresésekor olyan elemre keresünk, mely többször szerepel az objektumban,
# az első előforduló elem indexét kapjuk vissza
