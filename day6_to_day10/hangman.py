HANGMAN_PICS = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

word_list = [
    "banana",
    "carrot",
    "computer",
    "elephant",
    "sunflower",
    "python",
    "programming",
    "pineapple",
    "astronaut",
    "passionfruit",
]

import random

picked_word = random.choice(word_list).upper()
#print(picked_word)

size_word = []

for i in range(0, len(picked_word)):
    size_word.append('_')
for i in size_word:
    print(i,end='')
print('')

c = 0  

while c < len(HANGMAN_PICS):
  
  guess = str(input('Guess a letter: ')).upper()
  
  if guess in picked_word:
      print(guess)
      for i in range(len(picked_word)):
          if picked_word[i] == guess:
              size_word[i] = guess
      for i in size_word:
        print(i,end='')
      print('')

  else:
      c += 1
      print(HANGMAN_PICS[c-1])    
      print(i,end='')
      print('')
     

  if "_" not in size_word:
      print(f'The word is: {picked_word}')
      print("You win!")
      break
  
else:
    print(HANGMAN_PICS[-1])
    print(f'The word is: {picked_word}')
    print("Game Over!")