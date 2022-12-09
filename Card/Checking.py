from Card import *
from User.User import User
from Bank.Bank import Bank
from Account.Account import Account
from Transfer.Transaction import Transaction
from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for Checking (Card) entity
"""
class Checking(Card):
    id = int (0)
    number = int (0)
    password = int (0)
    type = str ("checking")
    balance = float (0)
    limit = float (0)
    valid = bool (0)
    account_id = int (0)

    """
    Constructor 
    :param: self
    :type: Checking
    :returns: nothing
    """
    def __init__(self, password, cardType, balance, limit, valid, account):
        super(Checking, self).__init__(password, "checking", balance, limit, valid, account)

        """
    This method creates Checking Card in the database
    :param: self
    :type: Checking
    :returns: nothing
    """
    def createCard(self):
        super(Checking, self).createCard()

    """
    This method generates the number of the Checking Card 
    :param: self
    :type: Checking
    :returns: number
    :rtype: int
    """
    def generateNumber(self):
        super(Checking, self).generateNumber()
        
    """
    This method checks if the Checking Card with the number given exists in the database  
    :param: self, number
    :type: Checking, int
    :returns: True or False
    :rtype: bool
    """
    def numberExists(self, number):
        super(Checking, self).numberExists(number)

    """
    This method checks if the password given is valid (4 numbers in a row)  
    :param: self, password
    :type: Checking, int
    :returns: True or False
    :rtype: bool
    """
    def validPassword(self, password):
        super(Checking, self).validPassword(password)

    """
    This method checks if the type given is valid (checking, credit or savings)  
    :param: self, type
    :type: Checking, str
    :returns: True or False
    :rtype: bool
    """
    def validType(self, type):
        super(Checking, self).validType(type)

    """
    This method changes the Checking Card password
    :param: self, newPassword
    :type: Checking, int
    :returns: nothing
    """
    def changePassword(self, newPassword):
        super(Checking, self).changePassword(newPassword)
    """
    This method updates the Checking Card password in the database
    :param: self
    :type: Checking
    :returns: nothing
    """
    def updatePassword(self):
        super(Checking, self).updatePassword()

    """
    This method changes the Checking Card balance
    :param: self, newBalance
    :type: Checking, float
    :returns: nothing
    """
    def changeBalance(self, newBalance):
        super(Checking, self).changeBalance(newBalance)

    """
    This method updates the Checking Card balance in the database
    :param: self
    :type: Checking
    :returns: nothing
    """
    def updateBalance(self):
        super(Checking, self).updateBalance()

    """
    This method changes the Checking Card gold status
    :param: self, gold
    :type: Checking, bool
    :returns: nothing
    """
    def changeGold(self, gold):
        super(Checking, self).changeGold(gold)

    """
    This method updates the Checking Card gold status in the database
    :param: self
    :type: Checking
    :returns: nothing
    """
    def updateGold(self):
        super(Checking, self).updateGold()

    """
    This method changes the Checking Card valid status and deletes the Checking Card if Checking Card becomes invalid 
    :param: self, valid
    :type: Checking, bool
    :returns: nothing
    """
    def changeValid(self, valid):
        super(Checking, self).changeValid(valid)

    """
    This method updates the Checking Card valid status in the database
    :param: self
    :type: Checking
    :returns: nothing
    """
    def updateValid(self):
        super(Checking, self).updateValid()

    """
    This method changes the Checking Card limit
    :param: self, newLimit
    :type: Checking, float
    :returns: nothing
    """
    def changeLimit(self, newLimit):
        super(Checking, self).changeLimit(newLimit)

    """
    This method updates the Checking Card limit in the database
    :param: self
    :type: Checking
    :returns: nothing
    """
    def updateLimit(self):
        super(Checking, self).updateLimit()

    """
    This method deletes the Checking Card from the database
    :param: self
    :type: Checking
    """
    def deleteCard(self):
        super(Checking, self).deleteCard()

    """
    Returns string representation of the Checking Card
    :param: self
    :type: Checking
    :returns: string representation
    :rtype: str
    """
    def __str__(self):
        super(Checking, self).__str__()
        
    """
    Makes transaction from the Checking Card
    :param: self, card, amount
    :type: Checking, Checking or Savings or Credit, float or int
    :returns: nothing
    """
    def makeTransaction(self, card, amount):
        assert type(card) == Checking or Card.Savings or Card.Credit, "You must make transaction on the Card!"
        assert self.cardExists(card) == True, "You can't make a transaction on the card that doesn't exist!"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.balance, "You can't make Transaction with more money than you have on your card!"
        if self.balance > amount:
            self.balance -= amount
            card.balance += amount
        self.updateBalance()
        card.updateBalance()

    """
    This method checks if the Card given Exists in the database
    :param: self, card
    :type: Checking or Savings or Credit
    :returns: True or False
    :rtype: bool
    """
    def cardExists(self, card):
        assert type(card) == Checking or Card.Savings or Card.Credit, "You must make transaction on the Card!"
        query = "SELECT * FROM card WHERE id = " + str (card.id) + ";"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return False
        else:
            return True

    """
    Withdraws the money from the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def withdraw(self, amount):
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.balance, "You can't withdraw more money than you have on your card!"
        if self.balance > amount:
            self.balance -= amount * 0.95
        self.updateBalance()

    """
    THis method puts money on the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def putMoney(self, user, amount):
        assert type(user) == User, "Only User can put money on the Card"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < user.money, "User can't put on the Card more money that he has!"
        self.balance += amount * 0.95
        self.updateBalance()
        user.changeMoney(user.money - amount)

u = User("asd", "1234567890", 1000)
b = Bank("ADASDASD", "AFASFAF", "AFSASFASFASFSA")
ac = Account("Aleks", "Severhin", "has job", u, b)
ch = Checking(1111, "checking", True, 2000, 1000, True, ac)
ch2 = Checking(1111, "checking", True, 2000, 1000, True, ac)
try:

except Exception as e:
    print(e)
