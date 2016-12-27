""" Set """

# Set: egyedi elemek halmaza
# ez annyit tesz, hogy egy Set-ben nem lehet két ugyan olyan elem (ahogy egy Dict.-ben sem lehet két azonos kulcs)
# gyakorlatilag egy matematikai halmaz megvalósítása

x = set()

x.add('alma')
print(x)                                    # {'alma'}

# ahogy megszokott, itt is lehet különböző típusokat keverni
x.add(2)
print(x)                                    # {2, 'alma'}


l = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
print(l)                                    # [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
print(set(l))                               # {1, 2, 3, 4, 5, 6}


# két Set (halmaz) úniója   2, 3, 4, 5, 7
a = set()
a.add(1)
a.add(3)
a.add(5)
a.add(6)

b = set()
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(7)

a_U_b = a.union(b)
print(a_U_b)                                    # {1, 2, 3, 4, 5, 6, 7}


# set-et meg lehet adni úgy mint szótár, csak értékek nélkül (de ettől még Set lesz!)
c = {1, 2, 5, 6, 9}
d = {2, 3, 6, 7}

c_U_d = c.union(d)
print(c_U_d)                                    # {1, 2, 3, 5, 6, 7, 9}



""" Boolean """

a = False

# A boolean értékek reprezentálnak számot is, 1 vagy 0

print(True.bit_length())                        # 1
print(False.bit_length())                       # 0

# ebből adódóan lehetséges ez is:
print(False < True)                             # True



# speciális "objektum" a None. Ezzel alapértelmezett üres állapotba lehet hozni egy változót (hasonló a Java null-jához)

var1 = "korte"                                  # itt megtörténik a var1 változó String típusúként történő azonosítása

print(var1)                                     # 'korte'

var1 = None                                     # itt 'resetelődik', azaz olyan típusú lesz amihez nincsenek függvények
                                                # redelve

print(var1)                                     # None


