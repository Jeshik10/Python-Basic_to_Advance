# income = 70000
# expenses = 50000

# print(f"Income is {income}")
# print(f"Expenses is {expenses}")
# print(f"Diff is {income-expenses}")

bill_total = float(input("Enter the bill total: Rs."))

# Get the desired tip percentage from the user
tip_percentage = float(input("Enter the tip percentage: %"))

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



