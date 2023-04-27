import time


def time_function(func):
    def wrapper():
        start = time.perf_counter()

        func()

        end = time.perf_counter()
        print(f"{func.__name__} took {end - start} seconds")

    return wrapper


def loop_test_1():
    i = 0
    while i < 10_000_000:
        i += 1


loop_test_1 = time_function(loop_test_1)


def loop_test_2():
    i = 0
    while i < 15_000_000:
        i += 1


loop_test_2 = time_function(loop_test_2)


def main():
    loop_test_1()
    loop_test_2()


if __name__ == '__main__':
    main()
