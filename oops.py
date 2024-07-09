## Create Class

class Teacher:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary
    
  def display(self):
    print(f"Name is {self.name}")  
    print(f"Age is {self.age}")
    print(f"Salary is {self.salary}")

## Create Object
tch1 = Teacher("jeshik", 24, 5000)
tch1.display()

tch2 = Teacher("binita", 23, 6000)
tch2.display()