from stencil import *

def test_initialization():
    account = BankAccount("123456789", 1000.0)
    assert account.get_balance() == 1000.0, "Initial balance should be 1000.0"
    
    # Test edge cases
    try:
        BankAccount("", 100.0)
        assert False, "Account number cannot be empty"
    except ValueError:
        pass
    
    try:
        BankAccount("123456789", -100.0)
        assert False, "Initial balance cannot be negative"
    except ValueError:
        pass

def test_deposit():
    account = BankAccount("123456789", 1000.0)
    account.deposit(500.0)
    assert account.get_balance() == 1500.0, "Balance should be 1500.0 after deposit"
    
    # Test edge cases
    try:
        account.deposit(-500.0)
        assert False, "Deposit amount cannot be negative"
    except ValueError:
        pass

def test_withdraw():
    account = BankAccount("123456789", 1000.0)
    account.withdraw(500.0)
    assert account.get_balance() == 500.0, "Balance should be 500.0 after withdrawal"
    
    # Test edge cases
    try:
        account.withdraw(-500.0)
        assert False, "Withdrawal amount cannot be negative"
    except ValueError:
        pass
    
    try:
        account.withdraw(1000.0)
        assert False, "Should not allow withdrawal exceeding balance"
    except ValueError:
        pass

def test_transfer():
    account1 = BankAccount("123456789", 1000.0)
    account2 = BankAccount("987654321", 500.0)
    account1.transfer(200.0, account2)
    assert account1.get_balance() == 800.0, "Balance should be 800.0 after transfer"
    assert account2.get_balance() == 700.0, "Balance should be 700.0 after transfer"
    
    # Test edge cases
    try:
        account1.transfer(-200.0, account2)
        assert False, "Transfer amount cannot be negative"
    except ValueError:
        pass
    
    try:
        account1.transfer(1000.0, account2)
        assert False, "Should not allow transfer exceeding balance"
    except ValueError:
        pass
    
    try:
        account1.transfer(200.0, "Not an account")
        assert False, "Recipient must be a BankAccount instance"
    except ValueError:
        pass

def test_apply_interest():
    account = BankAccount("123456789", 1000.0)
    account.apply_interest(0.05)
    assert account.get_balance() == 1050.0, "Balance should be 1050.0 after applying 5% interest"
    
    # Test edge cases
    try:
        account.apply_interest(-0.05)
        assert False, "Interest rate cannot be negative"
    except ValueError:
        pass

    try:
        account.apply_interest(0.0)
        assert False, "Interest rate cannot be zero"
    except ValueError:
        pass