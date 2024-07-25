# Exception Handling
# Wap to display persons age from birthdate (user input)

import datetime

def calculate_age():
  try:
    birthyear = int(input("Enter your birth date: "))
    
    age = datetime.date.today().year - birthyear
    print(f"Current age is: {age}")
    
  except:
    print("Invalid! please enter numeric values.")  

calculate_age()    