"""Make a list of names and randomly print one."""

import random

names = ["João", "Maria", "Pedro", "Ana", "Lucas", "Carla",
          "Rafael", "Beatriz"]

# 1 option
print(random.choice(names))

# 2 option
selected_len = random.randint(0, len(names)-1)
selected_name =  names[selected_len]
print(selected_name)
