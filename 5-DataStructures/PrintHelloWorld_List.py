chars = list("Hello World")
print(chars)
#prints only the characters in reverse order, but does not extract them from the list or join them together to form a string.
print(chars[::-1])
#extracts the characters from the list and joins them together to form a string.
print("".join(chars[::-1]))  # dlroW olleH
print("".join(chars))  # Hello World
print (len(chars))  # 11
