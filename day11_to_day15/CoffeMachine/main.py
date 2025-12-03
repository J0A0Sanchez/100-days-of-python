from functions import load_report, save_report, resources_checker, process_coins, make_coffe, edit_resources
import time

resources_path = 'C:\\Python Cursos\\100 Days of Code The Complete Python Pro Bootcamp\\day11_to_day15\\CoffeMachine\\resources.csv'

RECIPES = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}



machine_on = True
possible_options = "espresso", "latte" ,"cappuccino", "off", "report", "edit"

while machine_on:
    order =  ""
    while order not in possible_options:
        order = str(input("What would you like? (espresso/latte/cappuccino):")).strip().lower()
        if order not in possible_options:
            print("Invalid product, please try again!")

    if order == "off":
        machine_on = False
    
    elif order == "report":
        report = load_report(resources_path)
        print(report)

    elif order == "edit":
        edit_resources(load_report(resources_path), resources_path)
        
    elif order in RECIPES:
        print(f"Check resources for: {order}\n")
        time.sleep(2)
        availability = resources_checker(load_report(resources_path), RECIPES, order)
        if availability == True:
            cost = RECIPES[order]["cost"]
            coins = process_coins(cost)
            time.sleep(1)
            make_coffe(order, RECIPES, load_report(resources_path), resources_path)


print("Thank you! Turning off")