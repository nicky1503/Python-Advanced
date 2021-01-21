data = input().split(", ")
all_nums = []
all_nums.append([int(n) for n in data if int(n) >= 0])
all_nums.append([int(n) for n in data if int(n) < 0])
all_nums.append([int(n) for n in data if int(n) % 2 == 0])
all_nums.append([int(n) for n in data if int(n) % 2 == 1])
values = ["Positive", "Negative", "Even", "Odd"]
values_to_nums = {key: value for key, value in zip(values, all_nums)}
[print(f"{key}: {', '.join([str(n) for n in value])}") for key, value in values_to_nums.items()]
