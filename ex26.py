 
def add_keychains():
    print("add_keychains has been called")

def remove_keychains():
    print("remove_keychains has been called")

def view_order():
    print("view_order has been called")

def checkout():
    print("checkout has been called")

while True:
    print("1. Add Keychains")
    print("2. Remove Keychains")
    print("3. View Order")
    print("4. Checkout")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_keychains()
    elif choice == 2:
        remove_keychains()
    elif choice == 3:
        view_order()
    elif choice == 4:
        checkout()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")        
        
