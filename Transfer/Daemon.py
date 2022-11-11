from Transfer import Transfer

class Daemon(Transfer):
    fromCard = ""
    toCard = ""
    amount = 0
    frequency = 0
    nextDate = 0
    active = 0

    #constructor
    def __init__(self, fromCard, toCard, amount, frequency):
        self.fromCard = fromCard
        self.toCard = toCard
        self.amount = amount
        self.frequency = frequency
        #self.nextDate = add to today's date frequency
        self.active = True
