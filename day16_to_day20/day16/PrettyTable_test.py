
from prettytable import PrettyTable

table = PrettyTable()

pokemons = {
    "Pikachu": "Electric",
    "Charmander": "Fire",
    "Bulbasaur": "Grass / Poison",
    "Squirtle": "Water",
    "Eevee": "Normal",
    "Jigglypuff": "Normal / Fairy",
    "Meowth": "Normal",
    "Psyduck": "Water",
    "Snorlax": "Normal",
    "Gengar": "Ghost / Poison",
    "Dragonite": "Dragon / Flying",
    "Lucario": "Fighting / Steel",
    "Mewtwo": "Psychic",
    "Charizard": "Fire / Flying",
    "Gyarados": "Water / Flying"
}


table.add_column("Pokemons", [key for key in pokemons])
table.add_column("Type", [values for values in pokemons.values()])

table.align = "l"

print(table)