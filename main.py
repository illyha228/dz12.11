with open('text.txt ', 'r') as file:
    lines = file.readlines()

last_line = lines[-1]

with open('line.txt', 'w') as file:
    file.writelines(lines[:-1])