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
    ids_to_fetch = (1, 2, 3)

    for id in ids_to_fetch:
        fetch_data(id)


if __name__ == '__main__':
    main()
