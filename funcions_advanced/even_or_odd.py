def even_odd(*args):
    if args[-1] == "even":
        return [n for n in args[:-1] if n % 2 == 0]
    else:
        return [n for n in args[:-1] if n % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
