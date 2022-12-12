from User.User import *
from Account.Account import *
from ATM.ATM import *
from Bank.Bank import *
from Card.Checking import Checking
from Card.Credit import *
from Card.Savings import *
from Transfer.Transaction import *
from Transfer.Credit import *
from Transfer.Daemon import *


def createBasicData(self):
    pass
    #u =
    #hs = Account("Hryhorii", "Skovoroda", "working", 1, False)
    #c1 = Card(1111, "checking", 1, False)

""" Main file that start everything """
if __name__ == '__main__':
    #ac = con.restoreAccount(1)
    #print(ac)
    #print("-------------------------------------")
    #u = con.restoreUser("login")
    #print(u)
    #print("-------------------------------------")
    #c = con.restoreCards(ac.id)
    #card = c[0]
    #print(card)
    #print(card.__class__)

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


