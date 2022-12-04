from Card import Card
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
    gold = bool (0)
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
    def __init__(self, password, cardType, gold, balance, limit, valid, account):
        super(Checking, self).__init__(password, "checking", gold, balance, limit, valid, account)

    #make transaction from one card to another card
    def makeTransaction(self, card, amount):
        if self.balance > amount:
            self.balance -= amount
            #checks
            card.balance += amount
        #else
            #exceptions

    #take money from the card
    def witdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        #else
            #exceptions

    #put money on the card
    def putMoney(self, amount):
        self.balance += amount
        #else
            #exceptions

    #changePassword
    def changePassword(self, newPassword):
        super()

    #checkBalance
    def checkBalance(self):
        self()

    #creates a new Card
    def __init__(self, id, number, password, gold):
        type = "checking"
        super(self, id, number, password, type, gold)
