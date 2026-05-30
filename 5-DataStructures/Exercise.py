from collections import Counter

# Find the most repeated character in the text
def most_frequent_char(sentence):
    char_count = Counter(sentence)
    most_common_char, count = char_count.most_common(1)[0]
    return most_common_char, count

sentence = "This is a common interiew question"
most_common_char, count = most_frequent_char(sentence)
print(f"The most frequent character in '{sentence}' is '{most_common_char}' with a count of '{count}'")
