from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


p1 = Point(x=1, y=2)
# p1 = Point(x=10, y = 2)
p2 = Point(1, 2)    
print(p1 == p2)  # True
# print(id(p1), id(p2))  # Different memory addresses