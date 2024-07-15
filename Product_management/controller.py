import csv
from product import Product

products = []

def add_product():
    id = input("Enter product ID: ")
    name = input("Enter product name: ")
    qty = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    
    product = Product(id, name, qty, price)
    products.append(product)
    
    # Save to CSV file
    with open('products.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([product.id, product.name, product.qty, product.price])

def view_all_products():
    try:
        with open('products.csv', 'r') as f:
            print("All Products are:\n--------------")
            print(f.read())
            print("--------------")
    except FileNotFoundError:
        print("No products file found. The product list is empty.")

def view_single_product():
    id = input("Enter product ID to view: ")
    found = False
    try:
        with open('products.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id:
                    print(f"Product ID: {row[0]}")
                    print(f"Name: {row[1]}")
                    print(f"Quantity: {row[2]}")
                    print(f"Price: Rs.{float(row[3]):.2f}")
                    found = True
                    break
        if not found:
            print("Product not found.")
    except FileNotFoundError:
        print("No products file found. The product list is empty.")

def update_product():
    id = input("Enter product ID to update: ")
    found = False
    updated_products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id:
                    name = input("Enter new name (press enter to skip): ") or row[1]
                    qty = input("Enter new quantity (press enter to skip): ") or row[3]
                    price = input("Enter new price (press enter to skip): ") or row[2]
                    updated_products.append([id, name, qty, price])
                    found = True
                else:
                    updated_products.append(row)
        
        if found:
            with open('products.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_products)
            print("Product updated successfully!")
        else:
            print("Product not found.")
    except FileNotFoundError:
        print("No products file found. The product list is empty.")

def delete_product():
    id = input("Enter product ID to delete: ")
    found = False
    updated_products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != id:
                    updated_products.append(row)
                else:
                    found = True
        
        if found:
            with open('products.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_products)
            print("Product deleted successfully!")
        else:
            print("Product not found.")
    except FileNotFoundError:
        print("No products file found. The product list is empty.")