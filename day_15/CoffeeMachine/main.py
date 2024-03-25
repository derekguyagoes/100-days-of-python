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
    "water": 000,
    "milk": 000,
    "coffee": 000,
    "money": 0.0
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

    if len(missing_ingredients) > 0:
        return False, missing_ingredients
    else:
        return True


# TODO:1 Prompt 1/2
# TODO:2 turn off 1/1
# TODO:3 print report 1/1
# TODO:4 check sufficient resources 3/3
# TODO:5 process coins 0/3
# TODO:6 check transaction successful 0/3
# TODO:7 make coffee 0/2

RUNNING = True
STOP = False

making_coffee = RUNNING

while making_coffee:

    desire = "espresso"  # input("What would you like? (Espresso/Latte/Cappuccino \n").lower()

    if desire == "r" or desire == "report":
        print(generate_report())
    elif desire == "off":
        print("Good bye")
        making_coffee = STOP
    else:
        ready, missing_item = check_resources(desire)
        if ready:
            print("making drink")
        else:
            for missing in missing_item:
                print(f"missing {missing}")

            making_coffee = STOP
