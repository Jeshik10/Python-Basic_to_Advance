# Add your electricity bill from January to December in dictionary and find total and average value.

electricity_bills = {
    'January': 700.32,
    'February': 750.98,
    'March': 800.04,
    'April': 950,
    'May': 1009,
    'June': 1157.89,
    'July': 1530.45,
    'August': 1235,
    'September': 1115,
    'October': 600.7,
    'November': 500.09,
    'December': 1275,
}

for month, bill in electricity_bills.items():
  print(f"Electricity bill of {month} is: Rs.{bill}")
  electricity_bills.items()

total_bill = sum(electricity_bills.values())

average_bill = total_bill / len(electricity_bills)

print(f"Total electricity bill for the year: Rs.{total_bill: .2f}")
print(f"Average monthly electricity bill: Rs.{average_bill: .2f}")

