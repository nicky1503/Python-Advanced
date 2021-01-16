from collections import deque

kids = deque(input().split())
toss = int(input())
toss_counter = 1
while len(kids) > 1:

    if toss != toss_counter:
        next_kid = kids.popleft()
        kids.append(next_kid)
    else:
        print(f"Removed {kids.popleft()}")
        toss_counter = 0
    toss_counter += 1

print(f"Last is {''.join(kids)}t")