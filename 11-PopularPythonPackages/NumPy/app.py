import numpy as np

# # Create a 2D array, otherwise known as a matrix
# array = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
# print(array)
# print(type(array))

# array = np.zeros((3, 4), dtype=int)
# array = np.ones((3, 4), dtype=int)
# array = np.full((3, 4), 5, dtype=int)
# array = np.random.random((3, 4))
# print(array)
# print(array[0, 0]) # Access the first element
# print(array > 0.2) # Create a boolean array where the condition is true
# print(array[array > 0.2]) # Get the elements that satisfy the condition
# print(np.sum(array)) # Sum of all elements
# print(np.round(array)) # Round the elements to the nearest integer

# first = np.array([1, 2, 3])
# second = np.array([4, 5, 6])
# print(first + second) # Element-wise addition

dimensions_inch = np.array([10, 20, 30])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
