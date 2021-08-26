import os
products = []
if os.path.isfile('products.csv'): 
	print('Nice! we found the file.')
	with open('products.csv', 'r', encoding = 'utf-8') as f: 
		for l in products:
			if 'product, price' in line: 
				name, price = line.strip().line.split()
				products.append([name, price])
	print(products)
else: 
	print('Oh No, We failed to find the file')
while True: 
	name = input('Please enter the name of the product: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	products.append([name, price])
print(products)
for p in products:
	print('The price of', p[0], ' is', p[1])
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')