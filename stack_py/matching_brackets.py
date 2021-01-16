data = input()
result = []
stack = []
for index in range(len(data)):
    if data[index] == "(":
        stack.append(index)
    elif data[index] == ")":
        end_expression = stack.pop()
        result.append(data[end_expression:index+1])
for r in result:
    print(r)
