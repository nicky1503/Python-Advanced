import re


def count_words(words_in_text, words):
    result = {}
    for word in words:
        for word_in_text in range(len(words_in_text)):
            for word_text in range(len(words_in_text[word_in_text])):
                if word == words_in_text[word_in_text][word_text].lower():
                    if words_in_text[word_in_text][word_text].lower() not in result:
                        result[word] = 1
                    else:
                        result[word] += 1
    return result


pattern = r"([a-zA-z]+)"
with open("./files/Words Count/words.txt") as file_1:
    words = file_1.readline().split()

words_in_text = []
with open("./files/Words Count/text.txt") as file_2:
    while True:
        text = file_2.readline()
        if not text:
            break
        words_in_text.append(re.findall(pattern, text))
words_count = count_words(words_in_text, words)
words_count = dict(sorted(words_count.items(), key=lambda item: -item[1]))

with open("./files/Words Count/result.txt", "a") as result_file:
    for key, value in words_count.items():
        result_file.write(f"{key} - {value}\n")
