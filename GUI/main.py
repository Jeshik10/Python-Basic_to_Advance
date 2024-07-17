import tkinter as tk

root = tk.Tk()
root.title("Jeshik Phuyal")
root.geometry("1000x600")

def on_button_click():
  label.config(text = "Button Clicked")

label = tk.Label(root, text="welcome")
label.pack(pady=20)

button = tk.Button(root, text = "click me", command = on_button_click)
button.pack(pady=10)

#Run 
root.mainloop()
