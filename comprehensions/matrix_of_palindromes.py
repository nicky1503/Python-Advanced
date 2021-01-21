n = [int(num) for num in input().split()]
matrix = [[f"{chr(97 + row)}{chr(97+el + row)}{chr(97 + row)}" for el in range(n[1])] for row in range(n[0])]
[print(" ".join(row)) for row in matrix]