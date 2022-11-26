#class that is responsible for the card
class Card:
    id = 0
    number = ""
    password = ""
    type = "default"
    balance = 0
    gold = 0
    valid = 1
    account_id = 0

    #creates a Card
    def __init__(self, id, number, password, type, gold):
        #different chckings
        self.id = id
        self.number = number
        self.password = password
        self.type = type
        self.gold = gold

    #returns balance
    def checkBalance(self):
        return self.balance

    #changes password
    def changePassword(self, newPassword):
        if (newPassword != 0 & self.password != newPassword):
            self.password = newPassword


