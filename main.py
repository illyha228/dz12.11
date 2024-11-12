with open('text.txt', 'r') as file:
    content = file.readlines()

insert_index = len(content)
for i in range(len(content) - 1, -1, -1):
    if ',' not in content[i]:
        insert_index = i + 1
        break

content.insert(insert_index, '************\n')

with open('pass.txt', 'w') as output_file:
    output_file.writelines(content)ed_content)