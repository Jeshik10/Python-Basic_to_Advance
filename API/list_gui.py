import tkinter as tk 
import json
import requests

root = tk.Tk()
root.title("Quote App")  # Corrected 'titel' to 'title'
root.geometry("800x800")

def createlist(root, items):
    listbox = tk.Listbox(root)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)
    for i, item in enumerate(items, start=1):
        listbox.insert(tk.END, f"{i}. {item}")  # Corrected 'End' to 'END' and added numbering

url = "https://jsonguide.technologychannel.org/quotes.json"
response = requests.get(url)
quotes = json.loads(response.text)

clean_quotes = []  # Create a list to store clean quotes

for quote in quotes:
    # Strip quotation marks from the beginning and end of each quote
    clean_quote = quote["text"].strip('"')
    clean_quotes.append(clean_quote)

createlist(root, clean_quotes)  # Pass the list of clean quotes to createlist

root.mainloop()