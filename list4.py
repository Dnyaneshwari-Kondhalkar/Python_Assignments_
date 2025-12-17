#Create a nested list and calculate the sum of each inner list.

nested = [[1, 2, 3], [10, -5, 5], [4], [], [100, 200]]

sums = []
for inner in nested:
    total = 0
    for x in inner:
        total += x
    sums.append(total)

print("Nested list:", nested)
print("Sum of each inner list:", sums)
