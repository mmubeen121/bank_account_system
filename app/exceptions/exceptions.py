class BankAccountError(Exception):
    """Base class for bank account exceptions"""
    pass


class InvalidNameError(BankAccountError):
    pass


class InvalidAmountError(BankAccountError):
    pass


class InsufficientBalanceError(BankAccountError):
    pass


class AccountNotFoundError(BankAccountError):
    pass
