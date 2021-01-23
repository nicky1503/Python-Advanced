numbers1 = [[1, 2, 3], [4, 6, 6]]
nums = [1, 2, 3, 4, 5]


def num(x):
    return x % 2 == 0


result = filter(num, nums)
print(list(result))