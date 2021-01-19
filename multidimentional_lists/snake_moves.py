from collections import deque

n = [int(c) for c in input().split()]
text = input()
snake = deque([x for x in text*(n[0]*n[1])])
reverse_output = ""
reverse = False
for row in range(n[0]):
    if not reverse:
        print("".join([snake.popleft() for x in range(n[1])]))
        reverse = True
    else:
        reverse_output = [snake.popleft() for x in range(n[1])]
        reverse_output = "".join(reverse_output)
        print(reverse_output[::-1])
        reverse = False