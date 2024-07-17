# create a program that calculate simple interst using gui
import tkinter as  tk
from tkinter import messagebox

def simple_interest():
  P = float(entry1.get())
  T = float(entry2.get())
  R = float(entry3.get())
  result =  (P*T*R)/100

  messagebox.showinfo("Results",f"The interest is {result}")

root = tk.Tk()
root.title("Simple Interest")
root.geometry("3000x200")

label1 = tk.Label(root, text="Enter Principle: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label1 = tk.Label(root, text="Enter Time: ")
label1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

label1 = tk.Label(root, text="Enter Rate: ")
label1.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

# Button
button = tk.Button(root, text = "Simple Interest", command = simple_interest)
button.pack(pady=5)

# Run
root.mainloop()