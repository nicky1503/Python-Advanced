start = int(input())
end = int(input())
check_ins = [n for n in range(2, 10+1)]
nums_to_check = [el for el in range(start, end+1)]
nums = []
for num in nums_to_check:
    for c in check_ins:
        if num % c == 0 and num not in nums:
            nums.append(num)
print(nums)