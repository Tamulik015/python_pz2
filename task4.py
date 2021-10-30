str = input('Введите слова: ')
array = str.split(' ')

for elem in array:
    if len(elem) > 10:
        print(f'{array.index(elem)}', elem[0:4])
    else:
        print(f'{array.index(elem)}', elem)


