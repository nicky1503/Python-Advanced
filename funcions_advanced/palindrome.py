def palindrome(string, index):
    if len(string) == index:
        return f"{string} is a palindrome"
    elif string[index] != string[-(index+1)]:
        return f"{string} is not a palindrome"
    else:
        return palindrome(string, index+1)


print(palindrome("abcaacba", 0))
print(palindrome("peter", 0))
