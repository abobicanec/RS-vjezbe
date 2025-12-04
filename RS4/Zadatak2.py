import asyncio
import aiohttp
import re
from typing import List

API_URL = "https://catfact.ninja/fact"
FACTS_COUNT = 20
PATTERN = re.compile(r"\bcat(s)?\b", re.IGNORECASE)

async def get_cat_fact(session: aiohttp.ClientSession) -> str:
    """Dohvati jedan cat fact iz API-ja i vrati tekst facta."""
    async with session.get(API_URL) as resp:
        resp.raise_for_status()
        data = await resp.json()

        return data.get("fact", "")

def filter_cat_facts(facts: List[str]) -> List[str]:
    """Vrati samo facts koji sadrže riječ 'cat' ili 'cats' (case-insensitive)."""
    return [f for f in facts if f and PATTERN.search(f)]

async def main():
    async with aiohttp.ClientSession() as session:

        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(FACTS_COUNT)]

        results = await asyncio.gather(*tasks, return_exceptions=False)

    filtered = filter_cat_facts(results)

    print("Filtrirane činjenice o mačkama:")
    for fact in filtered:
        print("- " + fact)

if __name__ == "__main__":
    asyncio.run(main())
