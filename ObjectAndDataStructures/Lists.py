""" Listák """

list = [1, 2, 3]
print(list)                 # [1, 2, 3]


# a listákban különböző típusú értékek is lehetnek
list = ['string', 12, 1.2, 'o', True]
print(list)                             # ['string', 12, 1.2, 'o', True]


print(len(list))            # 5

print(list[2])              # 1.2  -  a lista 2-es indexen levő eleme

print(list[1:])             # [12, 1.2, 'o', True]  -  az 1. indexen levő elemtől (azt is beleértve) adja vissza

print(list[:3])             # ['string', 12, 1.2]  -  a 3. indexen levő elemig (azt már nem) adja vissza


print(list * 2)             # ['string', 12, 1.2, 'o', True, 'string', 12, 1.2, 'o', True]

""" listához elem hozzáadás (végéhez) """
list += ['new item']
print(list)                 # ['string', 12, 1.2, 'o', True, 'new item']

l = [1, 2, 3]
l.append('new item again')
print(l)                    # [1, 2, 3, 'new item again']



""" Pop """
# a .pop() visszaadja és egyben ki is veszi a lista adott/utolsó elemét
l = [1, 2, 3]
print(l)                    # [1, 2, 3]
print(l.pop())              # 3
print(l)                    # [1, 2]

# meg lehet adni a .pop() -nak argumentumot is, ami azt adja meg, melyik indexen levő elemet szeretnénk kivenni.
# ez alapértelmezetten -1 (ugye a legutolsó elem)
l = [1, 2, 3]
print(l)                    # [1, 2, 3]
print(l.pop(1))             # 2
print(l)                    # [1, 3]



""" Rendezés és sorrend megfordítás """

s_list = ['a', 'c', 'e', 'b', 'd', 'f']
s_list.sort()
print(s_list)               # ['a', 'b', 'c', 'd', 'e', 'f']

s_list.reverse()
print(s_list)               # ['f', 'e', 'd', 'c', 'b', 'a']


""" Mátrix """

l_1 = [1, 3, 5]
l_2 = [4, 2, 1]
l_3 = [7, 6, 9]

matrix = [l_1, l_2, l_3]
print(matrix)               # [[1, 3, 5], [4, 2, 1], [7, 6, 9]]
print(matrix[2][1])         # 6 -------------------------^

# a mátrix egy adott oszlopának kivétele
first_col = [row[0] for row in matrix]
print(first_col)            # [1, 4, 7]


