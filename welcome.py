# expenses = []
# days = ["sunday","monday","tuesday","thursday","wednesday","friday","saturday"]

# #loop
# for day in days:
#  expense = float (input(f"Enter the expense for {day}: "))
#  expenses.append(expense)

#  #calculaion
# total_expenses = sum(expenses)
# print(f"The total expenses for the week is: Rs.{total_expenses : .2f}")

# avg_daily_expenses = total_expenses / len(expenses)
# print(f"The average daily expense is : {avg_daily_expenses : .2f}") 

'''
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def get_expenses(self):
        print("Enter your expenses for the week:")
        for day in self.days:
            expense = self.validate_input(f"Enter your expense for {day}: ")
            self.expenses.append(expense)

    def validate_input(self, prompt):
        while True:
            try:
                expense = float(input(prompt))
                if expense < 0:
                    raise ValueError("Expense cannot be negative.")
                return expense
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid number.")

    def calculate_expenses(self):
        total_expenses = sum(self.expenses)
        average_daily_expenses = total_expenses / len(self.expenses)
        print(f"\nTotal expenses for the week: ${total_expenses:.2f}")
        print(f"Average daily expenses: ${average_daily_expenses:.2f}")
    def run(self):
        self.get_expenses()

        self.calculate_expenses()

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
'''


# user_input = input("Enter your full name: ")
# first_name, symbol, last_name = user_input.split()
# print(f"First name: {first_name}")
# print(f"Symbol: {symbol}")
# print(f"domain: {last_name}")

user_input = input("Enter your email address: ")
parts = user_input.split('@')

name, domain = parts
print(f"Name: {name}")
print(f"Symbol: @")
print(f"Domain: {domain}")
# else:
#     print("Invalid email format")