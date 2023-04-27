import timeit

def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()

        func(*args, **kwargs)

        end_time = timeit.default_timer()
        time_difference = end_time - start_time
        print(f"{func.__name__} took {time_difference} seconds")

    return wrapper

@time_function
def loop_test():
    i = 0
    while i < 100_000_000:
        i += 1

def main():
    loop_test()


if __name__ == '__main__':
    main()
