n = int(input())
names = []
for _ in range(n):
    data = input()
    names.append(data)
names = set(names)
for name in names:
    print(name)