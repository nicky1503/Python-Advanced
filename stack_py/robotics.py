import datetime
from collections import deque

robots = deque(input().split(';'))
precess_time = [int(t) for t in input().split(':')]
goods = input()
seconds = precess_time[0]*3600 + precess_time[1]*60 + precess_time[2]
products_waiting = deque()
products_waiting.append(goods)
taken_robots = deque()
work_time = 0
while products_waiting:
    seconds += 1
    work_time += 1
    time = str(datetime.timedelta(seconds=seconds))
    if robots:
        current_robot = robots.popleft()

        print(f"{current_robot} {products_waiting.popleft()} {time}")
        taken_robots.append(current_robot)

    for robot in taken_robots:
        robot_time = int(robot.split('-')[1])
        if (work_time) % robot_time == 0:

            robots.append(robot)
    if goods != 'End':
        goods = input()
        products_waiting.append(goods)
    if goods == "End" and len(products_waiting) == 1:

        break