from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    machine = CoffeeMaker()
    cashbox = MoneyMachine()
    items = Menu()
    machine_on = True
    while machine_on:
        prompt = input(f"What would you like? ({items.get_items()}): ").lower()
        if prompt == "off":
            machine_on = False
        elif prompt == "report":
            machine.report()
            cashbox.report()
        else:
            drink = items.find_drink(prompt)
            pay = drink.cost
            print(drink)
            possible = machine.is_resource_sufficient(drink)
            if possible:
                paid = cashbox.make_payment(pay)
                if paid:
                    machine.make_coffee(drink)
                    print(f"Enjoy your {prompt}☕!")


coffee_machine()
