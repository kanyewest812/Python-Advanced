class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")

        elif amount > self.__balance:
            print("Not enough balance")

        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Asya", 80000)

acc.deposit(15000)
acc.withdraw(30000)
acc.withdraw(70000)   # should fail
acc.deposit(-2000)     # should fail

print("Current balance:", acc.get_balance())
