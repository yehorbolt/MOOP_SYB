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
            self.checkIfValid(toCard, amount, card_account_id)
        except Exception as e:
            raise AssertionError(e)
        assert self.getCreditSum(card_account_id) + amount <= self.findCardLimit(fromCard), "You can't take other credit, as you've put a limit!"
        amount *= 1,1 # amount of the money with bank interest
        super(Credit, self).__init__(fromCard, toCard, amount, "credit",  amount, 0, card_id, card_account_id)
        self.changeBalance(toCard, amount, True)

    """
    This method checks if the user can get a credit on his account
    :param: self, card, amount
    :type: Credit, int, float/int
    :returns: True/False
    :rtype: bool
    """
    def checkIfValid(self, card, amount, card_account_id):
        assert self.checkActiveCredit(card) == False, "The user already has an active credit!"
        assert self.mayPay(card, amount) == True, "User doesn't have enough money on his cards!"
        return True

    """
    This method finds user_id by card_account_id
    :param: self, card_account_id
    :type: Credit, int
    :returns: user_id
    :rtype: int
    """
    def findUserId(self, card_account_id):
        query = "SELECT user_id FROM account WHERE id = '" + str (card_account_id) + "';"
        records = con.executeReturn(query)
        res = float('.'.join(str(ele) for ele in records[0]))
        return res

    """
    This method finds a card limit
    :param: self, account_id
    :type: Credit, int
    :returns: limit
    :rtype: float/int
    """
    def findCardLimit(self, account_id):
        query = 'SELECT "limit" FROM card WHERE account_id = \'' + str (account_id) + '\';'
        records = con.executeReturn(query)
        res = float('.'.join(str(ele) for ele in records[0]))
        return res

    """
    This method returns sum of all active credits the user took
    :param: self, card_account_id
    :type: Credit, int
    :returns: sum
    :type: float
    """
    def getCreditSum(self, card_account_id):
        query = "SELECT SUM(amount) FROM transfer WHERE  \"type\" = 'credit' AND card_account_id = '" + str (card_account_id) + "';"
        records = con.executeReturn(query)
        if None in records[0][0]:
            return 0
        else:
            return float('.'.join(str(ele) for ele in records(0)))

    """
    This method checks if the user has active credits
    :param: self, card
    :type: Credit, int
    :returns: True/False
    :rtype: bool
    """
    def checkActiveCredit(self, card):
        query = "SELECT * FROM transfer WHERE \"from\" = " + str (card) + " AND type = 'credit' AND active = 1;"
        records = con.executeReturn(query)
        if records.__len__() == 0:
            return False
        else:
            return True

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
        overallBalance = self.countMoneyOnCards(account_id)
        query = "SELECT status FROM account WHERE id = '" + str (account_id) + "';"
        records = con.executeReturn(query)
        if ''.join(records[0][0]) == "working":
            if overallBalance >= amount * 1/4:
                return True
            else:
                return False
        else:
            if overallBalance >= amount * 1/2:
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
    def countMoneyOnCards(self, account_id):
        query = "SELECT SUM(balance) FROM card where account_id = '" + str (account_id) + "' AND type <> 'credit';"
        records = con.executeReturn(query)
        res = float('.'.join(str(ele) for ele in records[0]))
        return res

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
        res = float('.'.join(str(ele) for ele in records[0]))
        return res



