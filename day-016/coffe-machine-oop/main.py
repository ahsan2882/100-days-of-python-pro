from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
items = menu.get_items()

is_machine_off = False


def get_order():
    global is_machine_off
    user_input = input(f"What would you like? ({items}): ")
    if user_input == "off":
        print("Machine is turning off")
        is_machine_off = True
        return
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input in items:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


while not is_machine_off:
    get_order()
