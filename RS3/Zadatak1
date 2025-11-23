import asyncio

async def dohvat_podataka():
    podaci = [x for x in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    return podaci

async def main():
    rezultat = await dohvat_podataka()
    print("Rezultat:", rezultat)

asyncio.run(main())