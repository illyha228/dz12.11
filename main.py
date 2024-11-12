search = input('Введіть: ')
overwritten = input('Введіть ')

with open('text.txt', 'r') as file:
    text = file.read()

updated_text = text.replace(search, overwritten)

print(updated_text)

with open('out.txt', 'w') as file:
    file.write(updated_text)es[:-1])