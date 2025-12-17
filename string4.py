#Write a program to find the frequency of each character in a string.
string1=input("enter string : ")
frequency={}
for char in string1:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

print(frequency)
