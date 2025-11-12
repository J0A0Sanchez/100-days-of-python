"""Simple if else exercise to check if someone over or under
120cs of height can go in rollercoaster.

But include another condition based on age:
>=18 pay 18
Between 12 - 18 pay 12
<12 pay 5"""

print("Welcome to the Rollercoaster!")
print("-"*30)
print("    Price List:\n"
      "• Adults (18 years and older): $18\n"
      "• Teenagers (12 to 17 years old): $12\n"
      "• Children (under 12 years old): $5")
print("-"*30)

height = int(input("What is your height in cm?: "))


if height >= 120:
    print("You can go in based on your height")

    age = int(input("What is your age?: "))

    if age >= 18:
        print("Please pay 18$")

    elif age >= 12 and age < 18:
        print("Please pay 12$")

    else:
        print("Please pay 7$")

else:
    print("Sorry but you are to short :(")