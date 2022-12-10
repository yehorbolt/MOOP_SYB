from Card import Card
from Transfer.Transaction import Transaction
from Transfer.Daemon import Daemon

"""
    This class is responsible for Savings (Card) entity
"""
class Savings(Card):
    id = int (0)
    number = int (0)
    password = int (0)
    type = str ("savings")
    balance = float (0)
    limit = float (0)
    valid = bool (1)
    account_id = int (0)
    userInterest = float (8)

    """
    Constructor 
    :param: self, password, cardType, balance, limit, account_id
    :type: Savings, int, str, float/int, float/int, int
    :returns: nothing
    """
    def __init__(self, password, cardType, account_id):
        super(Savings, self).__init__(password, "savings", account_id)
        d = Daemon(self.number, self.number, self.balance, 5, True, self.id, self.account_id)

    """
    Withdraws the money from the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def withdraw(self, amount):
        self.balance = self.getBalance() # updates card balance
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
        self.balance = self.getBalance() # updates card balance
        assert type(user_id) == int, "user_id can be only int!"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.checkUserMoney(user_id), "User can't put on the Card more money that he has!"
        t = Transaction(self.number, self.number, amount, self.id, "putMoney", self.account_id)
        self.balance = self.getBalance()
