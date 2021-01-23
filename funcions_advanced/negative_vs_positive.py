def valuate_number(numbers):
    positives = []
    negatives = []
    for n in numbers:
        if n > 0:
            positives.append(n)
        else:
            negatives.append(n)
    return negatives, positives


def which_sum_is_bigger(numbers):
    negatives, positives = valuate_number(numbers)
    print(sum(negatives))
    print(sum(positives))
    if abs(sum(negatives)) > sum(positives):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = [int(n) for n in input().split()]
which_sum_is_bigger(nums)
