odd_or_even = input()
nums = [int(n) for n in input().split()]
if odd_or_even == "Odd":
    print(sum(list(filter(lambda x: x % 2 == 1, nums)))*len(nums))
else:
    print(sum(list(filter(lambda x: x % 2 == 0, nums))) * len(nums))