array = [7, 5, 3, 3, 2]
rating = int(input('Введите рейтинг: '))


for elem in array:
    if rating > elem:
        array.insert(array.index(elem), rating)
        break
    elif elem == array[-1]:
        array.append(rating)
        break
print(array)

