## Write a python program to create a class Laptop with properties [id, name, ram] and create 3 objects of it and print all details.


## Using user inputs
class Laptop:
  def __init__(self, id, name , ram):
    self.id = id
    self.name = name 
    self.ram = ram

  def display_details(self):
    print(f"laptop Id : {self.id} \t Name : {self.name} \t RAM : {self.ram} GB")  

## Function to get input for a single laptop
def get_laptop_input(laptop_number):
  print(f"\nEnter details for laptop {laptop_number}")
  id = int(input("Enter Laptop ID: "))
  name = input("Enter Laptop Name: ")
  ram =  input("Enter RAM (in GB): ")
  return Laptop(id , name, ram)

# Create 3 Laptop objects using user input
laptops = []
for i in range(2):
  laptops.append(get_laptop_input(i+1))

# Print details of all laptops
print("Laptop details: ")
for laptop in laptops:
  laptop.display_details()