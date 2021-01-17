ns = input().split()
set_1 = {input() for _ in range(int(ns[0]))}
set_2 = {input() for _ in range(int(ns[1]))}
both = set_1.intersection(set_2)
[print(n) for n in both]
