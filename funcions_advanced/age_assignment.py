def age_assignment(*args, **kwargs):
    result = {}
    for names in args:
        result[names] = kwargs[names[0]]
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
