"""Request: Pizza size: S, M or L
Pepperoni topping: Y or N
Extra cheese: Y or N"""

"""Print the final bill based on the user's choices and prices
of each size of pizza and additional toppings. 

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: +$1"""

print("-"*35)
print("Welcome to Python Pizza Deliveries!")
print("-"*35)

#prices 
s_pizza = 15
m_pizza = 20
l_pizza = 25
pep_s_pizza = 2
pep_ml_pizza = 3
ex_cheese = 1
final_pizza = 0

#pizza style
pizza_size = input("What is the pizza size? (S, M or L): ").upper()
pep_top = input("Do you want pepperoni topping? [Y/N]: ").upper()
cheese_top = input("Do you want extra cheese? [Y/N]: ").upper()

if pizza_size == "S":
    final_pizza = s_pizza
elif pizza_size == "M":
    final_pizza = m_pizza
elif pizza_size == "L":
    final_pizza = l_pizza

if pep_top == "Y":
    if pizza_size == "S":
        final_pizza += pep_s_pizza
    else:
        final_pizza += pep_ml_pizza

if cheese_top == "Y":
    final_pizza += ex_cheese

print(f"Final Pizza price: ${final_pizza}")