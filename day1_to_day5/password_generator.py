# checking strutcture of ASCII table
# for i in range(128):
#    print(i, "→", chr(i)) 

import random

uppercase_list = []
lowercase_list = []
number_list = []
symbols_list = ['@', '*', '!']

for i in range(65, 91):
    # print(chr(i))
    uppercase_list.append(chr(i))

for i in range(97, 123):
    # print(chr(i))
    lowercase_list.append(chr(i))

for i in range(48, 58):
   # print(chr(i))
   number_list.append(chr(i))

# Checking final list strutcture
# print(uppercase_list)
# print(lowercase_list)
# print(number_list)
# print(simbols)

p_uletters = int(input('How many upper letter would you like in your password? '))
p_lletters = int(input('How many lower letter would you like in your password? '))
p_symbols = int(input('how many symbols would you like? '))
p_numbers = int(input('How many number would you like? '))

password = []

for i in range(0, p_uletters):
    choice = random.choice(uppercase_list)
    password.append(choice)

for i in range(0, p_lletters):
    choice = random.choice(lowercase_list)
    password.append(choice)

for i in range(0, p_symbols):
    choice = random.choice(symbols_list)
    password.append(choice)

for i in range(0, p_numbers):
    choice = random.choice(number_list)
    password.append(choice)

random.shuffle(password)
password_str = "".join(password)
print(f'Your password is: {password_str}')
     



