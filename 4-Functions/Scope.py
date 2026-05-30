message = "a"

def greet(name):
    global message
    message = "b"


greet("TheDudeman")
print(message)

