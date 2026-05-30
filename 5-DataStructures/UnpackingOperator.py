# numbers = [1, 2, 3]
# print(*numbers)
# print(1,2,3)

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# # Using the unpacking operator to take out values
# # in any iterable:
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
