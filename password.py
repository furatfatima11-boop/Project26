print("Welcome to the random password generator!")
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

while True:
    password = ""
    for i in range(12): 
        password += random.choice(characters)
    print("Generated Password:", password)
    answer = input("Do you like this password? (yes/no): ")
    if answer.lower() == "yes":
        print("Great!")
        break