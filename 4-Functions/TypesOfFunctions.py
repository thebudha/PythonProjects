# def greet(first_name, last_name):
def get_greeting(name):
    """Return a greeting message for the given name."""
    return f"Hi {name}"


message = get_greeting("Mosh")
with open("content.txt", "w", encoding="utf-8") as file:
    file.write(message)
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Thomas", "Johnson")
# There are 2 types of functions:
# 1- Functions that perform a task
# 2- Functions that return a value

