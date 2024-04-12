
encoded_password = "33332295"
decoded_password = ""

for char in encoded_password:
    if int(char) <= 2:
        decoded_char = 10 + (int(char) - 3)
        decoded_password += str(decoded_char)
    else:
        decoded_char = int(char) - 3
        decoded_password += str(decoded_char)

print(decoded_password)