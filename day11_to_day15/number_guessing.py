import random


def number_generator(n1, n2):
    """Randomly select a number between n1 and n2."""
    numbers = []
    for i in range (n1, n2+1):
        numbers.append(i)
        
    number = random.choice(numbers)
    return number


def difficulty(option):
    """Difficult level based on option"""
    if option == 'easy':
        return 10
    
    if option == 'hard':
        return 5


def game():
    print(r"""
    _   __                __                 ______                     _                ______                   
   / | / /_  ______ ___  / /_  ___  _____   / ____/_  _____  __________(_)___  ____ _   / ____/___ _____ ___  ___ 
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/  / / __/ __ `/ __ `__ \/ _ \
 / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  ) / / / / /_/ /  / /_/ / /_/ / / / / / /  __/
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/_/_/ /_/\__, /   \____/\__,_/_/ /_/ /_/\___/ 
                                                                            /____/                                """)
    print("Welcome to the number guessing game!")
    n1 = int(input("Select your start number: "))
    n2 = int(input("Select your end number: "))

    selected_number = number_generator(n1, n2)
    #print(selected_number)
    print(f"I'm thinking of a number between {n1} and {n2}!")


    option = ""
    while option not in ('easy', 'hard'):
        option = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        dif_level = difficulty(option)
        if option not in ('easy', 'hard'):
            print("Wrong option, try again!")


    while dif_level > 0:
        print(f"You have {dif_level} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess == selected_number:
            print("You win!")
            break
        if guess > selected_number:
            print("Too high!") 
        else:
            print("Too Low!")
        
        dif_level -= 1

        if dif_level == 0:
            print(f"You've run out of attempts! The number was {selected_number}.")



game()