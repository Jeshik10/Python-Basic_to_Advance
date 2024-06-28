#-------------------------- 1 --------------------------

# 1. Create a program that convert nepali currency to usd, euro and japanese currency.

# First method : Using User inputs
rates = {
 'USD' : 0.0075,
 'EUR' : 0.0068,
 'JPY' : 1.12,
}

nepali_npr = float(input(f"Enter an amount in NPR: Rs. "))
choice = input(f"Enter a choice (USD/EUR/JPY): ")

if choice in rates:
  changed_currency = rates[choice] * nepali_npr
  print(f"The {nepali_npr} NPR is: {changed_currency:.2f} {choice}")
else:
  print(f"Invalid Input!")

# Second method : To print all currencies output at once

rates = {
 'USD' : 0.0075,
 'EUR' : 0.0068,
 'JPY' : 1.19,
}
symbols = {
    'USD': '$',
    'EUR': '€',
    'JPY': '¥'
}
nepali_npr = float(input(f"Enter an amount in NPR: Rs. "))

for currency, rate in rates.items():
  changed_currency = rate * nepali_npr
  symbol = symbols[currency]
  print(f"NRS.{nepali_npr:.2f} is = {symbol} {changed_currency:.2f} ")


#------------------------- 2 --------------------------
##-------------2. Develop a basic calculator that performs addition, subtraction, multiplication, and division based on user input.-----------------------

num1 = float (input(f"Enter first number: "))
num2 = float (input(f"Enter second number: "))

print("\nSelect operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choice = input("Enter choice (1/2/3/4/5): ")

if choice == '1':
  sum = num1 + num2
  print(sum)
elif choice == '2':
  diff = num1 - num2
  print(diff) 
elif choice == '3':
  mul = num1 * num2
  print(mul)
elif choice == '4':
  div = num1 / num2
  print(div)
elif choice == '5':
  print(f"Exited")
else:
  print(f"Invalid Choice")



###------------------------- 3 -----------------------------
###--------------3. Create a program that calculates simple interest based on user input for principal, rate, and time. -----------------------


Principal = float(input(f"Enter a Pricipal: "))
Time = float(input(f"Enter a Time in year: "))
Rate = float(input(f"Enter a Rate in %: "))

simple_interest = (Principal * Time * Rate) / 100
print (f"Simple Interest is : RS. {simple_interest: .2f}")



###---------------------- 4 ------------------------------
###---------4. Write a script that calculates Body Mass Index (BMI) from user input (height and weight) using variables, data types, and operators.  -------------------------

weight = float(input(f"Enter the weight of a person : "))
height = float(input(f"Enter the weight of a person : "))

bmi = (weight / (height ** 2))
print(f"BMI: {bmi:.2f} ")

if bmi < 18.5:
  print(f"Under Weight")

elif 18.5 <= bmi < 25:
  print(f"Normal Weight")

elif 25 <= bmi < 30:
  print(f"Over Weight")

else:
  print(f"Obese")


##---------------------- 5 ------------------------------
###--------------5.Create a simple password generator-------------------------

import random

length = 8
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password = ""

for _ in range(length):
    password += random.choice(chars)

print("Generated password:", password)


##---------------------- 6 ------------------------------
###------------6. Write a program that calculates a user's age based on their birth year.--------

current_year = 2024
birth_year = int(input("Enter your birth year: "))

if birth_year <= current_year:
  current_age = current_year - birth_year
  print(f"Your are: {current_age} years old")
else:
  print(f"You are not born yet!")  


##---------------------- 7 ------------------------------
#-----------7. Write a script that calculates the tip amount based on the bill total and desired tip percentage entered by the user -----------

# Get the bill total from the user
bill_total = float(input("Enter the bill total: Rs."))

# Get the desired tip percentage from the user
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the tip amount
tip_amount = bill_total * (tip_percentage / 100)

# Calculate the total amount including tip
total_amount = bill_total + tip_amount

# Round the results to two decimal places
tip_amount = round(tip_amount, 2)
total_amount = round(total_amount, 2)

# Display the results
print(f"\nBill summary:")
print(f"Bill total: Rs.{bill_total:.2f}")
print(f"Tip percentage: {tip_percentage}%")
print(f"Tip amount: Rs.{tip_amount:.2f}")
print(f"Total amount (including tip): Rs.{total_amount:.2f}")

##---------------------- 8 ------------------------------
# 8. Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin using basic input and output, variables, and operators.

# Display menu
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

# Get user choice
choice = input("Enter your choice (1-6): ")

# Get temperature value
temp = float(input("Enter the temperature value: "))

# Perform conversion based on user choice
if choice == '1':
    result = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {result:.2f}°F")

elif choice == '2':
    result = temp + 273.15
    print(f"{temp}°C is equal to {result:.2f}K")

elif choice == '3':
    result = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {result:.2f}°C")

elif choice == '4':
    result = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F is equal to {result:.2f}K")

elif choice == '5':
    result = temp - 273.15
    print(f"{temp}K is equal to {result:.2f}°C")

elif choice == '6':
    result = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K is equal to {result:.2f}°F")

else:
    print("Invalid choice. Please enter a number between 1 and 6.")


##---------------------- 9 ------------------------------
#----- 9. Develop a script that converts distances between kilometers, miles, and meters based on user input-----

print("Distance Converter")
print("1. Kilometers to Miles")
print("2. Kilometers to Meters")
print("3. Miles to Kilometers")
print("4. Miles to Meters")
print("5. Meters to Kilometers")
print("6. Meters to Miles")

choice = input("Enter your choice (1-6): ")
value = float(input("Enter the distance value: "))

if choice == '1':
    result = value * 0.621371
    print(f"{value} kilometers is equal to {result:.2f} miles")

elif choice == '2':
    result = value * 1000
    print(f"{value} kilometers is equal to {result:.2f} meters")

elif choice == '3':
    result = value * 1.60934
    print(f"{value} miles is equal to {result:.2f} kilometers")

elif choice == '4':
    result = value * 1609.34
    print(f"{value} miles is equal to {result:.2f} meters")

elif choice == '5':
    result = value / 1000
    print(f"{value} meters is equal to {result:.2f} kilometers")

elif choice == '6':
    result = value / 1609.34
    print(f"{value} meters is equal to {result:.2f} miles")

else:
    print("Invalid choice. Please enter a number between 1 and 6.")


##---------------------- 10 ------------------------------    
##------ 10. Write a program that generates a username based on user input (e.g., first name, last name, favorite number) and ensures it meets certain criteria. ----   

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_number = input("Enter your favorite number: ")

# Create username
username = first_name[:3].lower() + last_name[:3].lower() + favorite_number

# Display the generated username
print(f"\nYour generated username is: {username}")


##---------------------- 11 ------------------------------  
##-------- 11. Create a program that formats a user-provided email address into different parts (username, domain) and validates its structure. -------

user_input = input("Enter your email address: ")
parts = user_input.split('@')
if len(parts) == 2:
    name, domain = parts
    print(f"Name: {name}")
    print(f"Symbol: @")
    print(f"Domain: {domain}")
else:
    print("Invalid email format")