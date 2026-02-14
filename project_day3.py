import random
import string
print("Welcome to the Password Generator!")
l= int(input("Enter the length of the password: "))
up = input("Include uppercase letters? (y/n): 🙂‍↕️\t").lower()
low = input("Include lowercase letters? (y/n): 👾\t").lower()
num = input("Include numbers? (y/n): ❄️\t").lower()
sym = input("Include symbols? (y/n): 💀\t").lower()

password = ""
characters = ""
if up == "y":
    characters += string.ascii_uppercase
if low == "y":
    characters += string.ascii_lowercase
if num == "y":
    characters += string.digits
if sym == "y":    
    characters += string.punctuation
#safty check to ensure at least one character type is selected
if characters == "":
    print("Error: You must select at least one character type!‼️")
else:
    password = ""
    for i in range(l):
        password += random.choice(characters)
    print("Your password is:🦾😉\n", password)