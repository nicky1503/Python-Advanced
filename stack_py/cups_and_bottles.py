from collections import deque

cups_capacity = [int(n) for n in input().split()]
cups_capacity = deque(cups_capacity)
filled_bottles = [int(n) for n in input().split()]
filled_bottles = deque(filled_bottles)
wasted_water = 0
no_more_cups = False
no_more_bottles = False
while True:
    if not cups_capacity:
        no_more_cups = True
        break
    if not filled_bottles:
        no_more_bottles = True
        break
    cup = cups_capacity.popleft()
    bottle = filled_bottles.pop()
    result = bottle - cup
    if result >= 0:
        wasted_water += result
    while result < 0:
        bottle = filled_bottles.pop()
        result += bottle
        if result > 0:
            wasted_water += result
result_bottles = [str(n) for n in filled_bottles]
result_bottles = reversed(result_bottles)
result_bottles = " ".join(result_bottles)
if no_more_cups:
    print(f"Bottles: {result_bottles}")
    print(f"Wasted litters of water: {wasted_water}")
if no_more_bottles:
    print(f"Cups: {' '.join([str(n) for n in cups_capacity])}")
    print(f"Wasted litters of water: {wasted_water}")