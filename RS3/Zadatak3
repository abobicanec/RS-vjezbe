import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFFds324'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_iz_baze, lozinka):
    await asyncio.sleep(2)  

    zapis = next(
        (z for z in baza_lozinka if z["korisnicko_ime"] == korisnik_iz_baze["korisnicko_ime"]),
        None
    )

    if zapis and zapis["lozinka"] == lozinka:
        return f"Korisnik ({korisnik_iz_baze['korisnicko_ime']}): Autorizacija uspješna."
    else:
        return f"Korisnik ({korisnik_iz_baze['korisnicko_ime']}): Autorizacija neuspješna."
    
async def autentifikacija(korisnik):
    korisnicko_ime = korisnik["korisnicko_ime"]
    lozinka = korisnik["lozinka"]

    await asyncio.sleep(3)

    korisnik_iz_baze = next(
        (k for k in baza_korisnika if k["korisnicko_ime"] == korisnicko_ime),
        None
    )

    if not korisnik_iz_baze:
        return f"Korisnik ({korisnicko_ime}) nije pronađen."
    
    rezultat = await autorizacija(korisnik_iz_baze, lozinka)
    return rezultat

async def main():
    test_korisnik = {
        "korisnicko_ime": "maja_0x",
        "email": "majaaaaa@gmail.com",
        "lozinka": "s324SDFFds324"
    }

    rezultat = await autentifikacija(test_korisnik)
    print(rezultat)


asyncio.run(main())
