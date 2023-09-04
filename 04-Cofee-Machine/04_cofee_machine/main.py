from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cofee_machine = CoffeeMaker()
machine_menu = Menu()
money_cal = MoneyMachine()

is_on = True

while is_on:
    CHOICE = str(input(f"What will you like to have today? ({machine_menu.get_items()}): "))
    if CHOICE == 'off':
        is_on = False
    elif CHOICE == "status":
        cofee_machine.report()
    elif CHOICE == "report":
        money_cal.report()
    else:
        drink = machine_menu.find_drink(CHOICE)
        if money_cal.make_payment(drink.cost) and cofee_machine.is_resource_sufficient(drink):
            cofee_machine.make_coffee(drink)