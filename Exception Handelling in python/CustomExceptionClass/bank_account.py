from Exception.exception import InsufficientFundsException


class Bank:

    def __init__(self, amount: float):
        self.balance = amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsException(amount)
        self.balance -= amount
        return f"Withdrawn: {amount}. Remaining balance: {self.balance}"

    def get_balance(self) -> float:
        return self.balance
