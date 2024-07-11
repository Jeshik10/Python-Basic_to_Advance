from customer import Customer

choice_txt = """
What do you want to do[1-2]?
1. Add Customer Details.
2. View All Details.
"""
choice = int(input(choice_txt))
if choice == 1:
  c = Customer(id=0, name="", phone=0, balance=0)
  c.id = int(input("Enter Customer ID: "))
  c.name = (input("Enter Customer name: "))
  c.phone = int(input("Enter Customer phone_no.: "))
  c.balance = float(input("Enter Customer balance: "))
  f = open('customer.csv','a')
  f.write(f"{c.id}, {c.name}, {c.phone}, {c.balance}\n")
  f.close()
  print("Details Added Successfully!")

elif choice == 2:
    f = open('customer.csv','r')
    print("All Customers are:\n--------------")
    print(f.read())
    print("--------------")