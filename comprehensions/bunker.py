item_category = input().split(", ")
n = int(input())
storage = {item_category[i]: {} for i in range(len(item_category))}
quantity = 0
avg_quality = 0
for i in range(n):
    category, item, stats = input().split(" - ")
    storage[category][item] = stats
    quantity_quality = stats.split(";")
    quantity_num = quantity_quality[0].split(':')
    quality_num = quantity_quality[1].split(':')
    quantity += int(quantity_num[1])
    avg_quality += int(quality_num[1])
print(f"Count of items: {quantity}")
print(f"Average quality: {avg_quality/len(item_category):.2f}")
[print(f"{key} -> {', '.join(value.keys())}")for key, value in storage.items()]

