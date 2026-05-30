items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]

#This function is replaced by a lambda
# def sort_item(item):
#     return item[1]

#Lambda syntax: item.sort(key=lambda parameter: expression)

items.sort(key=lambda item: item[1])
print(items)