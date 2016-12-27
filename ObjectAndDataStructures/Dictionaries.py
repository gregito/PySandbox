""" Dictionaries """

# hasonló a hashtable-höz
# a listákkal ellentétben, amik az elemeiket a relatív pozíviójuk alapján azonosítják,
# itt mappelésről van szó, tehát egy elemet, a hozzá tartozó kulcs azonosít.
# ebből adódóan lényeges infó, hogy egy Dictionary-ben az elemek nem tartanak egy adott sorrendhez, mert nem az
# objektumban elfoglalt pozíciójuk alapján hivatkozunk rájuk
# a kulcs megadásánál annyi típusmegkötés van, hogy hashelhetőnek kell lennie, pl lista nem lehet, de
# az érték megadásnál ezt már nem kell figyelembe venni (tehát ott már megengedett a lista is)

l = ['alma', 'korte']
dict = {'key1': 'value1', 'key2': 2, 'key3': True, 3.5: 12.22, 'lista': l}

print(dict)             # {'key1': 'value1', 'key2': 2, 'key3': True, 3.5: 12.22, 'lista': ['alma', 'korte']}
print(dict['key1'])     # value1
print(dict['key3'])     # True
print(dict['lista'])    # ['alma', 'korte']


# ha azonos kulccsal hozunk létre elemet, az azonosak közül az utolsó lesz az érvényes
dict2 = {True: 'alma', True: 'korte', False: 2}

print(dict2)            # {True: 'korte', False: 2}


# a vissztérési értékre jellemző funkciók elérhetőek lesznek, de ezek csak futási időben fognak kiértékelődni,
# így ha egy (nem várt) elemen szeretnénk olyan műveletet végrehajtani ami arra a típusra nem elérhet/megengedett,
# akkor az csak akkor fog kiderülni, mikor ráfut a kód

print(dict['key1'][::-1])       # '1eulav'  -  a visszakapott stringet fordítva iratja ki
print(dict['key1'].upper())     # VALUE1
print(dict[3.5] * 2 - 4)        # 20.44  -  megduplázza a kinyert 12.22 értéket majd kivon 4-et

print(dict)                 # {'key1': 'value1', 'key2': 2, 'key3': True, 3.5: 12.22, 'lista': ['alma', 'korte']}
print(dict['lista'].pop())  # korte  -  visszaadta és ki is vette a 'lista' kulcsú elem (ami ugye egy lista) utolsó elemét
print(dict)                 # {'key1': 'value1', 'key2': 2, 'key3': True, 3.5: 12.22, 'lista': ['alma']}



""" Elem módosítás """
dict['key1'] = 'new ' + dict['key1']
print(dict)                 # {'key1': 'new value1', 'key2': 2, 'key3': True, 3.5: 12.22, 'lista': ['alma']}




""" Elem kivétele """
# szintén kulcs megadásával ki lehet venni egy adott kulcs-érték párt. annyi (fontos) eltérés van a listától,
# hogy itt KÖTELEZŐ megadni, melyik elemet akarjuk kivenni

dict3 = {'k1': 'value1', 'k2': 23, 'k3': True}

print(dict3)                # {'k1': 'value1', 'k2': 23, 'k3': True}
print(dict3.pop('k2'))      # 23
print(dict3)                # {'k1': 'value1', 'k3': True}




""" Elem hozzáadás/feltöltés """
# hasonlóan a listákhoz, itt is meg lehet adni üresen az objektumunkat, majd később tetszés szerint bővíthetjük

e_dict = {}
print(e_dict)               # {}

e_dict['first'] = 'firstValue'
print(e_dict)               # {'first': 'firstValue'}




""" Egymásba ágyazott szótárak """
# a listákhoz hasonlóan itt is könnyen egymásba ágyazhatóak a szótárak

m_dict = {'k1': {'n_key1': {'s_n_key1': 's_n_value1'}}, 'k2': {'n_key2': {'s_n_key2': 's_n_value2'}}}

"""
Hogyan képzeljük el ezt:
    k1:
       n_key1:
             s_n_key1: s_n_value1
    k2:
       n_key2:
             s_n_key2: s_n_value2

ez alapján egy ilyen szerkezetből az értékkinyerés a következő:
"""
print(m_dict['k1']['n_key1']['s_n_key1'])           # 's_n_value1'




""" Kulcsok és értékek kiíratása """
k_dict = {'k1': 12, 'fruit': "alma", 'float_num': 12.2251}

#kulcsok kiíratása:
print(k_dict.keys())                # dict_keys(['k1', 'fruit', 'float_num'])

#értékek kiíratása:
print(k_dict.values())              # dict_values([12, 'alma', 12.2251])

#mindkettő kiíratása:
print(k_dict.items())               # dict_items([('k1', 12), ('fruit', 'alma'), ('float_num', 12.2251)])

# megjegyzés: a .items() tuple(öket) ad vissza, tehát az elemei (típuskényszerítés és változóba töltés nélkül)
# nem szerkeszthetőek/kiemelhetőek



