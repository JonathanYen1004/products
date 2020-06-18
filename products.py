import os #operating system

def read_file(filename):
    products = []
    with open(filename , 'r' , encoding='utf-8') as f:
        for line in f:
            if 'products , price' in line:  
  			        continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

#let user enter
def user_input(products):
    while True:
	    name = input('please enter the products: ') 
	    if name == 'q':
		    break
	    price = input('please enetr the prices of the products: ')
	    price = int(price)
	    products.append([name , price])
    print(products)
    return products

# print products
def print_products(products):
    for p in products:
	    print(p[0] , 'price is' , p[1] ) 

#write file
def write_file(filename , products):
    with open('products.csv' , 'w' , encoding='utf-8') as f:
	    f.write('products , price\n')
	    for p in products:
		    f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
	    print('yes')
	    products = read_file(filename)
    else:
	    print('not found')

    products = user_input(products)
    print_products(products)
    write_file('products.csv ' , products)


main()
