from unicodedata import digit

with open('text.txt', 'r') as f:
    origin = f.read()

_char = 0
for char in origin:
    _char += 1

_line = 0
for line in origin.splitlines():
    _line += 1

vowel_letters = 0
consonant_letters = 0
for i in origin:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel_letters += 1
    else:
        consonant_letters += 1

digit = 0
for i in origin:
    if i.isdigit():
        digit += 1


print(f"Number of characters: {_char}")
print(f"Number of lines: {_line}")
print(f"Number of vowel letters: {vowel_letters}")
print(f"Number of consonant letters: {consonant_letters}")
print(f"Number of digits: {digit}")