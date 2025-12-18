def common_elements(list1, list2):
    common = []
    for item in list1:
        for element in list2:
            if item == element and item not in common:
                common.append(item)
    return common

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
