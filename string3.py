#Check whether a given string is a palindrome using indexing and slicing
pal=input("enter string : ")
print(pal)
reverse=pal[::-1]
if(reverse==pal):
    print("string is palindrome")
else:
    print("string is not palindrome")



