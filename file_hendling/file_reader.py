file = open("files\\File Reader\\numbers.txt")
sum = 0
for line in file:
    sum += int(line.strip())
print(sum)
