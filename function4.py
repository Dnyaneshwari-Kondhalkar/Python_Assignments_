
def average(*args):
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    return total / count if count > 0 else 0

print(average(1,2,3,4,5,6,7,8,9))
