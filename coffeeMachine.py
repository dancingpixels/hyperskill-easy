# the coffee machine has $550, 400 ml of water, 540 ml of milk, 
# 120 g of coffee beans, and 9 disposable cups.

# The state of the coffee machine
money = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups =  9

def coffee_machine_stats():
    print(str(water)," of water")
    print(str(milk)," of milk")
    print(str(coffee_beans), " of coffee beans")
    print(str(disposable_cups)," of disposable cups")
    print('$'+str(money)," of money")
    print()

def buy():
    # choose one of three types of coffee that the coffee machine can make: 
    # espresso, latte, or cappuccino.
    # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. 
    # It costs $4.
    # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans.
    # It costs $7.
    # And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, 
    # and 12 g of coffee. It costs $6.

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()

    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money

    if choice == "1":
        if water < 250:
            print("Sorry, not enough water!")
        elif coffee_beans < 16:
            print("Sorry, not enough cofee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            print()
            water -= 250
            coffee_beans -= 16
            money += 4
            disposable_cups -=1

    elif choice == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif coffee_beans < 20:
            print("Sorry, not enough cofee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            print()
            water -= 350
            milk -= 75
            coffee_beans -=20
            money += 7
            disposable_cups -=1
    
    elif choice == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif milk < 10:
            print("Sorry, not enough milk!")
        elif coffee_beans < 12:
            print("Sorry, not enough cofee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            print()
            water -= 200
            milk -= 100
            coffee_beans -=12
            money += 6
            disposable_cups -=1

    elif choice == "back":
        start_up

    else:
        exit(0)

def fill():
    print("Write how many ml of water do you want to add:")
    fill_water = int(input())

    print("Write how many ml of milk do you want to add:")
    fill_milk = int(input())

    print("Write how many grams of coffee beans do you want to add:")
    fill_coffee = int(input())

    print("Write how many disposable cups of coffee do you want to add:")
    fill_cups = int(input())
    print()

    global water
    global milk
    global coffee_beans
    global disposable_cups

    water += fill_water
    milk += fill_milk
    coffee_beans += fill_coffee
    disposable_cups += fill_cups

def take():
    global money
    print("I give you $", str(money))
    money -= money
    print()

def start_up():

    while True:

        print("Write action (buy, fill, take, remaining, exit):")
        action = input()

        if action == 'take':
            take()

        elif action == 'fill':
            fill()

        elif action == 'buy':
            buy()

        elif action == 'remaining':
            coffee_machine_stats()

        elif action == 'exit':
            break

        else:
            exit(0)

start_up()
