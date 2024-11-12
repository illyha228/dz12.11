a = input("Введіть: ")

with open('text.txt', 'r') as file:
    content = file.read()

words = content.split()
count = 0

for word in words:
    if word.startswith(a):
        count += 1

print(count)