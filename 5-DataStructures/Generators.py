from sys import getsizeof

# Generator
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
