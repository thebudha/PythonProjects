# number = 100
# while number > 0:
#     print(number)
#     number //= 2

command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
