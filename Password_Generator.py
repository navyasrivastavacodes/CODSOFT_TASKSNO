# -----------------------------------------
# Password Generator
# Generates a random password based on the
# length entered by the user.
# -----------------------------------------

import string
import random

while True:

    print("======================================")
    print("        PASSWORD GENERATOR")
    print("======================================")

    characters = string.ascii_letters + string.digits + string.punctuation

    password_length = int(input("Enter the password length: "))

    if password_length <= 0:
        print("Invalid password length!")

    else:
        print("Generated Password: ", end="")

        for i in range(password_length):
            print(random.choice(characters), end="")

        print()  # Move to the next line after printing the password

        generate_again = input("Generate another password? (yes/no): ").strip().lower()

        if generate_again == "no":
            print("Thank you for using the Password Generator!")
            break
        elif generate_again == "yes":
            continue
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")