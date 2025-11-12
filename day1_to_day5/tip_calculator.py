print('Welcome to the tip calculator!')

bill = float(input('What was the total bill? $: '))
tip = int(input('What percentage tip would you like to give?' \
' 10, 12, or 15?: '))
people = int(input('How many people to split the bill?: '))

payment = bill +  (bill * tip / 100)
payment_per_person = payment / people

print('The total bill is: $' + payment.__format__('.2f'))
print('Each person should pay: $'
       + payment_per_person.__format__('.2f'))   