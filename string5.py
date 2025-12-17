
s = "hello"
print("Original string:", s)

try:
    s[0] = 'H'
except TypeError as e:
    print("\nError caught:")
    print(e)
    print("\nExplanation: In Python, strings are immutable. "
          "You cannot change them in place using indexing.")

new_s = 'H' + s[1:]
print("\nNew string (after change):", new_s)

chars = list(s)
chars[0] = 'H'
s_modified = "".join(chars)
print("Modified via list conversion:", s_modified)
