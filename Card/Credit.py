from Card import Card
from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for Credit (Card) entity
"""
class Credit(Card):
    id = int (0)
    number = int (0)
    password = int (0)
    type = str ("credit")
    gold = bool (0)
    balance = float (0)
    limit = float (0)
    valid = bool (0)
    account_id = int (0)
    bankInterest = float (0)

    #take money from the card
    def makeTransaction(self, amount):
        if self.balance > amount:
            self.balance -= amount
        #else
            #exceptions
        # db call

    #put money on the card
    def putLimit(self, limit):
        #some checks
        self.limit = limit
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
        type = "credit"
        super(self, id, number, password, type, gold)
