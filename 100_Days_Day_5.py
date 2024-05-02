######################
# Password Generator #
######################

# Importing Module
import random

# Beginning
print("Time to get you a new password that won't be cracked in 2 seconds!\n")

# Possible Characters For Password
possible_uppercase_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
possible_lowercase_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
possible_symbols = "~ ! @ # $ % ^ & * ( ) - =".split()
possible_numbers = "1 2 3 4 5 6 7 8 9 0".split()

# Clarifying Questions
number_of_uppercase = int(input("How many uppercase letters would you like in your password? \n"))
if number_of_uppercase < 3 or number_of_uppercase > 6:
    print()
    print("You don't follow instructions well, do you?  No password for you then.")
    exit()
print()
number_of_lowercase = int(input("How many lowercase letters would you like in your password? \n"))
if number_of_lowercase < 3 or number_of_lowercase > 6:
    print()
    print("You don't follow instructions well, do you?  No password for you then.")
    exit()
print()
number_of_symbols = int(input("How many symbols would you like? \n"))
if number_of_symbols < 3 or number_of_symbols > 6:
    print()
    print("You don't follow instructions well, do you?  No password for you then.")
    exit()
print()
number_of_numbers = int(input("How many numbers would you like? \n"))
if number_of_numbers < 3 or number_of_numbers > 6:
    print()
    print("You don't follow instructions well, do you?  No password for you then.")
    exit()
print()

# The (currently) empty list that will store the eventual password characters.
password_list = []

# Below are the for loops to generate random characters.
for upper in range(0, number_of_uppercase):
    password_list.append(random.choice(possible_uppercase_letters))

for lower in range(0, number_of_lowercase):
    password_list.append(random.choice(possible_lowercase_letters))

for symbol in range(0, number_of_symbols):
    password_list.append(random.choice(possible_symbols))

for number in range(0, number_of_numbers):
    password_list.append(random.choice(possible_numbers))

# Shuffling the list of password characters.
random.shuffle(password_list)

# Putting the list of password characters into one long string.
randomly_generated_password = ""
for character in password_list:
    randomly_generated_password += character

# Finally display the randomly generated password.
print(f"Here is your randomly generated password: {randomly_generated_password}")