from collections import deque

n = int(input())
result = deque()
current_fuel = 0
for _ in range(n):
    given_lites, needed_liters = input().split()
    result.append(int(given_lites)-int(needed_liters))
for i in range(len(result)):
    for pump in result:
        current_fuel += pump
        if current_fuel < 0:
            break
    result.append(result.popleft())
    if current_fuel >= 0:
        print(i)
        break
    current_fuel = 0

