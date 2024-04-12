"""
Team Members: Cesar Carballo, Jinghan Wu
"""

def encode(password):
    encoded_password = ""
    for char in password:
        char = int(char)
        char += 3
        encoded_password += str(char)
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        if int(char) <= 2:
            decoded_char = 10 + (int(char) - 3)
            decoded_password += str(decoded_char)
        else:
            decoded_char = int(char) - 3
            decoded_password += str(decoded_char)
    return decoded_password

if __name__ == "__main__":
    while True:
        print("Password Changer Menu Options:")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        print(" ")
        choice = input("Please Select a Menu Option: ")
        print(" ")
        if (choice != "1") and (choice != "2") and (choice != "3"):
            print("Invalid Menu option Please select again: ")
            choice = input("Please Select a Menu Option: ")
        if choice == "1":
            password = input("Please Enter a Numeric Password to Encode: ")
            password = encode(password)
            print("Encoded Password is: ", password)
            print(" ")
        if choice == "2":
            decoded_password = decode(password)
            print(f"The encoded password is {password}, "
                  f"and the original password is {decoded_password}.")
        if choice == "3":
            print("Thank you for USing Password Changer")
            break



