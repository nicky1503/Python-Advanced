from collections import deque

green_light_time = int(input())
free_window = int(input())

cars = input()
time_left = green_light_time
window = free_window
cars_waiting = deque()
cars_waiting.append(cars)
crash = False
car_count = 0
while cars_waiting:
    if cars == "END":
        break
    current_car = cars_waiting.popleft()
    if current_car != "green" and time_left > 0:
        for char in current_car:
            time_left -= 1
            if time_left < 0:
                window -= 1
                if window < 0:
                    crash = True
                    print("A crash happened!")
                    print(f"{current_car} was hit at {char}.")
                    break
        car_count += 1
    if crash:
        break
    elif current_car == "green":
        time_left = green_light_time
        window = free_window
    cars = input()
    cars_waiting.append(cars)
if not crash:
    print("Everyone is safe.")
    print(f"{car_count} total cars passed the crossroads.")