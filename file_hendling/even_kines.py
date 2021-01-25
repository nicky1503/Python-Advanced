def reverse_lines(text):
    reverse = []
    for line in text:
        line = line.split()
        line = line[::-1]
        reverse.append(' '.join([l for l in line]))
    return reverse


with open("files/text.txt") as file:
    text = file.readlines()
    text = [text[t] for t in range(len(text)) if t % 2 == 0]

reversed_lines = reverse_lines(text)
for line in range(len(reversed_lines)):
    for symbol in range(len(reversed_lines[line])):
        if reversed_lines[line][symbol] in ["-", ",", ".", "!", "?"]:
            line_as_list = list(reversed_lines[line])
            line_as_list[symbol] = "@"
            reversed_lines[line] = "".join(line_as_list)
for line in reversed_lines:
    print(line)


