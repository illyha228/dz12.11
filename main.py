lines = [
    "Test1",
    "Test2"
]


file_path = 'out2.txt'

with open(file_path, 'w') as file:
    for line in lines:
        file.write(line + '\n')

#ну я 8 сначала не поняв але так як я поняв по такій суті і 8 робеться