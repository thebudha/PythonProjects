items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]

# Previous:  prices = list(map(lambda item: item[1], items))

# Syntax:  [expression for item in items]
prices = [item[1] for item in items]

# Previous:  filtered = list(filter(lambda item: item[1] >= 10, items))

filtered = [item for item in items if item[1] >= 10]

print(prices)
print(filtered)