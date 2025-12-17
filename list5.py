#Demonstrate shallow copy and deep copy of a list with mutable elements.

# Shallow vs Deep copy demonstration

import copy

original = [[1, 2], [3, 4], [5, 6]]
print("Original:", original)

shallow = original.copy()
deep = copy.deepcopy(original)

original[0][0] = 999

print("\nAfter modifying original[0][0] = 999:")
print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)

original[1] = ['replaced']

print("\nAfter replacing original[1] = ['replaced']:")
print("Original:", original)
print("Shallow:", shallow)
