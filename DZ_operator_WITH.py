
file_1 = 'text.txt'
with open(file_1, mode='r', encoding='utf8') as fl:
    for line in fl:
        print(line, end='')
