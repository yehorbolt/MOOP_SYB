from User.User import *
from Account.Account import *
from ATM.ATM import *
from Bank.Bank import *
from Card.Checking import Checking
from Card.Credit import Credit as credit
from Card.Savings import *
from Transfer.Transaction import *
from Transfer.Credit import *
from Transfer.Daemon import *

from ConnectToDB import ConnectToDb as con

def createBasicData(self):
    pass
    #u =
    #hs = Account("Hryhorii", "Skovoroda", "working", 1, False)
    #c1 = Card(1111, "checking", 1, False)

""" Main file that start everything """
if __name__ == '__main__':
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

    """
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


