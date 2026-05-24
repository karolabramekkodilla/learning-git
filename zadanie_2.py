liczby = []
liczby_podzielne_przez_5 = []
liczy_do_potegi_3 = []
for i in range(0,101):
    liczby.append(i)
# print(liczby)
for item in liczby:
    if item%5 == 0:
        liczby_podzielne_przez_5.append(item)
print(liczby_podzielne_przez_5)
print([item ** 3 for item in liczby_podzielne_przez_5])

print("zadanie dodane w ramach ćwiczenia git")
    
