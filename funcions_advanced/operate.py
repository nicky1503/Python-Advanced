def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        result = 0
        for n in args:
            result -= n
        return result
    elif operator == "*":
        result = 1
        for n in args:
            result *= n
        return result
    elif operator == "/":
        result = 1
        for n in args:
            result /= n
        return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
