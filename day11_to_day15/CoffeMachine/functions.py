import pandas as pd
import time




def load_report(path):
    """loads a csv file and returns a dataframe"""
    try:
        report = pd.read_csv(path)
        return report
    except:
        print(f"Error: file not found in: {path}")


def save_report(dataframe, path):
    """saves a dataframe to a csv file"""
    try:
        dataframe.to_csv(path, index=False, header=True)
    except:
        print(f"Error: please check parameters")


def resources_checker(dataframe, recipes, product):
    """Function that check if there are enough resources to make the order"""
    # Set "resources" column as the index, so we can access quantities by ingredient name
    df_stock = dataframe.set_index("resources")
    
    # Convert the "qtt" column into a dictionary: stock[ingredient] = quantity
    stock = df_stock["qtt"].to_dict()
    
    # Get the ingredients required for the selected product
    ingredients = recipes[product]["ingredients"]

    # Loop through each ingredient and the amount required by the recipe
    for ing, required_amount in ingredients.items():
        # Get the available quantity from stock; default to 0 if the ingredient is missing
        available_amount = stock.get(ing, 0)
        # Check if there is enough of this ingredient
        if available_amount < required_amount:
            print(f"Not enough {ing}. Missing {required_amount - available_amount}.")
            return False  # Stop the check and return False if any ingredient is insufficient
        else:
            print(f"{ing}: OK (available {available_amount}, required {required_amount})")

    # If all ingredients are sufficient, return True
    return True


def process_coins(cost):
    """Function that process coins and returm total inserted"""
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.10
    NICKEL_VALUE = 0.05
    PENNY_VALUE = 0.01

    total_inserted = 0.0
    
    print("\nPlease insert coins.")
    print(f"The item cost is ${cost:.2f}.")

    while total_inserted < cost:

        try:
            quarters = int(input("How many quarters ($0.25)? "))
            dimes = int(input("How many dimes ($0.10)? "))
            nickles = int(input("How many nickles ($0.05)? "))
            pennies = int(input("How many pennies ($0.01)? "))
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")
            continue

        current_input = (quarters * QUARTER_VALUE) + \
                         (dimes * DIME_VALUE) + \
                         (nickles * NICKEL_VALUE) + \
                         (pennies * PENNY_VALUE)
        
        total_inserted += current_input

        if total_inserted < cost:
            remaining = cost - total_inserted
            print(f"Total inserted: ${total_inserted:.2f}. Remaining: ${remaining:.2f}.")

    if total_inserted > cost:
        print(f"You inserted ${total_inserted:.2f}. Your change is ${total_inserted-cost:.2f}")
        total_inserted -= (total_inserted-cost)
        
    print(f"\nCoin collection complete. Total inserted: ${total_inserted:.2f}")
    return total_inserted


def make_coffe(order, recipes, report, path):
    """Function that prepare the coffee selected and update the stock based on RECIPES"""
    print(f"Making: {order}")

    required_amount = recipes[order]
    product_cost = recipes[order]["cost"]

    new_report = report.set_index("resources")
    for ing, amount in required_amount["ingredients"].items():
        new_report.loc[ing,"qtt"] -= amount
    
    new_report.loc["money", "qtt"] += product_cost
    
    new_report = new_report.reset_index()
    save_report(new_report, path)
    time.sleep(2)
    print(f"{order} is ready. Enjoy!\n")
    

def edit_resources(report, path):
    """Function that edit stock"""
    df_stock = report.set_index("resources")
    stock = df_stock["qtt"].to_dict()
    
    print(f"Current resources {stock}")

    for i in stock:
        update = float(input(f"Please enter the amound of '{i}' you want to edit: "))
        stock[i] += update

    print(f"Updated stock: {stock}")

    new_report = pd.DataFrame.from_dict(stock, orient="index", columns=["qtt"])
    new_report = new_report.reset_index().rename(columns={"index": "resources"})

    save_report(new_report, path)






     
