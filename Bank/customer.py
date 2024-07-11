#Develop a software application for a bank that includes functionalities to add and view customer information. Each customer should have an ID, name, phone number, and balance.

class Customer:
  def __init__(self, id, name, phone, balance):
    self.id = id
    self.name = name
    self.phone = phone
    self.balance = balance
    
    