import tkinter as tk
from tkinter import messagebox

def calc_square():
  num = float(entry1.get())
  square = num * num
  # messagebox.showinfo("Results",f"The square of {num} is {square}")
  label.config(text=f"The square of {num} is {square}")

root = tk.Tk()
root.title("Jeshik Phuyal")
root.geometry("300x300")

label1 = tk.Label(root, text="Enter a number: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)



# Button
button = tk.Button(root, text = "Calculate Square", command = calc_square)
button.pack(pady=5)


label = tk.Label(root, text = "")
label.pack(pady=5)

# Run
root.mainloop()

# Create a program that calculate ROI in % 
# eg invest = 10000
# return = 100000

# profit = income - investment
# ROI = profit / investment * 100
