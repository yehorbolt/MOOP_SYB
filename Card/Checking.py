from Card.Card import *
from Transfer.Transaction import Transaction

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
    valid = bool (1)
    account_id = int (0)

    """
    Constructor 
    :param: self, password, cardType, balance, limit, account_id
    :type: Checking, int, str, float/int, float/int, int
    :returns: nothing
    """
    def __init__(self, password, cardType, account_id):
        super(Checking, self).__init__(password, "checking", account_id)

    """
    Makes transaction from the Checking Card
    :param: self, card, amount
    :type: Checking, Checking or Savings or Credit, float or int
    :returns: nothing
    """
    def makeTransaction(self, toCard, amount):
        self.balance = self.getBalance() #updates card balance
        assert type(toCard) == int, "Thr Card number on which you want transfer money is wrong!"
        assert self.cardExists(toCard) == True, "You can't make a transaction on the card that doesn't exist!"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.balance, "You can't make Transaction with more money than you have on your card!"
        t = Transaction(self.number, toCard, amount,  self.id, "transaction", self.account_id)
        self.balance = self.getBalance()


    """
    Withdraws the money from the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def withdraw(self, amount):
        self.balance = self.getBalance() #updates card balance
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.balance, "You can't withdraw more money than you have on your card!"
        t = Transaction(self.number, self.number, amount, self.id, "withdraw", self.account_id)
        self.balance = self.getBalance()

    """
    THis method puts money on the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def putMoney(self, user_id, amount):
        self.balance = self.getBalance() #updates card balance
        assert type(user_id) == int, "user_id can be only int!"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.checkUserMoney(user_id), "User can't put on the Card more money that he has!"
        t = Transaction(self.number, self.number, amount, self.id, "putMoney", self.account_id)
        self.balance = self.getBalance()
