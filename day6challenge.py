# Create a program that ask user to enter no. of month and display corresponding month.

months = [
    "January", "February", "March", "April", "May", "June",                
    "July", "August", "September", "October", "November", "December"
]

month_no =  int(input("Enter a month number [1-12]: "))

if 1 <= month_no <= 12:
  month_name = months[month_no - 1]
  print(f"{month_no} is: {month_name}")

else:
  print("Invalid Option!")