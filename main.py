with open('text.txt') as file:
    content = file.read()

with open('out.txt', 'w') as output_file:
    output_file.writelines(content)