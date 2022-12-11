from ConnectToDB import ConnectToDb as con
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
    #hs = Account("Hryhoriy", "Skovoroda", "working", 1, False)
    #c1 = Card(1111, "checking", 1, False)

""" Main file that start everything """
if __name__ == '__main__':
    ac = con.restoreAccount(1)
    print(ac)
    print("-------------------------------------")
    u = con.restoreUser("login")
    print(u)
    print("-------------------------------------")
    c = con.restoreCards(ac.id)
    card = c[0]
    print(card)
    print(card.__class__)
