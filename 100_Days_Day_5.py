######################
# Password Generator #
######################

# Beginning
print("Time to get you a new password that won't be cracked in 2 seconds!\n")

# Possible Characters For Password
possible_uppercase_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
possible_lowercase_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
possible_symbols = "~ ! @ # $ % ^ & * ( ) - =".split()
possible_numbers = "1 2 3 4 5 6 7 8 9 0".split()

print(possible_uppercase_letters)
print(possible_lowercase_letters)
print(possible_symbols)
print(possible_numbers)

# Clarifying Questions
# "How many uppercase letters would you like in your password?"
# "How many lowercase letters would you like in your password?"
# "How many symbols would you like?"
# "How many numbers would you like?"

# for n in range(0, len(password)):
#     password[n] = int(password[n])

# Generate Password
# "Here is your password: "