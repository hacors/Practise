from functools import reduce
a = [1, 2, 3, 4, 5, 6]


def add_temp(a, b, c):
    d = a+b
    e = b+c
    return d, e


b = reduce(add_temp, list(a))
print(b)
