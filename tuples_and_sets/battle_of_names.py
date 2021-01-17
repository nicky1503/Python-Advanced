lines = int(input())
even = set()
odd = set()
sum_of_chars = 0
all_elements = set()
for line in range(lines):
    names = input()
    for char in names:
        sum_of_chars += ord(char)
    sum_of_chars = sum_of_chars // (line + 1)
    if sum_of_chars % 2 == 0:
        even.add(sum_of_chars)
    else:
        odd.add(sum_of_chars)
    sum_of_chars = 0

if sum(odd) == sum(even):
    print(', '.join([str(n) for n in odd.union(even)]))
elif sum(even) > sum(odd):
    print(', '.join([str(n) for n in odd.symmetric_difference(even)]))
elif sum(odd) > sum(even):
    print(', '.join([str(n) for n in odd]))