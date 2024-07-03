# Function
'''
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Jeshik'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

'''
'''
# Defining function
def display_name():
  print("My name is Jeshik Phuyal")

# Calling funtion
display_name()

'''

# Create a function that display your address

'''
# Defining function
def display_address():
  print("I live in kathmandu")

# Calling funtion
display_address()
'''

# WAP to print even number between start and end using function
'''
def display_even(first, last):
  for i in range(first, last+1):
    if i % 2 == 0:
      print(i)

start = 100
end = 150

display_even(start, end)
'''


# Types of function:
# System Define
# User Define

## 1. No Parameter and No return Type

def display_details():
  print("My name is Jeshik Phuyal")
  print("I am from KTM")

display_details()

## 2. Parameter and No return type

def add(n1, n2):
  total = n1 + n2
  print(f"Total is :{total}")

add(2,5)

## 3. Parameter and return type

def find_cube(a):
    return a ** 3

print(find_cube(2))

## 4. No Parameter and return type

def voter_age():
  return 18

print(voter_age())


