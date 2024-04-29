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

# print(possible_uppercase_letters)
# print(possible_lowercase_letters)
# print(possible_symbols)
# print(possible_numbers)

# Clarifying Questions
number_of_uppercase = int(input("How many uppercase letters would you like in your password? \n"))
number_of_lowercase = int(input("How many lowercase letters would you like in your password? \n"))
number_of_symbols = int(input("How many symbols would you like? \n"))
number_of_numbers = int(input("How many numbers would you like? \n"))

# The (currently) empty list that will store the eventual password characters.
password_list = []

# Below are the for loops to generate random characters.
for upper in range(0, number_of_uppercase):
    uppercase_choices = random.choice(possible_uppercase_letters)
    password_list.append(uppercase_choices)

for lower in range(0, number_of_lowercase):
    lowercase_choices = random.choice(possible_lowercase_letters)
    password_list.append(lowercase_choices)

for symbol in range(0, number_of_symbols):
    symbol_choices = random.choice(possible_symbols)
    password_list.append(symbol_choices)

for number in range(0, number_of_numbers):
    number_choices = random.choice(possible_numbers)
    password_list.append(number_choices)

# Temporarily printing the (now) full list of password characters.
print(password_list)
print()

# Generate Password
print("Here is your password: ")