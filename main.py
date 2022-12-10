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
from ConnectToDB import ConnectToDb as con

def createBasicData(self):
    bank = Bank("PrivatBank", "Petr Krumphanzl", "Kyiv")
    atm1 = ATM("Kyiv, Peremohy square", bank)
    user1 = User("newlogin", "1234567890", 3000)
    hs = Account("Hryhoriy", "Skovoroda", "has job", user1, bank)
    #checking = Checking(1111, "checking", 3000, 500, True, hs)
    #credit = Credit
    #savings

""" Main file that start everything """
if __name__ == '__main__':
    user1 = User("newlogin", "1234567890", 3000, False)
    hs = Account("Hryhoriy", "Skovoroda", "has job", user1, bank)
    db1_user = con.restoreUser("newlogin") # it restores data about the User
    print(db1_user)
    account = con.restoreAccount() # it restores data about the Account of the User
    cards = tuple(con.restoreCards()) # it restores data about the Cards of the User
