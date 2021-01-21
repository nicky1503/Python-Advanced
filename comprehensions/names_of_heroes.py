names = input().split(", ")
items = input().split("-")
inventory = {key: {} for key in names}
while items[0] != "End":
    name, item, price = items[0], items[1], items[2]
    if item not in inventory[name]:
        inventory[name][item] = int(price)
    items = input().split('-')
[print(f"{key} -> Items: {len(value)}, Cost: {sum(value.values())}") for key, value in inventory.items()]

