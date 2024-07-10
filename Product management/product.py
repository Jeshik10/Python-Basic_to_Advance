class Product:
  def __init__(self,id,  name, quantity, price):
    self.id = id
    self.name = name
    self.qty = quantity
    self.price = price

  def display(self):
    print(f"ID : {self.id} , Name : {self.name}, Quanatity : {self.qty}, Price : {self.price}") 
