"""
Team Members: Cesar Carballo, Jinghan Wu
"""

def encode(password):
    encoded_password = ""
    for char in password:
        if char == "7":
            encoded_password += "0"
        if char == "8":
            encoded_password += "1"
        if char == "9":
            encoded_password += "2"
        if (char != "7") and (char != "8") and (char != "9"):
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
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        print(" ")
        choice = input("PLease enter an option: ")
        if (choice != "1") and (choice != "2") and (choice != "3"):
            print("Invalid Menu option Please select again: ")
            choice = input("Please Select a Menu Option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")
            print(" ")
        if choice == "2":
            decoded_password = decode(password)
            print(f"The encoded password is {password}, "
                  f"and the original password is {decoded_password}.")
            print(" ")
        if choice == "3":
            break



