def is_even(n):
    return int(n) % 2 == 0

print(list(map(int, filter(is_even, input().split()))))