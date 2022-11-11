from Transfer import Transfer

class Transaction(Transfer):
    fromCard = ""
    toCard = ""
    amount = 0
    date = 0

    #constructor
    def __init__(self, fromCard, toCard, amount):
        self.fromCard = fromCard
        self.toCard = toCard
        self.amount = amount
        #self.date =
        #should be somehow created and watched he real time date abd time
