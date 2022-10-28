from Card.Card import Card

#class that is responsible for checking card
class Checking(Card):
    id = 0
    number = ""
    password = ""
    type = "checking"
    balance = 0
    gold = 0

    #make transaction from one card to another card
    def makeTransaction(self, card, amount):
        if (self.balance > amount):
            self.balance -= amount
            #checks
            card.balance += amount
        #else
            #exceptions

    #take money from the card
    def witdraw(self, amount):
        if (self.balance > amount):
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