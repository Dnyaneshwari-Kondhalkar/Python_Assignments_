def is_palindrome(num):
    original = str(num)
    reversed_num = ""
    for ch in original:
        reversed_num = ch + reversed_num
    return original == reversed_num

print(is_palindrome(121))
print(is_palindrome(123))
