n = int(input())
stack = []
if 1 <= n <= 105:
    for _ in range(n):
        commands = input()
        commands = commands.split()
        if 1 <= int(commands[0]) <= 4:
            if int(commands[0]) == 1 and 1 <= int(commands[0]) <= 109:
                stack.append(int(commands[1]))
            elif int(commands[0]) == 2 and stack:
                stack.pop()
            elif int(commands[0]) == 3 and stack:
                print(max(stack))
            elif int(commands[0]) == 4 and stack:
                print(min(stack))

stack = [str(n) for n in stack]
stack = reversed(stack)
result = ", ".join(stack)
print(result)

