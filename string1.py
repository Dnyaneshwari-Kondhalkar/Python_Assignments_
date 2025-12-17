#Write a program to count the number of vowels, consonants, digits, and special characters in a given string.



text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
digit_count = 0
special_char_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_char_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("length:", len(text))
print("Special Characters:", special_char_count)

