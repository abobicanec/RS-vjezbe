def brojanje_rijeci(tekst):
    rijeci = tekst.split()  # dijeli tekst po razmacima
    frekvencija = {}
    for rijec in rijeci:
        if rijec in frekvencija:
            frekvencija[rijec] += 1
        else:
            frekvencija[rijec] = 1
    return frekvencija
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_rijeci(tekst))