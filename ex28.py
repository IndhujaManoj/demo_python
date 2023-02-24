sales_tax=0.0825
shipping_cost=5.0
per_keychain_shippingcost=1.0

def get_num_keychains():
    while True:
        num_keychains = int(input("Enter the number of keychains to purchase: "))
        if num_keychains >= 0:
            return num_keychains
        else:
            print("Error: The number of keychains must be non-negative.")

def get_menu_choice():
    while True:
        print("1. Add keychains to the order")
        print("2. Remove keychains from the order")
        print("3. View the current order")
        print("4. Checkout")
        choice = int(input("Enter your choice: "))
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            print("Error: Invalid menu choice. Please try again.")
def calculate_shipping(num_keychains):
    return shipping_cost + (num_keychains * per_keychain_shippingcost)
def calculate_subtotal(num_keychains , price_per_keychain ):
    return num_keychains * price_per_keychain
def calculate_tax(subtotal):
    return subtotal *sales_tax
def calculate_total(subtotal,shipping,tax):
    return subtotal + shipping + tax
def view_order(num_keychains, price_per_keychain, tax, base_shipping, per_keychain_shipping):
    shipping = calculate_shipping(num_keychains)
    subtotal = calculate_subtotal(num_keychains, price_per_keychain)
    total = calculate_total(subtotal, shipping, tax)
    print("Number of keychains: ", num_keychains)
    print("Price per keychain: $", price_per_keychain)
    print("Shipping charges: $", shipping)
    print("Subtotal before tax: $", subtotal)
    print("Tax on the order: $", tax)
    print("Final cost of the order: $", total)
def checkout(num_keychains, price_per_keychain, tax, base_shipping, per_keychain_shipping):
    name = input("Enter your name: ")
    view_order(num_keychains, price_per_keychain, tax, base_shipping, per_keychain_shipping)
    print("Thank you, ", name, ", for your order!")

def run():
    num_keychains = 0
    price_per_keychain = 10
    tax = sales_tax
    base_shipping = shipping_cost
    per_keychain_shipping = per_keychain_shippingcost
    while True:
        choice = get_menu_choice()
        if choice == 1:
            num_keychains += get_num_keychains()
        elif choice == 2:
            num_keychains -= get_num_keychains()
        elif choice == 3:
            view_order(num_keychains, price_per_keychain, tax, base_shipping, per_keychain_shipping)
        elif choice == 4:
            checkout(num_keychains, price_per_keychain, tax, base_shipping, per_keychain_shipping)
            break

run()


