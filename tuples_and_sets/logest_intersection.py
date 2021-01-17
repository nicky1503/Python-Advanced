n = int(input())
longest_intersection = []
range_1 = set()
range_2 = set()
for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = first.split(',')
    second_start, second_end = second.split(',')
    for n in range(int(first_start), int(first_end) + 1):
        range_1.add(n)
    for n in range(int(second_start), int(second_end)+1):
        range_2.add(n)
    intersection = range_1.intersection(range_2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = [n for n in intersection]
    range_1.clear()
    range_2.clear()
print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")


