from modules.triangle.line import print_line


def print_triangle(num):
    for growing_side in range(1, num+1):
        print_line(1, growing_side)
    for falling_side in range(num-1, 0, -1):
        print_line(1, falling_side)

