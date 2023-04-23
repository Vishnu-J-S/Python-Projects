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

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def check(item):
    req = MENU[item]["ingredients"]
    for i in req:
        if req[i] >= resources[i]:
            print(f"Not enough {i}")
            return False
        elif req[i] < resources[i]:
            return True


def make_coffe(item):
    req = MENU[item]["ingredients"]
    for i in req:
        resources[i] -= req[i]
    print(f"Enjoy your {item}☕!")
    return


def bill(item):
    cost = MENU[item]["cost"]
    print("Please insert coins:")
    no_q = float(input("Enter the no. of quarters: "))
    no_d = float(input("Enter the no. of dimes: "))
    no_n = float(input("Enter the no. of nickels: "))
    no_p = float(input("Enter the no. of pennies: "))
    amt_q = no_q * QUARTER
    amt_d = no_d * DIME
    amt_n = no_n * NICKEL
    amt_p = no_p * PENNY
    payment = amt_q + amt_d + amt_n + amt_p
    change = round(payment - cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
        return True
    elif change == 0:
        print("No change to be given.")
        return True
    elif change < 0:
        print("Payment less than price.Money refunded")
        return False


def coffee_machine():
    money = 0
    machine_on = True
    while machine_on:
        prompt = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
        if prompt == "off":
            machine_on = False
        elif prompt == "report":
            print(f"Water:{resources['water']} ml")
            print(f"Milk:{resources['milk']} ml")
            print(f"Coffee:{resources['coffee']} gm")
            print(f"Money: ${money}")
        else:
            possible = check(prompt)
            if possible:
                paid = bill(prompt)
                money += MENU[prompt]["cost"]
                if paid:
                    make_coffe(prompt)
    return


coffee_machine()
