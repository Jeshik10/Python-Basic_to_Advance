## Create a list of 10 employees, each belonging to a different department, and print the details of all employees who are in the IT department.

employees = [
  ("Bikesh Shrestha", "Sales"),
  ("Sarbghya Jamkattel", "Marketing"),
  ("Manish Chhetri", "IT"),
  ("Saurab Ghimire", "Human Resources"),
  ("Diwakar Bhattarai", "IT"),
  ("Rabina Phuyal", "Operations"),
  ("Ram Magar", "Research and Development"),
  ("Manisha Lamichhane", "Customer Service"),
  ("Tsering lama", "IT"),
  ("Hari Karki", "Product Management")
]

# Print details of employees in the IT department
print("Employees in the IT department:")
for name, department in employees:
    if department == "IT":
        print(f"{name}: {department}")