def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati izmedu 8 i 15 znakova")
        return

    ima_veliko = any(c.isupper() for c in lozinka)
    ima_broj = any(c.isdigit() for c in lozinka)
    if not (ima_veliko and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return

    lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return

    print("Lozinka je jaka!")

lozinka_unos = input("Unesite lozinku: ")
provjera_lozinke(lozinka_unos)
