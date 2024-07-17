import tkinter as tk

def change_value():
  label.config(text="Namaste")


root = tk.Tk()
root.title("Jeshik Phuyal")
root.geometry("300x300")

label = tk.Label(root, text = "Hello")
label.pack(pady=5)

button = tk.Button(root, text="Change Text", command=change_value)
button.pack(pady=5)

root.mainloop()