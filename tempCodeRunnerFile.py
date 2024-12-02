class CoffeeDrink:
    """Class representing a coffee drink."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class Menu:
    """Class representing the menu of drinks."""
    def __init__(self):
        self.drinks = [
            CoffeeDrink("Espresso", water=50, milk=0, coffee=18, cost=1.5),
            CoffeeDrink("Latte", water=200, milk=150, coffee=24, cost=2.5),
            CoffeeDrink("Cappuccino", water=250, milk=100, coffee=24, cost=3.0),
        ]

    def get_items(self):
        return ", ".join(drink.name for drink in self.drinks)

    def find_drink(self, name):
        for drink in self.drinks:
            if drink.name.lower() == name.lower():
                return drink
        return None


class CoffeeMachine:
    """Class representing a coffee machine."""
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0.0
        self.menu = Menu()
        self.is_on = True

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money:.2f}")

    def is_resource_sufficient(self, drink):
        """Checks if resources are sufficient for the selected drink."""
        if self.water < drink.water:
            print("Sorry, not enough water.")
            return False
        if self.milk < drink.milk:
            print("Sorry, not enough milk.")
            return False
        if self.coffee < drink.coffee:
            print("Sorry, not enough coffee.")
            return False
        return True

    def process_payment(self, cost):
        """Processes payment and checks if it's sufficient."""
        print(f"The cost is ${cost:.2f}. Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total = quarters + dimes + nickels + pennies

        if total < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = total - cost
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            self.money += cost
            return True

    def make_coffee(self, drink):
        """Deducts resources to make coffee."""
        self.water -= drink.water
        self.milk -= drink.milk
        self.coffee -= drink.coffee
        print(f"Here is your {drink.name}. Enjoy!")

    def start(self):
        """Starts the coffee machine."""
        while self.is_on:
            options = self.menu.get_items()
            choice = input(f"What would you like? ({options}): ").lower()

            if choice == "off":
                self.is_on = False
                print("Turning off the coffee machine. Goodbye!")
            elif choice == "report":
                self.report()
            else:
                drink = self.menu.find_drink(choice)
                if drink:
                    if self.is_resource_sufficient(drink):
                        if self.process_payment(drink.cost):
                            self.make_coffee(drink)
                else:
                    print("Sorry, we don't have that drink.")


# Run the Coffee Machine
machine = CoffeeMachine()
machine.start()
