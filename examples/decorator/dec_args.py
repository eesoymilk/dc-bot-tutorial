def print_args_kwargs_decorator(func):
    def wrapper(*args, **kwargs):
        print(
            f'Function {func.__name__} called with\n' +
            f'arguments: {args} and\n' +
            f'keyword arguments: {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@print_args_kwargs_decorator
def sum_three_num(a, b, c=0):
    return a + b + c


def main():
    print(f'Result: {sum_three_num(1, 2, c=3)}')


if __name__ == '__main__':
    main()
