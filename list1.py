#Write a program to remove duplicate elements from a list without using set.

arr = [1, 2, 2, 3, 1, 4, 3, 5]
unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

print("Original:", arr)
print("Without duplicates:", unique)
