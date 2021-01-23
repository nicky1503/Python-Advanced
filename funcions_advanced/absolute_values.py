def round_num(x):
    return round(x)


print(list(map(round_num, map(float, input().split()))))