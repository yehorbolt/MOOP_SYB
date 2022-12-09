from Card.Card import *
from ATM.ATM import *
from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for a Transfer entity 
"""
class Transfer:
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

    """
    Constructor
    :param: self
    :type: Card
    :returns: nothing
    """
    def __init__(self, fromCard, toCard, amount, date, transferType, atm):
        assert self.cardExists(fromCard) == True, "Card from which you want to make a transfer doesn't exist!"
        assert self.cardExists(toCard) == True, "Card on which you want to make a transfer doesn't exist!"
        assert amount > 0, "You can't make a Transaction with amount less than 1!"
        assert self.validType(transferType) == True, "You can't make a transfer with type different from Transaction, Daemon or Credit"
        assert type(atm) == ATM.ATM, "You can't make a transfer on something that isn't an ATM"
        self.id = con.getLastId("transfer") + 1
        self.fromCard = fromCard.id
        self.toCard = toCard.id
        self.amount = amount
        self.date
        self.type = type
        self.card_id = fromCard.id
        self.card_account_id = fromCard.

    """
    This method checks if the Card given Exists in the database
    :param: self, card
    :type: Checking or Savings or Credit
    :returns: True or False
    :rtype: bool
    """
    def cardExists(self, card):
        assert type(card) == Card.Checking or Card.Savings or Card.Credit, "You must make transfer on the Card!"
        query = "SELECT * FROM card WHERE id = " + str (card.id) + ";"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return False
        else:
            return True

    """
    This method checks if the type given is valid (transaction, daemon or credit)  
    :param: self, type
    :type: Card, str
    :returns: True or False
    :rtype: bool
    """
    def validType(self, type):
        type = str (type)
        if type != "transaction" or type != "daemon" or type != "credit":
            return False
        else:
            return True
