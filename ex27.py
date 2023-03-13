current_number=0
price_perkeychain=10
def add_keychain():
    num_keychain=int(input("how many keychain would you like to add?:"))
    global keychains
    keychains= current_number + num_keychain
    print("Now you have",keychains," keychains")
    return keychains
add_keychain()
print("______________________________________________________________________________________")
def remove_keychains():
    num_remove=int(input("How many number of keychains would you like to remove?:"))
    global remove
    remove=keychains-num_remove
    print("Now you have currently ",remove,"number of keychains. ")
    return remove
remove_keychains()
print("______________________________________________________________________________________")

def view_order():
    print("Now you have",remove,"number of keychains in the order.")
    print("price per keychain is $ 10.")
    global total_cost
    total_cost=remove * price_perkeychain
    print("The total cost of the keychain is $",total_cost)
view_order()
print("______________________________________________________________________________________")

def checkout():
    name=input("Enter your name:")
    print("Hi",name,"now you have",remove,"number of keychain")
    print("Price per keychain is $10")
    print("total cost of the order is ",total_cost)
    print("Thankyou ",name,"for ordering......")
checkout()    

    
