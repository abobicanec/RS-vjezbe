import random

tajni_broj = random.randint(1,100)

pogoden = False
broj_pokusaja =0

print("Pogodi broj između 1 i 1000")

while not pogoden:
    pokusaj=int(input("Unesi svoj broj:"))
    broj_pokusaja+=1
    if pokusaj <tajni_broj:
        print("Tvoj broj je manji od traženog.")
    elif pokusaj > tajni_broj:
        print("Tvoj broj je veći od traženog.")
    else:
        pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")