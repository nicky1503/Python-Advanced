data = input().split()
counted_values = []
for num in data:
    if num not in counted_values:
        counted_values.append(num)
        print(f"{float(num)} - {data.count(num)} times")