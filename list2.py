#Given a list of numbers, create a new list containing only even numbers using list comprehension.

list1 = [1, 2, 2, 3, 1, 4, 3, 5]
even_list2=[num for num in list1 if num%2==0]
print("list: ", list1)
print("even list : " ,even_list2)

