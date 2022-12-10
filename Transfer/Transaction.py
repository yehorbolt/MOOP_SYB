from Transfer import Transfer
from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for a Transaction entity 
"""
class Transaction(Transfer):
    id = int (0)
    fromCard = int (0)
    toCard = int (0)
    amount = float (0)
    date = str ("default")
    type = str ("transaction")
    active = bool (0)
    card_id = int (0)             # from which card (id) is transfer
    card_account_id = int (0)     # id of the account that has a card from which transfer takes place
    atm_id = int (1)              # id of the atm where transaction is taken
    atm_bank_id = int (1)         # bank id that has an atm

    """
    Constructor
    :param: self, fromCard, toCard, amount, date, transferType, card_id, card_account_id, atm_id, atm_bank_id
    :type: Transaction, int, int, float/int, date, str, int, int, int, int
    :returns: nothing
    """
    def __init__(self, fromCard, toCard, amount, card_id, card_account_id):
        super(Transfer, self).__init__(fromCard, toCard, amount, self.type, 0, 0, card_id, card_account_id, self.atm_id, self.atm_bank_id)
        self.moneyChange(fromCard, toCard, amount)

    """
    This method changes in database amount of money on the cards
    :param: self, fromCard, toCard, amount
    :type: Transfer, int, int, float/int
    :returns: nothing
    """
    def moneyChange(self, fromCard, toCard, amount):
        self.changeBalance(fromCard, amount, False)
        self.changeBalance(toCard, amount, True)
        self.inactive()
