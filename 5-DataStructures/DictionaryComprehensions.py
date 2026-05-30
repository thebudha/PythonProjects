# Whenever we have this pattern in our code
# we can use a dictionary comprehension
# values = []
# for x in range(5):
#     values. append(x * 2)
# print(values)

values = {x: x * 2 for x in range(5)}
print(values)
