with open('text.txt', 'r') as file:
    content = file.read()

new_content = ""

for char in content:
    if char == '*':
        new_content += '&'
    else:
        new_content += char

with open('text.txt', 'w') as file:
    file.write(new_content)

print("символи '*' замінено на '&'.")

with open('symbol.txt', 'w') as overwrite:
    content = overwrite.write(new_content)