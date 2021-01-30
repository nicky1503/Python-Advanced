# try:
#     line = input()
#     times = int(input())
#     print(line * times)
# except ValueError:
#     print("Variable times must be an integer")


def read_input():
    line = input()
    times = int(input())
    return times, line


def solve():
    try:
        times, line = read_input()
    except ValueError:
        return "Variable times must be an integer"
    return line * times


print(solve())