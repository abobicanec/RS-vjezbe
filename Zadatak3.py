#1
parni_kvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati)

#2
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorrinolaringolog"]

duljine_sa_slovom_a = [len(r) for r in rijeci if "a" in r]
print(duljine_sa_slovom_a)

#3
kubovi = {x: (x**3 if x % 2 != 0 else x) for x in range(1, 11)}
print(kubovi)

#4
import math

korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}
print(korijeni)

#5
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [3, 13, 35, 44, 25]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [9, 8, 21, 11]},
    {"ime": "Petar", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 89]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 47, 56, 23]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{s["prezime"]: sum(s["bodovi"])} for s in studenti]

print(zbrojeni_bodovi)

#6
import math

faktorijeli = {x: math.factorial(x) for x in range(1, 11)}
print(faktorijeli)

