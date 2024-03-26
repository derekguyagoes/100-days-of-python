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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.5
}

MENU_LIST = {
    "l": "latte",
    "e": "espresso",
    "c": "cappuccino"
}


def generate_report():
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.capitalize()}: {resources[resource]}g")
        elif resource == "money":
            print(f"{resource.capitalize()}: ${resources[resource]}")


def check_resources(drink_choice):
    drink_recipe_ingredients = MENU[drink_choice]['ingredients']
    missing_ingredients = []
    for ingredient in dict(resources.items()):
        if ingredient in drink_recipe_ingredients:
            if resources[ingredient] < drink_recipe_ingredients[ingredient]:
                missing_ingredients.append(ingredient)
        else:
            continue

    return len(missing_ingredients) == 0, missing_ingredients


def process_coins():
    q = float(input("How many quarters?: ")) * 0.25
    d = float(input("How many dimes?: ")) * 0.1
    n = float(input("How many nickles?: ")) * 0.05
    p = float(input("How many pennies?: ")) * 0.01

    total = q + d + n + p
    return total


# TODO:1 Prompt 1/2
# TODO:2 turn off 1/1
# TODO:3 print report 1/1
# TODO:4 check sufficient resources 3/3
# TODO:5 process coins 3/3
# TODO:6 check transaction successful 3/3
# TODO:7 make coffee 2/2

RUNNING = True
STOP = False

making_coffee = RUNNING


def make_drink(drink_choice):
    drink_recipe_ingredients = MENU[drink_choice]['ingredients']
    for ingredient in dict(resources.items()):
        if ingredient in drink_recipe_ingredients:
            resources[ingredient] -= drink_recipe_ingredients[ingredient]
        else:
            continue


while making_coffee:

    choice = input("What would you like? (Espresso/Latte/Cappuccino \n").lower()

    if choice == "r" or choice == "report":
        print(generate_report())
    elif choice == "off":
        print("Good bye")
        making_coffee = STOP
    else:
        desire = MENU_LIST[choice]
        ready, missing_item = check_resources(desire)
        if ready:
            total_amount_received = process_coins()
            desireds_cost = MENU[desire]['cost']
            if total_amount_received >= desireds_cost:
                if total_amount_received > desireds_cost:
                    change_due = total_amount_received - desireds_cost
                    if change_due < -0.01:
                        print("Not enough change")
                        making_coffee = STOP
                    else:
                        resources['money'] += total_amount_received
                        resources['money'] -= change_due
                        if change_due > 0:
                            print(f" here is {change_due:.2f} dollars in change")
                print("making drink")
                make_drink(desire)
                print(f"Here is your {desire}. Enjoy!")
                generate_report()
            else:
                print("Sorry that's not enough. Money refunded")
        else:
            for missing in missing_item:
                print(f"missing {missing}")

            making_coffee = STOP
