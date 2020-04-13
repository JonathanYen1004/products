products = []
while True:
	name = input('please enter the products : ') 
	if name == 'q':
		break
	price = input('please enetr the prices of the products: ')
	price = int(price)
	products.append([name , price])
print(products)

for p in products:
	print(p[0] , 'price is' , p[1] ) 

with open('products.csv' , 'w' , encoding='utf-8') as f:
	f.write('products , price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  