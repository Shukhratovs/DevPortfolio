MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

base_water = 400
base_milk = 300
base_coffee = 100
base_money = 0

is_on = True

while is_on:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if users_choice == 'report':
        print(f"Water: {base_water}ml \nMilk: {base_milk}ml \nCoffee: {base_coffee}g \nMoney: ${base_money}")
    if users_choice == 'espresso':
        if base_water < 50 or base_coffee < 18:
            print("Sorry, there is not enough ingredient to make this coffee.")
        else:
            base_water -= 50
            base_coffee -= 18
            base_money += 1.5
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = round((quarter/4), 1) + round((dimes/10), 1) + round((nickles/20), 1) + round((pennies/100), 1)
            if total > 1.5:
                print(f"Here is ${round((total - 3.0), 1)} in change.")
                print('Here is your espresso ☕️. Enjoy!')
            elif total < 1.5:
                print("Sorry that's not enough money. Money refunded.")
            elif total == 1.5:
                print(f"Here is ${round((total - 3.0), 1)} in change.")
                print('Here is your espresso ☕️. Enjoy!')

    elif users_choice == 'latte':
        if base_water < 200 or base_milk < 150 or base_coffee < 24:
            print("Sorry, there is not enough ingredient to make this coffee.")
        else:
            base_water -= 200
            base_milk -= 150
            base_coffee -= 24
            base_money += 2.5
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = round((quarter/4), 1) + round((dimes/10), 1) + round((nickles/20), 1) + round((pennies/100), 1)
            if total > 1.5:
                print(f"Here is ${round((total - 3.0), 1)} in change.")
                print('Here is your latte ☕️. Enjoy!')
            elif total < 1.5:
                print("Sorry that's not enough money. Money refunded.")
            elif total == 1.5:
                print(f"Here is ${round((total - 3.0), 1)} in change.")
                print('Here is your latte ☕️. Enjoy!')

    elif users_choice == 'cappuccino':
        if base_water < 250 or base_milk < 100 or base_coffee < 24:
            print("Sorry, there is not enough ingredient to make this coffee.")
        else:
            base_water -= 250
            base_milk -= 100
            base_coffee -= 24
            base_money += 3.0
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = round((quarter/4), 1) + round((dimes/10), 1) + round((nickles/20), 1) + round((pennies/100), 1)
            if total > 1.5:
                print(f"Here is ${round((total - 3.0), 1)} in change.")
                print('Here is your cappuccino ☕️. Enjoy!')
            elif total < 1.5:
                print("Sorry that's not enough money. Money refunded.")
            elif total == 1.5:
                print(f"Here is ${round((total - 3.0), 1)} in change.")
                print('Here is your cappuccino ☕️. Enjoy!')

    elif users_choice == 'off':
        is_on = False
