from product import Product

tota_prod = int(input("How many product data you want to insert: "))

lists = []
for i in range(tota_prod):
  id = input(f"Enter product {i+1} id: ")
  name = input(f"Enter product {i+1} name: ")
  quantity = input(f"Enter product {i+1} quantity: ")
  price = input(f"Enter product {i+1} price: ")
  s = Product(id, name, quantity, price)
  ## Save to File
  f = open("product.csv", "a")
  f.write(f"{s.id},{s.name},{s.qty},{s.price}\n")
  f.close()
