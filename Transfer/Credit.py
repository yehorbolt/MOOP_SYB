from Transfer.Transfer import Transfer
from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for a Credit Entity
"""
class Credit(Transfer):
    id = int (0)
    fromCard = int (0)
    toCard = int (fromCard)
    amount = float (0)
    date = str ("default")
    type = str ("credit")
    active = bool (0)
    bankInterest = int (10)       # bank interest
    card_id = int (0)             # from which card (id) is transfer
    card_account_id = int (0)     # id of the account that has a card from which transfer takes place
    atm_id = int (1)              # id of the atm where transaction is taken
    atm_bank_id = int (1)         # bank id that has an atm

    """
    Constructor
    :param: self, fromCard, toCard, amount, date, transferType, card_id, card_account_id, atm_id, atm_bank_id
    :type: Credit, int, int, float/int, date, str, int, int, int, int
    :returns: nothing
    """
    def __init__(self, fromCard, toCard, amount, card_id, card_account_id):
        try:
            self.checkIfValid(toCard, amount)
        except Exception as e:
            raise AssertionError(e)

        amount *= 1,1 # amount of the money with bank interest
        super(Transfer, self).__init__(fromCard, toCard, amount, "credit",  amount, 0, card_id, card_account_id, self.atm_id, self.atm_bank_id)
        if self.checkIfValid(card_id, amount) == True:
            self.changeBalance(fromCard, toCard, amount, True)

    """
    This method checks if the user can get a credit on his account
    :param: self, card, amount
    :type: Credit, int, float/int
    :returns: True/False
    :rtype: bool
    """
    def checkIfValid(self, card, amount):
        assert self.checkActiveCredit(card) == False, "The user already has an active credit!"
        assert self.mayPay(card) == True, "User doesn't have enough money on his cards!"
        return True

    """
    This method checks if the user has active credits
    :param: self, card
    :type: Credit, int
    :returns: True/False
    :rtype: bool
    """
    def checkActiveCredit(self, card):
        query = "SELECT * FROM transfer WHERE number = " + str (card) + " AND type = 'credit' AND active = 1;"
        records = con.executeReturn(query)
        if records.__len__() == 0:
            return True
        else:
            return False

    """
    This method checks if the user has enough money on his cards
    so that his credit will be accessed
    if user has a job -> he must have more than 25% of the credit amount
    if user is workless -> he must have more than 50% of the credit amount
    :param: self, card, amount
    :type: Credit, int, float/int
    :returns: True/False
    :rtype: bool
    """
    def mayPay(self, card, amount):
        account_id = self.getAccountId(card)
        overallBalance = self.countMoneyOnCards()
        query = "SELECT balance FROM card WHERE number = " + str (card) + " AND account_id = '" + str (account_id) + "';"
        records = con.executeReturn(query)
        if records.__len__() == 0:
            return False
        else:
            for i in records:
                overallBalance += records[i][0]
        query = "SELECT status FROM account WHERE id = " + str (account_id) + "';"
        records = con.executeReturn(query)
        if records[0][0] == "has a job":
            if 1/4 * overallBalance >= amount:
                return True
            else:
                return False
        else:
            if 1/2 * overallBalance >= amount:
                return True
            else:
                return False

    """
    This method counts all money user have on his cards
    :param: self, account_id
    :type: Credit, int
    :returns: money
    :rtype: float/int
    """
    def countMoneyOnCards(self, user_id):
        query = "SELECT COUNT(balance) FROM card where user_id = '" + str (user_id) + "' AND WHERE type <> 'credit';"
        return float (con.executeReturn(query).__getitem__(0))

    """
    This method gets accountid from the database by the card number given
    :param: self, card
    :type: Credit, int
    :returns: account_id
    :rtype: int
    """
    def getAccountId(self, card):
        query = "SELECT account_id FROM card WHERE number = " + str (card) + ";"
        records = con.executeReturn(query)
        return records.__getitem__(0)



