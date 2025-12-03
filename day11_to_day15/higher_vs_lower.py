import random

art_higher_lower = r""""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/                                   
"""
art_vs = """          
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
                       
"""

data = [
    {
        "name": "Cristiano Ronaldo",
        "followers": 612,
        "description": "Football player",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "followers": 492,
        "description": "Football player",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "followers": 430,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "followers": 400,
        "description": "TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "followers": 397,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Ariana Grande",
        "followers": 380,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "followers": 364,
        "description": "TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Beyoncé",
        "followers": 319,
        "description": "Musician and businesswoman",
        "country": "United States"
    },
    {
        "name": "Khloé Kardashian",
        "followers": 310,
        "description": "TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Taylor Swift",
        "followers": 282,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Neymar",
        "followers": 218,
        "description": "Football player",
        "country": "Brazil"
    },
    {
        "name": "National Geographic",
        "followers": 290,
        "description": "Magazine and documentary channel",
        "country": "United States"
    },
    {
        "name": "Virat Kohli",
        "followers": 264,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Jennifer Lopez",
        "followers": 254,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Zendaya",
        "followers": 185,
        "description": "Actress",
        "country": "United States"
    },
]




score = 0
entity_A = random.choice(data)

should_continue = True
while should_continue:
    print(f"Compara A: {entity_A["name"]}, {entity_A["description"]}, from {entity_A["country"]}.")
    print(art_vs)

    while True:
        entity_B = random.choice(data)
        if entity_B == entity_A:
            continue
        else:
            break  
        
    print(f"Against B: {entity_B["name"]}, {entity_B["description"]}, from {entity_B["country"]}.")

    user_choice = ""
    while user_choice not in ("A",  "B"):
        user_choice = str(input("\nWho has more followers? Type 'A' or 'B': ")).strip().upper()
        if user_choice not in ("A", "B"):
            print("Invalid Input, Try again")

    if entity_A["followers"] > entity_B["followers"]:
        correct_choice = 'A'
    else:
        correct_choice = 'B'

    if user_choice == correct_choice:
        score += 1
        entity_A = entity_B 
        print(f"\nYou are right! Current score: {score}")

    else:
        print(f"\nSorry, that's wrong!")
        print(f"The correct answer was '{correct_choice}'.")
        print(f"'A' had {entity_A['followers']}M followers and 'B' had {entity_B['followers']}M followers.")
        print(f"Final score: {score}")
        should_continue = False