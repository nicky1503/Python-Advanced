from collections import deque

water_quantity = int(input())
name = input()
names = deque()
while name != "Start":
    names.append(name)
    name = input()
data = input()
while data != "End":
    data = data.split()
    if data[0] == "refill":
        water_quantity += int(data[1])
    elif water_quantity >= int(data[0]):
        water_quantity -= int(data[0])
        print(f"{names.popleft()} got water")
    else:
        print(f"{names.popleft()} must wait")
    data = input()
print(f"{water_quantity} liters left")
