add = 0
reduce = 0
cost = 0

def add_keychain():
    global reduce
    global add
    add = int(input("You have {} keychains. How many to add? ".format(reduce)))
    reduce += add
    print("Now you have {} keychains.".format(reduce))

def remove_keychain():
    global reduce
    remove = int(input("You have {} keychains. How many to remove? ".format(reduce)))
    reduce -= remove
    print("Now you have {} keychains.".format(reduce))

def current_order():
    global reduce
    global cost
    cost = 10 * reduce
    print("Now you have {} keychains.".format(reduce))
    print("Keychains cost $10 each.")
    print("Total cost is: ${}.".format(cost))

def checkout():
    global reduce
    global cost
    name = input("What is your name? ")
    print("You have {} keychains.".format(reduce))
    print("Keychains cost $10 each.")
    print("Total cost is: ${}.".format(cost))
    print("Thank you for your order, {}.".format(name))

while True:
    print("Ye Olde Keychain Shoppe")
    print("1. Add keychains to order")
    print("2. Remove keychains from order")
    print("3. View current order")
    print("4. Checkout")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        add_keychain()
    elif choice == 2:
        remove_keychain()
    elif choice == 3:
        current_order()
    elif choice == 4:
        checkout()
        break
    else:
        print("Please enter a valid choice.")
