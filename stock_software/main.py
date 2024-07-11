from product import Product

option_text = """
what to u want to do[1-2]?
1. ADD product
2. View All Products
"""
option = int(input(option_text))
if option == 1:
  p = Product(id=0, name = "", qty=0, price=0)
  p.id = int(input(f"Enter product  id: "))
  p.name = input(f"Enter product  name: ")
  p.qty = int(input(f"Enter product  qty: "))
  p.price = float(input(f"Enter product  price: "))
  f = open('product.csv', 'a')
  f.write(f"{p.id},{p.name},{p.qty},{p.price}\n")
  f.close()
  print("Task Completed")  

elif option == 2:
  f = open("product.csv", 'r')
  print("All Products are:\n------------------")
  print(f.read())
  print("-------------")


