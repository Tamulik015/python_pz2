cart_products = int(input('Сколько всего нужно товара: '))
list_products = []
num = 1

while num <= cart_products:
    name_product = input('Введите название продукта: ')
    price_product = input('Введите цену: ')
    quantity_product = input('Введите количество: ')

    dict = {'название': name_product, 'цена': price_product, 'количество': quantity_product, 'ед': 'шт'}
    tuple = (num, dict)

    list_products.append(tuple)
    num += 1
print(list_products)

