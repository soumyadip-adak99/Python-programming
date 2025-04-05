class InsufficientFundsException(Exception):

    def __init__(self, amount: float):
        self.amount = amount

    def __str__(self):
        return "You don't have enough money"
