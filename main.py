with open('text.txt') as file:
    content = file.read()

new_text = []
word_count = 0

for word in content.split():
    if len(word) > 6:
        word_count += 1
        new_text.append(f"{word_count}: {word}")

with open('out.txt', 'w') as output_file:
    output_file.write("\n".join(new_text))