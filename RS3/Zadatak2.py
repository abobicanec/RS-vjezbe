import asyncio

import random

async def dohvat_korisnika():
    await asyncio.sleep(3)
    korisnici = [{"id": i, "ime": f"Korisnik{i}"} for i in range(1, 4)]
    return korisnici

async def dohvat_proizvoda():
    await asyncio.sleep(5)
    proizvodi = [{"id": i, "naziv": f"Proizvod{i}"} for i in range(1, 4)]
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(
        dohvat_korisnika(),
        dohvat_proizvoda()
    )

    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

asyncio.run(main())