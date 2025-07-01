import random
import string

def generate_password():
    print("Here is your password generator 🙂")
    try:
        length = int(input("Enter the password length you want : "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated Password: {password}")
generate_password()
