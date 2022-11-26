from Card import Card

#class that is responsible for checking card
class Savings(Card):
    id = 0
    number = ""
    password = ""
    type = "savings"
    balance = 0
    gold = 0
    userInterest = 0

    #take money from the card
    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        #else
            #exceptions
        # db call

    #put money on the card
    def putMoney(self, limit):
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
