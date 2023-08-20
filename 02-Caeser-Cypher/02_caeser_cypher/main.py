from cipher_art import logo

def caeser(msg, key, type):
    result_msg = ""
    for i in msg.lower():
        if type == "encrypt":
            result_msg += chr((ord(i) - 97 + key) % 26 + 97)
        elif type == "decrypt":
            result_msg += chr((ord(i) - 97 - key) % 26 + 97)
    type_msg = "Encrypted" if type == "encrypt" else "Decrypted"
    print(f"{type_msg} message is: {result_msg}")

print(logo)

stop = False

while stop != True:
    operation = str(input(r"Type 'encypt' to encrypt the message and 'decrypt' to decrypt the message: ")).lower()

    if operation in ["encrypt", "decrypt"]:
        message = str(input("Enter Message: "))
        key = int(input("Enter Key: "))
        caeser(msg=message, key=key, type=operation)
    else:
        print(r"Invalid Operation. Use 'encrypt' or 'decrypt")

    choice = ''
    while choice not in ['y', 'n']:
        choice = str(input("Do you wish to continue(y/n)?: ")).lower()
        if choice in ['y', 'n']:
            break
        else:
            print("Invalid Choice. Try Again.")
    
    if choice == 'n':
        break

