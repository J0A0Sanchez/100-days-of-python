import random
import os

def even_odd(player1, player2):
    total = player1 + player2

    if total % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
    
def checker(results):
    winner = max(results, key=results.get)
    loser = min(results, key=results.get)
    if winner == loser:
        return "It's a draw!"
    else:
        return f"The overall winner is: {winner} with {results[winner]} wins!\nThe loser is: {loser} with {results[loser]}"
    
  



results = {}
numbers = [1,2,3,4,5,6,7,8,9,10]


player_name = str(input("What is your name? : "))
results[player_name] = 0
results["Computer"] = 0
plays = int(input("How many matches you wanna play? : "))

count_plays = 0

while count_plays < plays:
    player_choice = str(input("Your pick is 'EVEN' or 'ODD'? : ")).title()
    u_number = int(input("Pick a number between 0 and 10: "))
    c_number = random.choice(numbers)
    t_number = u_number + c_number
    print("-"*25)
    print(f"Computer choice is: {c_number}")
    print("-"*25)
    result = even_odd(u_number,c_number)
    print(f"Total is: {t_number} = {result}")



    if result == player_choice:
        print("You win this round!")
        results[player_name] += 1

    else:
        print("You lose this round!")
        results["Computer"] += 1


    print(results)
    count_plays += 1

print("-"*25)
print(checker(results))