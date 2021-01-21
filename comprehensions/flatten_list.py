nums = [[n for n in row.split()]for row in input().split('|')]
nums = nums[::-1]
print(" ".join([(' '.join(nums[i])) for i in range(len(nums))]))
