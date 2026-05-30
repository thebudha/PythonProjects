numbers = list(range(20))
#Prints the numbers from 0 to 19
print(numbers)
#Prints the numbers in reverse order
print(numbers[::-1])

#Prints Hello World in a list of characters
chars = list("Hello World")
print(chars)
#Prints Hello World in reverse order
print("".join(chars[::-1]))

for char in chars:
    print(char)

print(chars[::-1])