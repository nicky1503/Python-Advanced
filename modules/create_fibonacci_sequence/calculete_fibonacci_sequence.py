def calculate_sequence(num):
    n1, n2 = 0, 1
    count = 0
    result = []
    while count < num:
        result.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return result
