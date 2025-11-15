class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} eur, Dostupna količina: {self.dostupna_kolicina}")


# Inicijalno stanje skladišta s 2 proizvoda
skladiste = [
    Proizvod("Stolica", 150, 15),
    Proizvod("Stol", 500, 5)
]

# Funkcija za dodavanje novih proizvoda
def dodaj_proizvod(proizvod_dict):
    novi_proizvod = Proizvod(
        proizvod_dict["naziv"],
        proizvod_dict["cijena"],
        proizvod_dict["dostupna_kolicina"]
    )
    skladiste.append(novi_proizvod)
