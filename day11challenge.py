## Write a python program to create a class Laptop with properties [id, name, ram] and create 3 objects of it and print all details.

class Laptop:
  def __init__(self, id, name , ram):
    self.id = id
    self.name = name 
    self.ram = ram

  def display(self):
    print(f"Id : {self.id}\t Name : {self.name}\t RAM : {self.ram}")  

## objects
obj1 = Laptop('1', "Mac M1 chip", '512 gb')    
obj2 = Laptop('2', "Lenovo", '256 gb')    
obj3 = Laptop('2', "Vivo", '256 gb')    

obj1.display()
obj2.display()
obj3.display()