import asyncio

# Korutina odbrojava zadani broj sekundi
async def timer(name, delay):
    # Petlja od delay → 1 (odbrojavanje)
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        
        # PAUZA KORUTINE — predaja kontrole event loop-u
        # Event loop će ovu korutinu zaustaviti i nastaviti nakon 1 sekunde
        await asyncio.sleep(1)

     # Ovo se ispisuje tek nakon što petlja završi
    print(f'{name}: Vrijeme je isteklo!')

async def main():
     # STVARAJU SE TASK OBJEKTI — odmah se zakazuju u event loop
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    # Ovdje main() čeka da SVI taskovi završe
    # gather() paralelno izvršava sve timer korutine
    await asyncio.gather(*timers)

# Pokretanje event loop-a i glavne korutine
asyncio.run(main())
