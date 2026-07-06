import re

class Account:
    def __init__(self, acc_no, balance):
        if re.fullmatch(r"\d{8}", acc_no):
            self.acc_no = acc_no
        else:
            print("Invalid Account Number")
            return

        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Balance:", self.__balance)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


class SavingsAccount(Account):
    def withdraw(self, amount):
        print("Savings Account")
        super().withdraw(amount)


class CurrentAccount(Account):
    def withdraw(self, amount):
        print("Current Account")
        super().withdraw(amount)


acc = SavingsAccount("12345678", 10000)
acc.withdraw(3000)

print("Final Balance:", acc.get_balance())