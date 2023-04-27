import time


def loop_test_1():
    i = 0
    while i < 10_000_000:
        i += 1


def loop_test_2():
    i = 0
    while i < 15_000_000:
        i += 1


def main():
    start = time.perf_counter()
    loop_test_1()
    end = time.perf_counter()
    print(f"{loop_test_1.__name__} took {end - start} seconds")

    start = time.perf_counter()
    loop_test_2()
    end = time.perf_counter()
    print(f"{loop_test_2.__name__} took {end - start} seconds")


if __name__ == '__main__':
    main()
