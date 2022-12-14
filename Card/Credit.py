from Card.Card import Card
from Transfer.Credit import Credit as cred
from Transfer.Transaction import Transaction
from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for Credit (Card) entity
"""
class Credit(Card):
    id = int (0)
    number = int (0)
    password = int (0)
    type = str ("credit")
    balance = float (0)
    limit = float (0)
    valid = bool (1)
    leftToPay = int (0)           # left to pay for the credit
    bankInterest = float (10)     #
    account_id = int (0)

    """
    Constructor 
    :param: self, password, cardType, balance, limit, account_id
    :type: Checking, int, str, float/int, float/int, int
    :returns: nothing
    """
    def __init__(self, password, cardType, account_id, restore):
        if restore == False:
            super(Credit, self).__init__(password, "credit", account_id, restore)
        if restore == True:
            id = self.findCardId(account_id, cardType)
            number = self.findCardNumber(account_id, cardType)
            balance = self.findCardBalance(account_id, cardType)
            self.valid = True
            limit = self.findCardLimit(account_id, cardType)
            leftToPay = self.findLeftToPay(account_id, cardType)
            self.restoreCard(id, number, password, cardType, balance, limit, leftToPay, account_id)

    """
    Constructor for restoring Card
    :param: self, id, number, password, cardType, balance, limit, leftToPay, account_id
    :type: Credit, int, str, str, str, float/int, float/int, float/int, int 
    :returns: nothing
    """
    def restoreCard(self, id, number, password, cardType, balance, limit, leftToPay, account_id):
        super(Credit, self).restoreCard(id, number, password, cardType, balance, limit, leftToPay, account_id)

    """
    This method gets the user status
    :param: self, user_id
    :type: Credit, int
    :returns: status
    :rtype: str
    """
    def getUserStatus(self, user_id):
        query = "SELECT status FROM account where user_id = '" + str (user_id) + "';"
        return str (con.executeReturn(query).__getitem__(0))

    """
    This method takes credit 
    :param: self, amount
    :type: Credit, float/int
    :returns: nothing
    """
    def takeCredit(self, amount):
        try:
            cred(self.number, self.number, amount, self.id, self.account_id)
            self.balance += amount
            self.leftToPay = amount * float(1.1)
            self.updateLeftToPay(self.leftToPay)
        except Exception as e:
            raise Exception(e)

    """
    This method changes leftToPay in database
    :param: self, leftToPay
    :type: Credit, float/int
    :returns: nothing
    """
    def updateLeftToPay(self, leftToPay):
        query = "UPDATE card SET leftToPay = '" + str (leftToPay)  + "' WHERE id = '" + str (self.id) + "';"
        con.execute(query)

    """
    Makes transaction from the Checking Card
    :param: self, card, amount
    :type: Checking, Checking or Savings or Credit, float or int
    :returns: nothing
    """
    def makeTransaction(self, toCard, amount):
        self.balance = self.getBalance() #updates card balance
        assert type(toCard) == int, "Thr Card number on which you want transfer money is wrong!"
        assert self.cardExists(toCard) == True, "You can't make a transaction on the card that doesn't exist!"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.balance, "You can't make Transaction with more money than you have on your card!"
        from Transfer.Transfer import Transfer
        if Transfer.getCardType(Transfer, self.number) != "credit":
            assert (self.balance - amount) >= self.limit, "You can't make a transaction, because of the limit!"
        Transaction(self.number, toCard, amount, self.id, "transaction", self.account_id)
        self.balance = self.getBalance()
        self.leftToPays = self.getLeftToPay()

    """
    Withdraws the money from the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def withdraw(self, amount):
        self.balance = self.getBalance() #updates card balance
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount < self.balance, "You can't withdraw more money than you have on your card!"
        Transaction(self.number, self.number, amount, self.id, "withdraw", self.account_id)
        self.balance = self.getBalance()

    """
    THis method puts money on the Checking Card
    :param: self, amount
    :type: Checking, float or int
    :returns: string representation
    :rtype: str
    """
    def putMoney(self, user_id, amount):
        self.balance = self.getBalance() #updates card balance
        assert type(user_id) == int, "user_id can be only int!"
        assert type(amount) == float or int, "You must enter amount as a float or an int!"
        assert amount <= self.checkUserMoney(user_id), "User can't put on the Card more money that he has!"
        Transaction(self.number, self.number, amount, self.id, "putMoney", self.account_id)
        self.balance = self.getBalance()
        self.leftToPay = self.getLeftToPay()
