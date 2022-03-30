goods = []
while True:
    name = input('Input name of product or stop to exit \n')
    if name == 'stop':
        break
    product = {'name': name}
    product['price'] = input(f'Input price of {name} \n')
    product['quantity'] = input(f'Input quanntity of {name} \n')
    product['units'] = input(f'Input units of {name} \n')
    goods.append((len(goods) + 1, product))
name_set = set()
price_set = set()
quantity_set = set()
units_set = set()
for item in goods:
    name_set.add(item[1]['name'])
    price_set.add(item[1]['price'])
    quantity_set.add(item[1]['quantity'])
    units_set.add(item[1]['units'])
goods_dict = {
    'name': name_set,
    'price': price_set,
    'quantity': quantity_set,
    'units': units_set
}
print(goods_dict)
