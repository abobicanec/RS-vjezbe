import asyncio
import aiohttp

DOG_URL = "https://dogapi.dog/api/v2/facts"
CAT_URL = "https://catfact.ninja/fact"


async def get_dog_fact(session: aiohttp.ClientSession) -> str:
    """Dohvati jedan dog fact sa dogapi.dog"""
    async with session.get(DOG_URL) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return data["data"][0]["attributes"]["body"]


async def get_cat_fact(session: aiohttp.ClientSession) -> str:
    """Dohvati jedan cat fact sa catfact.ninja"""
    async with session.get(CAT_URL) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return data.get("fact", "")


def mix_facts(dog_facts, cat_facts):
    """Ako je dog fact dulji — uzmi njega, inače cat fact."""
    mixed = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed.append(dog_fact)
        else:
            mixed.append(cat_fact)
    return mixed


async def main():
    async with aiohttp.ClientSession() as session:

        dog_tasks = [asyncio.create_task(get_dog_fact(session)) for _ in range(5)]
        cat_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]


        dog_cat_facts = await asyncio.gather(*dog_tasks, *cat_tasks)

        dog_facts = dog_cat_facts[:5]
        cat_facts = dog_cat_facts[5:]

        mixed = mix_facts(dog_facts, cat_facts)

        print("Mixane činjenice o psima i mačkama:")
        for fact in mixed:
            print(fact)


if __name__ == "__main__":
    asyncio.run(main())