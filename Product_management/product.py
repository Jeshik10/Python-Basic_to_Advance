class Product:
  def __init__(self,id,  name, quantity, price):
    self.id = id
    self.name = name
    self.qty = quantity
    self.price = price

  def _str_(self):
    print(f"ID : {self.id} , Name : {self.name}, Quanatity : {self.qty}, Price : {self.price}") 

  def display(self):
        print(f"Product ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.qty}")
        print(f"Price: Rs.{self.price:.2f}")
        print() 