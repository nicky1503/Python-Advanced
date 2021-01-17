data = input()
chars = {}
for char in data:
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1

sorted_chars = sorted(chars.keys())
[print(f"{char}: {chars[char]} time/s") for char in sorted_chars]