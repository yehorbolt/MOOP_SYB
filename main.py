from ConnectToDB import ConnectToDb as con
from Account.Account import *
from ATM.ATM import *
from Bank.Bank import *
from Card.Checking import Checking
from Card.Credit import *
from Card.Savings import *
from Transfer.Transaction import *
from Transfer.Credit import *
from Transfer.Daemon import *
from User.User import *

def createBasicData(self):
    pass
    #u =
    #hs = Account("Hryhoriy", "Skovoroda", "working", 1, False)
    #c1 = Card(1111, "checking", 1, False)

""" Main file that start everything """
if __name__ == '__main__':
    u = con.restoreUser("login")
    print(u)
    print("-------------------------------------")
    ac = con.restoreAccount(u.id)
    print(ac)
    print("-------------------------------------")
    # c = con.restoreCards(ac.id)
    # checking = Checking (c[0], "checking", 1)
    # print(checking)
    # print(checking.__class__)
