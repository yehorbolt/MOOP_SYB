from ConnectToDB import ConnectToDb as con
from User.User import User
from Transfer.Transfer import Transfer

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
    def __init__(self, fromCard, toCard, amount, card_id, type, card_account_id):
        super(Transaction, self).__init__(fromCard, toCard, amount, type, 0, 0, card_id, card_account_id)
        if type == "transaction":
            self.transaction(fromCard, toCard, amount)
        if type == "withdraw":
            self.withdraw(fromCard, amount)
            self.userChangeMoney(amount, type, card_account_id)
        if type == "putMoney":
            self.putMoney(toCard, amount)
            self.userChangeMoney(amount, type, card_account_id)


    """
    This method changes amount of money user has with him
    :param:
    :type:
    :returns: nothing
    """
    def userChangeMoney(self, amount, type, card_account_id):
        user_id = self.findUserId(card_account_id)
        if type == "withdraw":
            user_balance = User.returnMoney(user_id) + amount
        if type == "putMoney":
            user_balance = User.returnMoney(user_id) - amount
        query = "UPDATE user SET money = %s WHERE id = %s"
        values = (user_balance, user_id)
        con.executeWithVal(query, values)

    """
    Retunrs user id from db by account id given
    :param: self, card_account_id
    :type: Transaction, int
    :returns: user_id
    :rtype: int
    """
    def findUserId(self, card_account_id):
        query = "SELECT user_id FROM account WHERE id = '" + str(card_account_id) + "';"
        return tuple(con.executeReturn(query)).__getitem__(0)[0]

    """
    This method changes in database amount of money on the cards
    :param: self, fromCard, toCard, amount
    :type: Transfer, int, int, float/int
    :returns: nothing
    """
    def transaction(self, fromCard, toCard, amount):
        self.changeBalance(fromCard, amount, False)
        self.changeBalance(toCard, amount, True)
        self.inactive()

        """
    This method changes in database amount of money on the cards
    :param: self, fromCard, toCard, amount
    :type: Transfer, int, int, float/int
    :returns: nothing
    """
    def withdraw(self, fromCard, amount):
        self.changeBalance(fromCard, amount, False)
        self.inactive()

        """
    This method changes in database amount of money on the cards
    :param: self, fromCard, toCard, amount
    :type: Transfer, int, int, float/int
    :returns: nothing
    """
    def putMoney(self, toCard, amount):
        self.changeBalance(toCard, amount, True)
        self.inactive()