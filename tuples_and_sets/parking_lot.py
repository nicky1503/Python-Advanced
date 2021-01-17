n = int(input())
cars_in_parking_lot = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars_in_parking_lot.add(car_number)
    else:
        cars_in_parking_lot.remove(car_number)
if cars_in_parking_lot:
    [print(c) for c in cars_in_parking_lot]
else:
    print("Parking Lot is Empty")