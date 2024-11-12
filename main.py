with open('text.txt', 'w') as file:
    file.write("Message")

with open('text2.txt', 'r') as file:
    content = file.read()

read = content.split()
count_words = 0

for i in read:
    count_words += 1

print(count_words)