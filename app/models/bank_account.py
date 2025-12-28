class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder_name: str, opening_balance: float):
        # validating the data
        if not isinstance(account_holder_name, str) or not account_holder_name.strip():
            raise ValueError("Account holder name must be a non-empty string")
        if not isinstance(opening_balance, (int, float)) or opening_balance < 0:
            raise ValueError("Opening balance must be a non-negative number")

        BankAccount.account_counter += 1
        self.account_no = BankAccount.account_counter
        self.account_holder = account_holder_name.strip()
        self.balance = float(opening_balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")

        # updating balance
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        # updating balance
        self.balance -= amount

    def get_balance(self):
        return self.balance
