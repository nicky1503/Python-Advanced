# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     number = int(input())
#     numbers_dictionary[number_as_string] = number
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     print(numbers_dictionary[searched])
#
# line = input()
#
# while line != "End":
#     searched = line
#     del numbers_dictionary[searched]
#
# print(numbers_dictionary)


def write_in_dict():
    result = {}
    line = input()
    while line != "Search":
        number_as_string = line
        number = int(input())
        result[number_as_string] = number
        line = input()
    return result


def search_a_pair(dict_nums):
    line = input()
    while line != "Remove":
        searched = line
        print(dict_nums[searched])
        line = input()


def remove_from_dict(dict_nums):
    line = input()
    while line != "End":
        searched = line
        del dict_nums[searched]
        line = input()
    return dict_nums


numbers_dictionary = {}
try:
    numbers_dictionary = write_in_dict()
    search_a_pair(numbers_dictionary)
    numbers_dictionary = remove_from_dict(numbers_dictionary)
except KeyError:
    print("Number does not exist in dictionary")
except ValueError:
    print("The variable number must be an integer")
finally:
    print(numbers_dictionary)



