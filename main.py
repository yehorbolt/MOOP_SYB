from Account.Account import *
from Card.Checking import Checking
from Card.Credit import Credit as credit
from Transfer.Transaction import *
from ConnectToDB import ConnectToDb as con

""" Main file that start everything """
if __name__ == '__main__':
    """ Creates connection to database """
    con.db_connect()

    """ Creating new User """
    user = User("Testing", "11111111", 30000, False)
    print("User:")
    print(user)
    print()

    """ Changing user password """
    """ Error as password is less than 8 symbols """
    try:
        user.changePassword("1234567")
    except Exception as e:
        print(e)

    """ Success """
    user.changePassword("12345678")
    print("User:")
    print(user)
    print()

    """ Creating user's account """
    account = Account("Taras", "Shevchenko", "workless", user.id, False)
    print("Account:")
    print(account)
    print()

    """ Changing name and status of the account """
    account.changeName("TarasGrygorovych")
    account.changeStatus("working")
    print("Account:")
    print(account)
    print()

    """ Creating checking card """
    checking = Checking(1111, "checking", account.id, False)
    print("Checking Card:")
    print(checking)
    print()

    """ Make a transaction with 0 money """
    try:
        checking.makeTransaction(601226214, 2000)
    except Exception as e:
        print(e)

    """ Withdraw with 0 money """
    try:
        checking.withdraw(2000)
    except Exception as e:
        print(e)

    """ Put money user has on the card """
    """ Let's put more than the user has """
    try:
        checking.putMoney(user.id, 2000000)
    except Exception as e:
        print(e)
    print("User:")
    print(user)
    print()

    """ Let's put money that the user has on the card """
    checking.putMoney(user.id, 10000)
    print("Checking:")
    print(checking)
    print()

    """Let's make a transaction """
    checking.makeTransaction(601226214, 2000)
    print("Checking:")
    print(checking)
    print()

    """ Let's withdraw some money """
    checking.withdraw(2000)
    print("Checking:")
    print(checking)
    print("User:")
    print(user)
    print()

    """ Put the card limit """
    checking.changeLimit(4000)
    print("Checking:")
    print(checking)
    print()

    """ Not let's make a transaction on amount that is higher than the limit """
    try:
        checking.makeTransaction(601226214, 4000)
    except Exception as e:
        print(e)
    print("Checking:")
    print(checking)
    print()

    """ Let's create a credit card """
    credit = credit(2222, "credit", account.id, False)
    print("Credit:")
    print(credit)
    print()

    """ Let's do impossible things now """
    try:
        credit.withdraw(2000)
    except Exception as e:
        print(e)
    print("Credit:")
    print(credit)
    print()

    try:
        credit.makeTransaction(601226214, 2000)
    except Exception as e:
        print(e)
    print("Credit:")
    print(credit)
    print()

    """ Let's change the credit limit """
    credit.changeLimit(9000)
    print("Credit:")
    print(credit)
    print()

    """ Now, let's take a credit """
    try:
        credit.takeCredit(89500)
    except Exception as e:
        print(e)
    print("Credit:")
    print(credit)
    print()

    """ Change limit again """
    credit.changeLimit(30000)
    print("Credit:")
    print(credit)
    print()

    """ Let's take a credit """
    credit.takeCredit(10000)
    print("Credit:")
    print(credit)
    print()

    """ Make a transaction """
    credit.makeTransaction(601226214, 2000)
    print("Credit:")
    print(credit)
    print()

    """ Withdraw money """
    credit.withdraw(2000)
    print("Credit:")
    print(credit)
    print()

    """ Put money some money to decrease left to pay amount"""
    credit.putMoney(user.id, 3000)
    print("Credit:")
    print(credit)
    print()

    """ Closes database connection """
    con.db_close()

    """
    con.db_connect()    
    """

    """
    u = User("test", "123456789", 5000, True)
    ac = Account("Test", "Testov", "working", u.id, True)
    ch = Checking(1111, "checking", ac.id, True)

    try:
        ch.putMoney(u.id, 10000)
    except Exception as e:
        print(e)

    try:
        ch.putMoney(u.id, 3000)
    except Exception as e:
        print(e)

    try:
        ch.makeTransaction(601226214, 25000)
    except Exception as e:
        print(e)

    try:
        ch.makeTransaction(601226214, 2500)
    except Exception as e:
        print(e)

    try:
        ch.withdraw(100000)
    except Exception as e:
        print(e)

    try:
        ch.withdraw(500)
    except Exception as e:
        print(e)
    """

    """
    u = User("test", "123456789", 5000, True)
    ac = Account("Test", "Testov", "working", u.id, True)
    cr = credit(1111, "credit", ac.id, True)

    try:
        cr.takeCredit(100000)
    except Exception as e:
        print(e)
    print(cr)

    cr.changeLimit(20000)
    print(cr)

    try:
        cr.takeCredit(float (40000))
    except Exception as e:
        print(e)

    cr.changeLimit(40000)
    print(cr)

    try:
        cr.takeCredit(40000)
    except Exception as e:
        print(e)
    print(cr)

    try:
        cr.putMoney(u.id, 10000)
    except Exception as e:
        print(e)
    print(cr)

    try:
        cr.putMoney(u.id, 3000)
    except Exception as e:
        print(e)
    print(cr)

    try:
        cr.makeTransaction(601226214, 250000)
    except Exception as e:
        print(e)

    try:
        cr.makeTransaction(601226214, 25000)
    except Exception as e:
        print(e)
    print(cr)

    try:
        cr.withdraw(1000000)
    except Exception as e:
        print(e)

    try:
        cr.withdraw(5000)
    except Exception as e:
        print(e)
    print(cr)
    try:
        cr.takeCredit(10000)
    except Exception as e:
        print(e)
    print(cr)

    
    u = User("test", "123456789", 5000, True)
    ac = Account("Test", "Testov", "working", u.id, True)
    s = Savings(1111, "savings", ac.id, True)

    print(s)

    try:
        s.putMoney(u.id, 3000)
    except Exception as e:
        print(e)

    print(s)

    try:
        s.withdraw(3000)
    except Exception as e:
        print(e)

    print(s)
    """

