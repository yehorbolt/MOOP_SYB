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
    c = con.restoreCards(ac.id)
    print(c[0])

    #user1 = User("newlogin", "1234567890", 3000, False)
    #hs = Account("Hryhoriy", "Skovoroda", "has job", user1, bank)
    #db1_user = con.restoreUser("newlogin") # it restores data about the User
    #print(db1_user)
    #account = con.restoreAccount() # it restores data about the Account of the User
    #cards = tuple(con.restoreCards()) # it restores data about the Cards of the User
