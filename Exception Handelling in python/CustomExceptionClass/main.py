from bank_account import Bank
from Exception.exception import InsufficientFundsException

if __name__ == "__main__":
    account = Bank(10)

    try:
        print(account.withdraw(10))
    except InsufficientFundsException as e:
        print(e)
