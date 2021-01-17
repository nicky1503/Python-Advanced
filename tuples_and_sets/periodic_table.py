n = int(input())
compounds = set()
for _ in range(n):
    data = input().split()
    for c in data:
        compounds.add(c)
[print(c) for c in compounds]