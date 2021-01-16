expression = input()
stack = []
opening_brackets = []
balances = True
for bracket in expression:
    if len(expression) % 2 == 1:
        balances = False
        print("NO")
        break
    if bracket == "[" or bracket == "{" or bracket == "(":
        opening_brackets.append(bracket)
    else:
        if opening_brackets:
            if ord(bracket) == 93 and ord(opening_brackets[-1]) == 91:
                opening_brackets.pop()
            elif ord(bracket) == 125 and ord(opening_brackets[-1]) == 123:
                opening_brackets.pop()
            elif ord(bracket) == 41 and ord(opening_brackets[-1]) == 40:
                opening_brackets.pop()
            else:
                print('NO')
                balances = False
                break
        else:
            balances = False
            print("NO")
if balances and len(opening_brackets) == 0:
    print("YES")