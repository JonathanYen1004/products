products = []
while True:
	name = input('please enter the products : ') 
	if name == 'q':
		break
	price = input('please enetr the prices of the products: ')
	products.append([name , price])
print(products)

for p in products:
	print(p[0] , 'price is' , p[1] )