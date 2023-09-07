import secrets
import string
import random

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the Python Password Generator!")
choice = str(input("Would you like your password generation to be completely automated? Enter y for yes and n for no."))
if choice not in ["y", "n"]:
    raise ValueError("Please enter y or n.")

if choice == "n":
    nr_letters= int(input("How many letters would you like in your password?"))
    nr_symbols = int(input("How many symbols would you like?"))
    nr_numbers = int(input("How many numbers would you like?"))

    character_list=[]
    for num in range(0,nr_letters):
      character_list.append(secrets.choice(letters))
    for num in range(0,nr_numbers):
      character_list.append(secrets.choice(numbers))
    for num in range(0,nr_symbols):
      character_list.append(secrets.choice(symbols))
    password=""
    random.shuffle(character_list)
    password = password.join(character_list)
    print(password)

if choice == "y":
    characters = letters + numbers + symbols

    character_list=[]
    for num in range(random.randint(10,18)):
      character_list.append(secrets.choice(characters))

    password=""
    random.shuffle(character_list)
    password = password.join(character_list)
    print(password)