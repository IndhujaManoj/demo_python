"""
pin = 12345

print("WELCOME TO THE BANK OF MITCHELL.")
entry = int(input("ENTER YOUR PIN: "))

while entry != pin:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))

print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

"""




pin = 12345
tries = 0

print("WELCOME TO THE BANK OF MITCHELL.")
while tries < 3:
    entry = int(input("ENTER YOUR PIN: "))
    tries += 1
    if entry == pin:
        print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
        break
    else:
        print("\nINCORRECT PIN. TRY AGAIN.")
