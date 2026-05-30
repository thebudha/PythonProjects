letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")

#print chars in reverse order, 
# extract the characters from the list,
# and join them together to form a string.
print("".join(chars[::-1]))

print(f"{(combined)}\n\n")
print(f"{numbers}\n\n")
print(chars)
print(numbers[::-1])
print(list(reversed(chars)))
#prints only the characters in reverse order, but does not extract them from the list or join them together to form a string.
print(chars[::-1])
print("".join(chars[::-1]))  # dlroW olleH