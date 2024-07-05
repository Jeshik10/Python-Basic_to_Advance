## Program that asks user to enter n number of todo and display

'''
todos = []

total_todo = int(input("Enter total number of todo: "))

for i in range(1,total_todo+1):
  todo = input(f"Enter todo {i}: ")
  todos.append(todo)

print("\n-----------\n")  
print("All todos are: ")

# Display all result
for todo in todos:
    print(todo)
  
'''

fruits = []

total_fruit = int(input("Enter total number of fruits: "))
##  ASK
for i in range(1,total_fruit+1):
  todo = input(f"Enter fruit {i}: ")
  fruits.append(todo)

print("\n-----------\n")  
print("All fruits are: ")

# Display all result
for fruit in fruits:
  print(f"{fruit}")