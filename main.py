with open('text.txt', 'r') as origin_file:
    origin_data = [line.strip() for line in origin_file.readlines()]

with open('out.txt', 'r') as overwrite_file:
    overwrite_data = [line.strip() for line in overwrite_file.readlines()]

origin_diff = []

for line in origin_data:
    if line not in overwrite_data:
        origin_diff.append(line)

print("нема'text.txt',  у 'out.txt':")
for line in origin_diff:
    print(line)