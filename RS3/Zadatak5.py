import asyncio

async def secure_data(podatak):
    await asyncio.sleep(3)
    return {
        'prezime': hash(podatak['prezime']),
        'ime': hash(podatak['ime']),
        'broj_kartice': hash(podatak['broj_kartice']),
        'cvv': hash(podatak['cvv'])
    }
async def main():
    zadaci = [
        {'prezime': 'Peric', 'ime': 'Ivan', 'broj_kartice': '12345678', 'cvv': '111'},
        {'prezime': 'Anić', 'ime': 'Ana', 'broj_kartice': '87654321', 'cvv': '222'},
        {'prezime': 'Kos', 'ime': 'Marko', 'broj_kartice': '11223344', 'cvv': '333'},
    ]
    taskovi = [asyncio.create_task(secure_data(z)) for z in zadaci]
    rezultati = await asyncio.gather(*taskovi)
    print("Enkriptirani podaci:")
    for r in rezultati:
        print(r)

asyncio.run(main())