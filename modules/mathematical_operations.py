from modules.math_operations import calculate

eq = input().split()
print(f"{calculate(float(eq[0]), float(eq[2]), eq[1]):.2f}")