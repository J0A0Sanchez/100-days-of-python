"""Simple if else exercise to check if someone over or under
120cs of height can go in rollercoaster.

But include another condition based on age:
>=18 pay 18
Between 12 - 18 pay 12
<12 pay 5

And inclue if they want photos by 3$"""

print("Welcome to the Rollercoaster!")
print("-"*30)
print("    Price List:\n"
      "• Adults (18 years and older): $18\n"
      "• Teenagers (12 to 17 years old): $12\n"
      "• Children (under 12 years old): $5")
print("-"*30)

height = int(input("What is your height in cm?: "))
adults_price = 18
teenagers_price  = 12
children_price = 5
photo_price = 3

if height >= 120:
    print("You can go in based on your height")

    age = int(input("What is your age?: "))

    if  age >= 45 and age <=50:
        print("You are in the age group that gets a free ride. Enjoy!")
        category_set_price = 0

    elif age >= 18:
        print(f"Price {adults_price}$")
        category_set_price = adults_price

    elif age >= 12 and age < 18:
        print(f"Price {teenagers_price}$")
        category_set_price = teenagers_price

    else:
        print(f"Price {children_price}$")
        category_set_price = children_price

    photo = str(input("Do you want photos? - [Y/N]:")).upper()

    if photo == "Y":
        print("The cost for photos is 3$")
        print(f"The total bill is {category_set_price + 3}")

    else:
        print(f"Please pay {category_set_price}$")

else:
    print("Sorry but you are to short :(")