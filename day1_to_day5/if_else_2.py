"""Simple if else exercise to check if someone over or under
120cs of height can go in rollercoaster.

But include another condition if the person is over 18 years
pay 12$ or <=18 pay 7$"""

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?: "))
age = int(input("What is your age?: "))

if height >= 120:
    print("You can go in based on your height")
    if age >= 18:
        print("Please pay 18$")
    
    else:
        print("Please pay 7$")

else:
    print("Sorry but you are to short :(")