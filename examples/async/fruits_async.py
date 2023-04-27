import time
import asyncio


async def fetch_data(id: int):
    db = {
        1: 'apples',
        2: 'oranges',
        3: 'bananas',
    }
    # simulate the time it takes to fetch data from a remote db
    # using asyncio.sleep for asynchronous programming
    await asyncio.sleep(1)
    data = db[id]
    print(f'{data} fetched successfully!')
    return data


async def main():
    aws = []
    for id in range(1, 4):
        aws.append(fetch_data(id))

    await asyncio.gather(*aws)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'It took {end - start:.4f}s.')
