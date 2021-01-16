clothes = [int(n) for n in input().split()]
rack_size = int(input())
rack_count = 0
clothes_on_rack = 0
while clothes and rack_size > 0:
    current_clothe = clothes.pop()
    clothes_on_rack += current_clothe
    if clothes_on_rack == rack_size:
        rack_count += 1
        clothes_on_rack = 0
    elif clothes_on_rack > rack_size:
        rack_count += 1
        clothes.append(current_clothe)
        clothes_on_rack = 0
    elif not clothes and clothes_on_rack > 0:
        rack_count += 1
print(rack_count)
