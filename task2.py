array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_for_iterations = int(len(array) / 2)
items = []
num1 = 0
num2 = 2

while number_for_iterations > 0:
    res = array[num1:num2]
    res.reverse()
    items.extend(res)
    num1 += 2
    num2 += 2
    number_for_iterations -= 1
print(items)

