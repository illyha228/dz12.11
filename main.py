with open('text.txt', 'r') as f:
    origin = f.read()

count = 0
for char in origin:
    count += 1

print(count)