broj1=float(input("Unesite prvi broj: "))
broj2=float(input("Unesite drugi broj: "))
operatorr= input ("Unesite operator (+,-,*,/):")

if operatorr == '+':
    rezultat=broj1+broj2
    print(f"Rezultat operacije{broj1}+{broj2} je {rezultat}")
elif operatorr == '-':
    rezultat = broj1 - broj2
    print(f"Rezultat operacije {broj1} - {broj2} je {rezultat}")
elif operatorr == "*":
    rezultat = broj1 - broj2
    print(f"Rezultat operacije {broj1} * {broj2} je {rezultat}")
elif operatorr == '/':
    if broj2==0:
        print("Dijeljenje s nulom nije dozvoljeno")
    else:
        rezultat = broj1/broj2
        print(f"Rezultat operacije {broj1}/{broj2} je {rezultat}")

else:
    print("Nepodržani operator!")
    
