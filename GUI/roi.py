# Create a program that calculate ROI in % 
# eg invest = 10000
# return = 100000

# profit = income - investment
# ROI = profit / investment * 100

import tkinter as tk

def return_on_investment():
  investment = float(entry1.get())
  income = float(entry2.get())
  
  profit = income - investment
  total_roi =  round((profit / investment) * 100,2)

  label.config(text=f"The total Return On Investment (in %) is: {total_roi}")

 
root = tk.Tk()
root.title("Simple Interest")
root.geometry("300x200")

label1 = tk.Label(root, text="Enter total investment: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label1 = tk.Label(root, text="Enter Income: ")
label1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)


# Button
button = tk.Button(root, text = "Return On Investment", command = return_on_investment)
button.pack(pady=5)

label = tk.Label(root, text = "")
label.pack(pady=5)

# Run
root.mainloop()