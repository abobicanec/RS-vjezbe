from shop.proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        tekst = "Naručeni proizvodi: "
        tekst += ", ".join(f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi)
        tekst += f", Ukupna cijena: {self.ukupna_cijena} eur"
        print(tekst)


narudzbe = []

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        print("Greška: naručeni proizvodi moraju biti lista!")
        return None
    if len(lista_proizvoda) == 0:
        print("Greška: lista proizvoda je prazna!")
        return None

    for p in lista_proizvoda:
        if not isinstance(p, dict):
            print("Greška: svaki proizvod mora biti rječnik!")
            return None
        if any(k not in p for k in ("naziv", "cijena", "narucena_kolicina")):
            print("Greška: nedostaju obavezni ključevi!")
            return None

        skladisni_proizvod = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not skladisni_proizvod or skladisni_proizvod.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None

    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in lista_proizvoda)

    narudzba = Narudzba(lista_proizvoda, ukupna_cijena)
    narudzbe.append(narudzba)

    # ažuriranje skladišta
    for p in lista_proizvoda:
        skladisni_proizvod = next(s for s in skladiste if s.naziv == p["naziv"])
        skladisni_proizvod.dostupna_kolicina -= p["narucena_kolicina"]

    return narudzba
