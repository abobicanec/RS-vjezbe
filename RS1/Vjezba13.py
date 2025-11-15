#zadatak1
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))

#zadatak2

def maks_i_min(lista):
    maks = lista[0]
    min_ = lista[0]
    for broj in lista[1:]:
        if broj > maks:
            maks = broj
        if broj < min_:
            min_ = broj
    return (maks, min_)
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))

#zadatak3
def presjek(skup1, skup2):
    return {x for x in skup1 if x in skup2}
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2)) 
