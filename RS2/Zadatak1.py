#1 kvadriranje broja:
def kvadriraj(x):
    return x ** 2

kvadriraj = lambda x: x **2

print(kvadriraj(4))

#2 Zbroji pa kvadriraj
def zbroji_pa_kvadriraj(a,b):
    return (a+b) **2

zbroji_pa_kvadriraj = lambda a,b: (a+b) **2
print(zbroji_pa_kvadriraj(1,3))

#3 Kvadriraj duljinu niza
def kvadriraj_duljinu(niz):
    return len(niz)**2

kvadriraj_duljinu = lambda niz: len(niz) **2
print(kvadriraj_duljinu("test"))

#4 Pomnoži vrijednost s 5 pa potenciraj na x
def pomnozi_i_potenciraj(x,y):
    return (y*5) **x

pomnozi_i_potenciraj = lambda x,y: (y*5) **x
print(pomnozi_i_potenciraj(1,2))

#5 Vrati True ako je broj para, inače None
def paran_broj(x):
    if x % 2==0:
        return True
    else: 
        return None
    
    paran_broj = lambda x: True if x % 2 == 0 else None
print(paran_broj(1))
print(paran_broj(2))


