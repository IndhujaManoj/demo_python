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
else:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")
