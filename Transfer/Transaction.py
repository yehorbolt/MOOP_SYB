from Transfer import Transfer

class Transaction(Transfer):
    id = int (0)
    fromCard = int (0)
    toCard = int (0)
    amount = float (0)
    date = str ("default")
    type = str ("default")
    card_id = int (0)             # from which card (id) is transfer
    card_account_id = int (0)     # id of the account that has a card from which transfer takes place
    atm_id = int (0)              # id of the atm where transaction is taken
    atm_bank_id = int (0)         # bank id that has an atm

    #constructor
    def __init__(self, fromCard, toCard, amount):
        self.fromCard = fromCard
        self.toCard = toCard
        self.amount = amount
        #self.date =
        #should be somehow created and watched he real time date abd time
