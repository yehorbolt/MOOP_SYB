from Account.Account import *
from ATM.ATM import *
from Bank.Bank import *
from Card.Checking import *
from Card.Credit import *
from Card.Savings import *
from Transfer.Transaction import *
from Transfer.Credit import *
from Transfer.Daemon import *
from User.User import *
from ConnectToDB import ConnectToDb as con

def createBasicData(self):
    bank1 = Bank("PrivatBank", "Petr Krumphanzl", "Kyiv")
    bank2 = Bank("Raiffeisen", "Oleksandr Pisaruk", "Kyiv")
    atm1 = ATM("Kyiv, Peremohy square", bank1)
    atm2 = ATM("Kyiv, Khreschatyk street", bank1)
    atm3 = ATM("Kyiv, Velyka Vasylkivska street", bank1)
    atm4 = ATM("Kyiv, Andriivska street", bank1)
    atm5 = ATM("Kyiv, Peremohy square", bank2)
    atm6 = ATM("Kyiv, Andriivska street", bank2)
    user1 = User("newlogin", "1234567890", 3000)
    hs = Account("Hryhoriy", "Skovoroda", "has job", user1, bank1)
    checking = Checking(1111, "checking", 3000, 500, True, hs)
    credit = Credit
    savings

""" Main file that start everything """
if __name__ == '__main__':
    createBasicData() # it should be called only once, before running the program for the first time!
    banks = tuple (con.restoreBanks()) # it restores data about Banks
    atms = tuple (con.restoreAtms()) # it restores data about ATMs
    user = con.restoreUser() # it restores data about the User
    account = con.restoreAccount() # it restores data about the Account of the User
    cards = tuple(con.restoreCards()) # it restores data about the Cards of the User
