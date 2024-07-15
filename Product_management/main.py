from product import Product
import controller as c

choice_txt = """
What do you want to do?
1. Add Product Details.
2. View All Products.
3. View Product By ID.
4. Update Product.
5. Delete Product.
6. Exit
"""

while True:
    choice = input(choice_txt)
    
    if choice == '1':
        c.add_product()
    elif choice == '2':
        c.view_all_products()
    elif choice == '3':
        c.view_single_product()
    elif choice == '4':
        c.update_product()
    elif choice == '5':
        c.delete_product()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")