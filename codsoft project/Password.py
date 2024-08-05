import random
import string
def generate_password(length, use_uppercase, use_digits, use_special):
    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password
def main():
 print("Welcome to the Password Generator!")
while True:
    try:
            length = int(input("Enter the desired length of the password: "))
    finally:
        length <= 0
        break
print("Please enter a valid positive integer for the password length")
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
password = generate_password(length, use_uppercase, use_digits, use_special)
print(f"\nGenerated Password: {password}")


