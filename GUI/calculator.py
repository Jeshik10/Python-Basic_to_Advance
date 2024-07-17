# Create a visually appealing program using Python's tkinter library that calculates the sum, difference, product, and quotient of two user-entered numbers.

import tkinter as tk
from tkinter import messagebox

def calculate():
  # Get value from textbox
  num1 = float(entry1.get())
  num2 = float(entry2.get())

  sum = num1 + num2
  diff = num1 - num2
  multiply = num1 * num2

  if num2 != 0:
    quotient = num1 / num2
  else:
    quotient = "Undefined"

  # Create a single message with all results
  result_message = f"Sum is {sum:.2f}\n"
  result_message += f"Difference is {diff:.2f}\n"
  result_message += f"Product is {multiply:.2f}\n"
  result_message += f"Quotient is {quotient if isinstance(quotient, str) else f'{quotient:.2f}'}"

  # Display all results in a single messagebox
  messagebox.showinfo("Results", result_message)


root = tk.Tk()
root.title("Calculator")
root.geometry("500x200")

# For First number
label1 = tk.Label(root, text="Enter First Number: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# For Second number
label2 = tk.Label(root, text="Enter Second Number: ")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button
button = tk.Button(root, text = "Calculate", command = calculate)
button.pack(pady=5)

# Run
root.mainloop()


