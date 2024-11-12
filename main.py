with open('text.txt', 'r') as file:
    content = file.readlines()

reversed_content = content[::-1]

with open('out.txt', 'w') as output_file:
    output_file.writelines(reversed_content)