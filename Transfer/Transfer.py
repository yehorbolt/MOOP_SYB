from ConnectToDB import ConnectToDb as con
from datetime import datetime
from pytz import timezone

"""
    This class is responsible for a Transfer entity 
"""
class Transfer:
    id = int (0)
    fromCard = int (0)
    toCard = int (0)
    amount = float (0)
    date = str ("default")
    transferType = str ("default")
    active = bool (0)
    frequency = int (0)
    card_id = int (0)             # from which card (id) is transfer
    card_account_id = int (0)     # id of the account that has a card from which transfer takes place
    atm_id = int (1)              # id of the atm where transaction is taken
    atm_bank_id = int (1)         # bank id that has an atm

    """
    Constructor
    :param: self, fromCard, toCard, amount, date, transferType, card_id, card_account_id, atm_id, atm_bank_id
    :type: Transfer, int, int, float/int, date, str, int, int, int, int
    :returns: nothing
    """
    def __init__(self, fromCard, toCard, amount, transferType, leftToPay, frequency, card_id, card_account_id):
        assert self.cardExists(fromCard) == True, "Card from which you want to make a transfer doesn't exist!"
        assert self.cardExists(toCard) == True, "Card on which you want to make a transfer doesn't exist!"
        assert amount > 0, "You can't make a Transaction with amount less than 1!"
        if transferType == "credit" and fromCard != toCard or transferType != "putMoney-savings":
            assert self.getBalance(fromCard) >= amount, "You can't transfer more money than you have on the Card!"
        assert self.validType(transferType) == True, "You can't make a transfer with type different from Transaction, Daemon or Credit"
        assert type(leftToPay) == float or int, "You can't use other type than float or int for initialising leftToPay!"
        assert type(frequency) == float or int, "You can't set frequency for a daemon using other type than float or int!"
        self.id = con.getLastId("transfer") + 1
        self.fromCard = fromCard
        self.toCard = toCard
        self.amount = amount
        self.date = self.getTime()
        self.transferType = transferType
        self.active = bool (1)
        self.leftToPay = float (leftToPay)
        self.frequency = float (frequency)
        self.card_id = card_id
        self.card_account_id = card_account_id
        self.createTransfer()

    """
    This method adds transfer to db
    :param: self
    :type: Transfer
    :returns: nothing
    """
    def createTransfer(self):
        query = 'INSERT INTO transfer (id, "from", "to", amount, date, type, active, card_id, card_account_id, atm_id, atm_bank_id) ' \
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        val = (str (self.id), self.fromCard, self.toCard, self.amount, self.date,
               self.transferType, int (self.active), str (self.card_id),
               str (self.card_account_id), str (self.atm_id), str (self.atm_bank_id))
        con.executeWithVal(query, val)

    """
    This method returns date for a transfer
    :param: self
    :type: Transfer
    :returns: nothing
    """
    def getTime(self):
        ukraine_time = timezone('Europe/Kiev')
        ua_time = datetime.now(ukraine_time).strftime("%Y-%m-%d %H:%M:%S")
        return ua_time

    """
    This method changes activeness of transaction 
    :param: self
    :type: Transfer
    :returns: nothing
    """
    def inactive(self):
        self.active = bool (0)
        query = "UPDATE transfer SET active = 0 WHERE id = '" + str (self.id) + "';"
        con.execute(query)

    """
    This method checks if the Card given Exists in the database
    :param: self, card
    :type: Checking or Savings or Credit
    :returns: True or False
    :rtype: bool
    """
    def cardExists(self, card):
        query = "SELECT * FROM card WHERE number = " + str (card) + ";"
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
        if type != "transaction" and type != "putMoney" and type != "withdraw" and type != "credit" and type != "putMoney-savings" and type != "daemon":
            return False
        else:
            return True

    """
    This method returns balance of the card given
    :param: self, card
    :type: Transaction, int
    :returns: balance
    :rtype: float/int
    """
    def getBalance(self, card):
        query = "SELECT balance FROM card WHERE number = " + str (card) + ";"
        records = con.executeReturn(query)
        res = float('.'.join(str(ele) for ele in records[0]))
        return res

    """
    This method returns type of the card given
    :param: self, card
    :type: Transaction, int
    :returns: type
    :rtype: str
    """
    def getCardType(self, card):
        query = "SELECT type FROM card WHERE number = " + str (card) + ";"
        records = con.executeReturn(query)
        res = str (records.__getitem__(0))
        res = res.replace(',', '')
        res = res.replace(')', '')
        res = res.replace('(', '')
        res = res.replace("'", '')
        return res

    """
    This method returns leftToPay of the card given
    :param: self, card
    :type: Transaction, int
    :returns: type
    :rtype: str
    """
    def getLeftToPay(self, card):
        query = "SELECT leftToPay FROM card WHERE number = " + str (card) + ";"
        records = con.executeReturn(query)
        res = float('.'.join(str(ele) for ele in records[0]))
        return res

    """
    This method changes balance
    :param: self, card, amount, add
    :type: Transaction, int, float/int, bool
    :returns: nothing
    """
    def changeBalance(self, card, amount, add):
        if self.getCardType(card) == "credit" and add == True:
            leftToPay = self.getLeftToPay(card)
            if  leftToPay > 0 and leftToPay < amount:
                query = "UPDATE card SET leftToPay = %s WHERE number = %s;"
                values = (0, card)
                con.executeWithVal(query, values)
                newBalance = self.getBalance(card) + amount - leftToPay
                query = "UPDATE card SET balance = %s WHERE number = %s;"
                values = (newBalance, card)
                con.executeWithVal(query, values)
            if  leftToPay > amount:
                query = "UPDATE card SET leftToPay = %s WHERE number = %s;"
                values = (leftToPay-amount, card)
                con.executeWithVal(query, values)
            if  leftToPay == 0:
                newBalance = self.getBalance(card) + amount
                query = "UPDATE card SET balance = %s WHERE number = %s;"
                values = (newBalance, card)
                con.executeWithVal(query, values)
        else:
            if self.cardExists(card) == True:
                if add == True:
                    newBalance = self.getBalance(card) + amount
                    query = "UPDATE card SET balance = %s WHERE number = %s;"
                    values = (newBalance, card)
                    con.executeWithVal(query, values)
                else:
                    newBalance = self.getBalance(card) - amount
                    query = "UPDATE card SET balance = %s WHERE number = %s;"
                    values = (newBalance, card)
                    con.executeWithVal(query, values)
            else:
                raise Exception("This Card doesn't exist!")
