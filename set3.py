
a = {1, 2}
b = {1, 2, 3, 4}
is_subset = True
for x in a:
    if x not in b:
        is_subset = False
        break
print(is_subset)
