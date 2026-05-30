# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(sorted(numbers, reverse=True))
# print(numbers)

items = [
    ("Product 1", 10),
    ("Product 1", 9),
    ("Product 1", 12),
]

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
