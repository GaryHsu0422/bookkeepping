products = []
while True: 
	name = input('Please enter the name of the product: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	products.append([name, price])
print(products)

for p in products:
	print('The price of', p[0], ' is', p[1])
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
