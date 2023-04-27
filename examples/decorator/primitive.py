import timeit

def loop_test():
    i = 0
    while i < 10_000_000:
        i += 1

def main():
    start_time = timeit.default_timer()

    loop_test()

    end_time = timeit.default_timer()
    time_difference = end_time - start_time
    print(f"{loop_test.__name__} took {time_difference} seconds")


if __name__ == '__main__':
    main()
