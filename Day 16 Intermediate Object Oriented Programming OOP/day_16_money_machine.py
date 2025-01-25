# Class for handling all money-related operations in the coffee machine
class MoneyMachine:
    # Class constants for currency and coin values
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,  # Quarter = $0.25
        "dimes": 0.10,     # Dime = $0.10
        "nickles": 0.05,   # Nickle = $0.05
        "pennies": 0.01    # Penny = $0.01
    }

    def __init__(self):
        """Initialize money machine with zero profit and received money"""
        self.profit = 0          # Total profit accumulated
        self.money_received = 0  # Current transaction amount

    def report(self):
        """Prints the current profit"""
        # Display current profit with currency symbol
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        # Calculate total from each type of coin inserted
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        # Process inserted coins
        self.process_coins()
        
        # Check if payment is sufficient
        if self.money_received >= cost:
            # Calculate and return change
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            # Update profit and reset money received
            self.profit += cost
            self.money_received = 0
            return True
        else:
            # Refund if payment insufficient
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
