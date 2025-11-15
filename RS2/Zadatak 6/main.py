from shop.proizvodi import dodaj_proizvod, skladiste
from shop.narudzbe import napravi_narudzbu

# Proizvodi za dodavanje
proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Mis", "cijena": 108, "dostupna_kolicina": 100}
]

# Dodavanje proizvoda u skladiste
for p in proizvodi_za_dodavanje:
    dodaj_proizvod(p)

# Ispis svih proizvoda u skladistu
print("Trenutno stanje skladišta:")
for p in skladiste:
    p.ispis()

# Kreiranje narudzbe
naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

narudzba = napravi_narudzbu(naruceni_proizvodi)
if narudzba:
    print("\nIspis narudžbe:")
    narudzba.ispis_narudzbe()
