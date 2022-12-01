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
}

isMachineOff = False
money_in_machine = 0.0


def generate_report():
    """generate a report of all the resources"""
    return {
        **resources,
        "Money": money_in_machine,
    }


def return_change(money):
    """return change to user"""
    print(f"Here is your ${money} in change")


def process_coins():
    """Process coins from user"""
    print("Please insert your coins.")
    num_quarters = int(input("How may quarters? "))
    num_dimes = int(input("How may dimes? "))
    num_nickels = int(input("How may nickels? "))
    num_pennies = int(input("How may pennies? "))
    total = num_quarters * 0.25 + num_dimes * 0.1 + num_nickels * 0.05 + num_pennies * 0.01
    return total


def check_resources(coffee_type):
    """check if machine has enough resources to dispense said coffee"""
    required_resources = MENU[coffee_type]["ingredients"]
    if resources["water"] < required_resources["water"]:
        print("Not enough water")
        return False
    if 'milk' in required_resources and resources["milk"] < required_resources["milk"]:
        print("Not enough milk")
        return False
    if resources["coffee"] < required_resources["coffee"]:
        print("Not enough coffee")
        return False
    return True


def add_money_to_machine(money):
    """add money for each coffee in the machine"""
    global money_in_machine
    money_in_machine += money


def make_coffee(coffee_type):
    """subtract resources"""
    required_resources = MENU[coffee_type]['ingredients']
    for ingredient in required_resources:
        resources[ingredient] -= required_resources[ingredient]
    print(f"Here is your {coffee_type}. Enjoy!")


def get_order():
    """Get the order from user"""
    global isMachineOff
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        print("Machine is turning off")
        isMachineOff = True
        return
    if user_input == "report":
        # TODO: 3. Print report of all resources
        print(resources)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_resources(user_input):
            money_inserted = process_coins()
            coffee_type = MENU[user_input]
            required_money = coffee_type['cost']
            if money_inserted < required_money:
                print("Sorry! not enough money. money refunded")
                return_change(money_inserted)
                return
            elif money_inserted > required_money:
                change = round(money_inserted - required_money, 2)
                return_change(change)
            add_money_to_machine(required_money)
            make_coffee(user_input)
    else:
        print("Not available in menu. Please choose again")


while not isMachineOff:
    get_order()
