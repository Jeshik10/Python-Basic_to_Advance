from datetime import datetime

# Wap to find date difference

birthdate = datetime.date(2000,2,14)
currentdate= datetime.date.today()

age =  currentdate - birthdate
print(age)

# Wap to find differnce betwwen years , months and days 

def date_difference(date1, date2):
  d1 =  datetime.strptime(date1, "%Y-%m-%d")
  d2 =  datetime.strptime(date2, "%Y-%m-%d")

  diff = abs(d2 - d1)

  years = diff.days // 365
  months =  (diff.days % 365) // 30
  days = (diff.days % 365) % 30

  return f"{years} years, {months} months, {days} days"

date1 =  input("Enter the first date (YYYY-MM-DD): ")
date2 =  input("Enter the second date (YYYY-MM-DD): ")

try:
  result = date_difference(date1,date2)
  print(f"The difference between {date1} and {date2} is: ")
  print(result)

except ValueError:
  print("Invalid date format. please use YYYY-MM-DD.")  



'''
now = datetime.datetime.now()
print(now)

# Today's Date
print(datetime.date.today().year)

bithdate =  datetime.date(2000,2,14)
print(bithdate)
'''