import time


def fetch_data(id: int):
    db = {
        1: 'apples',
        2: 'oranges',
        3: 'bananas',
    }
    # simulate the time it takes to fetch data from a remote db
    time.sleep(1)
    data = db[id]
    print(f'{data} fetched successfully!')
    return data


def main():
    for id in range(1, 4):
        fetch_data(id)


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'It took {end - start:.4f}s.')
