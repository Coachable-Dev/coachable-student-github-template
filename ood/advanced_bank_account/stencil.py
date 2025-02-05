class BankAccount:
    '''
    Represents a bank account with basic operations.

    - The account number should be a non-empty string.
    - The balance should be initialized as a non-negative float.

    Edge Cases:
    - Raise a ValueError if the account number is empty.
    - Raise a ValueError if the initial balance is negative.
    '''
    def __init__(self, account_number: str, balance: float) -> None:
        # Initialize private instance variables for account number and balance
        pass

    '''
    Deposits a specified amount into the account.

    - The deposit amount must be a positive float.
    - The balance should be updated and rounded to 4 decimal places.

    Edge Cases:
    - Raise a ValueError if the deposit amount is not positive.
    '''
    def deposit(self, amount: float) -> None:
        # Method to deposit money into the account
        pass

    '''
    Withdraws a specified amount from the account, ensuring sufficient balance.

    - The withdrawal amount must be a positive float.
    - Overdrafts (withdrawing more than the balance) should not be allowed.
    - The balance should be updated and rounded to 4 decimal places.

    Edge Cases:
    - Raise a ValueError if the withdrawal amount is not positive.
    - Raise a ValueError if the withdrawal amount exceeds the current balance (no overdrafts allowed).
    '''
    def withdraw(self, amount: float) -> None:
        # Method to withdraw money from the account, ensuring sufficient balance
        pass

    '''
    Returns the current balance of the account.

    - The balance should be returned as a float rounded to 4 decimal places.
    '''
    def get_balance(self) -> float:
        # Method to return the current balance
        pass

    '''
    Transfers a specified amount to another BankAccount instance.

    - The transfer amount must be a positive float.
    - Ensure there are sufficient funds in the account to make the transfer.
    - Update the balance in both accounts, rounding to 4 decimal places.

    Edge Cases:
    - Raise a ValueError if the transfer amount is not positive.
    - Raise a ValueError if the transfer amount exceeds the current balance (no overdrafts allowed).
    - Raise a ValueError if the recipient is not a BankAccount instance.
    '''
    def transfer(self, amount: float, recipient: 'BankAccount') -> None:
        # Method to transfer money to another BankAccount instance
        pass

    '''
    Applies an interest rate to the current balance.

    - The interest rate should be a positive float, representing a percentage (e.g., 5% as 0.05).
    - The balance should be updated by applying the interest rate and then rounded to 4 decimal places.

    Edge Cases:
    - Raise a ValueError if the interest rate is not positive.
    '''
    def apply_interest(self, interest_rate: float) -> None:
        # Method to apply interest to the current balance
        pass