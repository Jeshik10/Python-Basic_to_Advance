## To check if you are eligible to vote or not
'''
birth_year = int(input("Enter your birth year: "))
age = 2024 - birth_year

print(f"Your age is: {age}")

if age >= 18:
  print("You can vote!")
else:
  print("You are not eligible to vote!")

'''
## To calulate if price is expensive or cheap
'''
price = float(input("Enter your price: "))

if price >= 500:
  print("Price is expensive")
else:
  print("Price is okay")

'''

## To calculate if a number is even or odd

'''
number = int(input("Enter a number: ")) 

if number % 2 == 0:
  print("It is Even no.")
else:
  print("It is Odd no.")  

number = int(input("Enter a number: ")) 
'''

## To calculate which one is greater!
'''
n1 = int(input("Enter a first number: ")) 
n2 = int(input("Enter a second number: ")) 
n3 = int(input("Enter a third number: ")) 

if n1 > n2 and n1 > n3:
  print(f"{n1} is greater!")
elif n2 > n1 and n2 > n3:  
  print(f"{n2} is greater!")
elif n3 > n1 and n3 > n2:  
  print(f"{n3} is greater!") 
else:
  print("Something is wrong")
'''

# Day Finder
no_of_day =  int(input("Enter a number of day[1-7]: "))

if no_of_day == 1:
  print("Day is Sunday")
elif no_of_day == 2:
  print("Day is Monday")
elif no_of_day == 3:
  print("Day is Tuesday")
elif no_of_day == 4:
  print("Day is Wednesday")
elif no_of_day == 5:
  print("Day is Thursday")
elif no_of_day == 6:
  print("Day is Friday")
elif no_of_day == 7:
  print("Day is Saturday")
else:
  print("Invalid Option!")  
  


