from collections import deque

food_quantity = int(input())
orders = deque(input().split())
people_serviced = deque()
orders_left = []
biggest_order = 0
success = True
orders = [int(n) for n in orders]
orders = deque(orders)
print(max(orders))
while orders:
    order = orders.popleft()
    if food_quantity >= order:
        if order > biggest_order:
            biggest_order = order
        food_quantity -= order
    elif food_quantity < order:
        orders.appendleft(order)
        success = False
        break
if success:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(n) for n in orders])}")
