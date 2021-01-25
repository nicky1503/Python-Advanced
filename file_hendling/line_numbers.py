with open("files/text.txt") as file:
    result = []
    for inx, line in enumerate(file):
        letter_count = [l for l in line if l.isalpha()]
        punctuation_marks_count = [m for m in line if m in "{-,.!?'"]
        result.append(f"Line {inx+1}: {line.strip()} ({len(letter_count)})({len(punctuation_marks_count)})")
        

with open("files/output.txt", "w") as output_file:
    for line in result:
        output_file.write(line+"\n")