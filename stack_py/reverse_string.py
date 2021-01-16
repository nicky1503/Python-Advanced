data = input()
text = []
result = ""
for ch in data:
    text.append(ch)
while text:
    result += text.pop()
print(result)