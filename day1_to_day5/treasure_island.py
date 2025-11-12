# Treasure Island Adventure Game - create a program based on the given flowchart.

print("Welcome to Treasure Island - Your mission is to find the treasure.")

i1 = input("Left or Right? [L/R]: ").upper()

if i1 != "L":
    print("Fall into a hole, Game Over! :(")

i2 = input("Swim or Wait? [S/W]: ").upper()

if i2 != "W":
    print("Attached by trout, Game Over! :(")

i3 = input("Which door? Red, Blue or Yellow? [R/B/Y]: ").upper()

if i3 == "R":
    print("Burned by fire, Game over! :(")

elif i3 == "B":
    print("Eaten by beasts, Game over! :(")

elif i3 == "Y":
    print("Congrats! You won!")

else: 
    print("Game Over!!!")