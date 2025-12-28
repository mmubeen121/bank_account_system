from app.models.bank_account import BankAccount
from app.exceptions.exceptions import BankAccountError, AccountNotFoundError


class AccountManager:
    def __init__(self):
        self.accounts = []

    # creating bank account
    def create_account(self, account_holder_name, opening_balance):
        account = BankAccount(account_holder_name, opening_balance)
        self.accounts.append(account)
        return account

    def find_account(self, account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account
        return None

    def account_to_deposit(self,account_no, amount):
        account = self.find_account(account_no)
        if not account:
            raise AccountNotFoundError("Account not found")
        account.deposit(amount)

    def account_to_withdraw(self,account_no, amount):
        account = self.find_account(account_no)
        if not account:
            raise AccountNotFoundError("Account not found")
        account.withdraw(amount)

    def get_account_detail(self, account_no):
        account = self.find_account(account_no)
        if not account:
            raise AccountNotFoundError("Account not found")

        return {
            "account_no": account.account_no,
            "holder_name": account.holder_name,
            "balance": account.get_balance()
        }
