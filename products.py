import os #operating system


#read file
products = []
if os.path.isfile('products.csv'):
	print('yes')
	with open('products.csv' , 'r' , encoding='utf-8') as f:
		for line in f:
			if 'products , price' in line:
			    continue
		name, price = line.strip().split(',')
		products.append([name, price])
		print(products)
else:  
	print('not found')

#let user enter
while True:
	name = input('please enter the products : ') 
	if name == 'q':
		break
	price = input('please enetr the prices of the products: ')
	price = int(price)
	products.append([name , price])
print(products)

#print records
for p in products:
	print(p[0] , 'price is' , p[1] ) 

#write file
with open('products.csv' , 'w' , encoding='utf-8') as f:
	f.write('products , price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  