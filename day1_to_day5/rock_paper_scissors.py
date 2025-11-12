"""Rock, Paper, Scissors Game Module"""

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



while True:
    
    user_comand = int(input("Let's play rock, paper or scissors!!!\n" \
"Chose below:\n" \
"Rock = 0\n" \
"Paper = 1\n" \
"Scissors = 2\n" \
"Type 9 to quit.\n"))

    if user_comand == 9:
        print("Thanks for playing! 👋")
        break

    if user_comand == 0:
        print(f"You selected rock \n {rock}")
        computer = random.choice([rock, paper, scissors])
        if computer == rock:
            print(f'Computer selected rock{rock}')
            print('Draw  🤝 ')
        elif computer == paper:
            print(f'Computer selected paper{paper}')
            print('You lose 😢 ')
        elif computer == scissors:
            print(f'Computer selected scissors{scissors}')
            print('You win  🎉 ')

    elif user_comand == 1:
        print(f"You selected paper \n {paper}")
        computer = random.choice([rock, paper, scissors])
        if computer == rock:
            print(f'Computer selected rock{rock}')
            print('You win  🎉 ')
        elif computer == paper:
            print(f'Computer selected paper{paper}')
            print('Draw  🤝 ')
        elif computer == scissors:
            print(f'Computer selected scissors{scissors}')
            print('You lose 😢 ')

    elif user_comand == 2:
        print(f"You selected scissors \n {scissors}")
        computer = random.choice([rock, paper, scissors])
        if computer == rock:
            print(f'Computer selected rock{rock}')
            print('You lose 😢 ')
        elif computer == paper:
            print(f'Computer selected paper{paper}')
            print('You win  🎉 ')
        elif computer == scissors:
            print(f'Computer selected scissors{scissors}')
            print('Draw  🤝 ')

    else:
        print('Invalid comand - Try again')