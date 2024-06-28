# TO store expenses from sunday to saturday and find total expenses and average expense
sunday_expeses = 2000
monday_expenses = 2000
tuesday_expenses = 1000
wednesday_expenses = 3000
thursday_expenses = 4000
friday_expenses = 2000
saturday_expenses = 1000

total_expenses = sunday_expeses + monday_expenses + tuesday_expenses + wednesday_expenses + thursday_expenses + friday_expenses + saturday_expenses

avg_expenses = total_expenses / 7

print(f"Total weekly expenses is RS.{total_expenses}")
print(f"Average Expense is Rs.{avg_expenses: .2f}")

