def f(a, b, *, c, d):
    '''a, b, c, d can be passed as both positional and keyword arguments'''
    print(a, b, c, d)


f(1, 2, c=3, d=4)  # a, b, c, d are positional arguments
