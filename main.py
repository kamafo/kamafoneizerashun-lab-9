# This is Kamafo Neizer-Ashun's main.py file
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decode(password):
    decoded_password = ""
    for digit in password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


if __name__ == "__main__":
    
    print("""Menu
    -------------
    1. Encode
    2. Decode 
    3. Quit""")

    stop = False
    encoded_password = None

    while not stop:
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")

        elif option == "3":
            stop = True
