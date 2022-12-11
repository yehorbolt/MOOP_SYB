from ConnectToDB import ConnectToDb as con
import random

"""
    This class is responsible for Card entity
"""
class Card:
    id = int (0)
    number = int (0)
    password = int (0)
    type = str ("default")
    balance = float (0)
    limit = float (0)
    valid = bool (0)
    leftToPay = int (0)           # left to pay for the credit
    account_id = int (0)

    """
    Constructor 
    :param: self
    :type: Card
    :returns: nothing
    """
    def __init__(self, password, cardType, account_id, restore):
        assert type(password) is int, "Card password must be an int!"
        assert self.validPassword(password) == True, "Password must be be 4 numbers from 0 to 9!"
        assert self.validType(cardType) == True, "You've entered invalid Card type!"
        assert type(account_id) is int, "You must give an int (account_id) as the last parameter!"
        if restore == False:
            assert self.thisCardExists(cardType, account_id) == True, "You can't create the card of type " + str (cardType) + " as you already have one!"
            self.id = con.getLastId("card") + 1
            self.number = self.generateNumber()
            self.password = password
            self.type = cardType
            self.balance = float (0)
            self.valid = True
            self.limit = float (0)
            self.account_id = account_id
            self.createCard()
        else:
            pass

    """
    This method checks if the account already has the card of this type
    :param: self, type account_id
    :type: Card, str, int
    :returns: True/False
    :rtype: bool
    """
    def thisCardExists(self, type, account_id):
        query = "SELECT * FROM card WHERE account_id = '" + str (account_id) + "' AND type = '" + str (type) + "';"
        recors = tuple (con.executeReturn(query))
        if recors.__len__() == 0:
            return True
        return False

    """
    This method finds a card id
    :param: self, account_id
    :type: Card, int
    :returns: id
    :rtype: int
    """
    def findCardId(self, account_id):
        query = "SELECT id FROM card WHERE account_id = '" + str (account_id) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    This method finds a card number
    :param: self, account_id
    :type: Card, int
    :returns: id
    :rtype: int
    """
    def findCardNumber(self, account_id):
        query = "SELECT number FROM card WHERE account_id = '" + str (account_id) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    This method finds a card balance
    :param: self, account_id
    :type: Card, int
    :returns: balance
    :rtype: float/int
    """
    def findCardBalance(self, account_id):
        query = "SELECT balance FROM card WHERE account_id = '" + str (account_id) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    This method finds a card limit
    :param: self, account_id
    :type: Card, int
    :returns: limit
    :rtype: float/int
    """
    def findCardLimit(self, account_id):
        query = 'SELECT "limit" FROM card WHERE account_id = \'' + str (account_id) + '\';'
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    This method finds a card leftToPay
    :param: self, account_id
    :type: Card, int
    :returns: id
    :rtype: int
    """
    def findLeftToPay(self, account_id):
        query = "SELECT leftToPay FROM card WHERE account_id = '" + str (account_id) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    Constructor for restoring Card
    :param: self, id, number, password, cardType, account_id
    :type: Card, int, str, str, str, int
    :returns: nothing
    """
    def restoreCard(self, id, number, password, cardType, balance, limit, leftToPay, account_id):
        self.id = id
        self.number = number
        self.password = password
        self.type = cardType
        self.balance = balance
        self.valid = True
        self.limit = limit
        self.leftToPay = leftToPay
        self.account_id = account_id

    """
    This method creates Card in the database
    :param: self
    :type: Card
    :returns: nothing
    """
    def createCard(self):
        query = 'INSERT INTO card (id, number, password, type, balance, valid, "limit", leftToPay, account_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
        val = (self.id, self.number, self.password, self.type, self.balance, int (self.valid), self.limit, self.leftToPay, self.account_id)
        con.executeWithVal(query, val)

    """
    This method generates the number of the card 
    :param: self
    :type: Card
    :returns: number
    :rtype: int
    """
    def generateNumber(self):
        number = str (random.randint(0,9))
        for i in range(8):
           number += str (random.randint(0,9))
        while self.numberExists(number) == True:
            newNumber = str (random.randint(0,9))
            for i in range(6):
                newNumber += str (random.randint(0,9))
            number = newNumber
        return number

    """
    This method checks if the card with number given exists in the database  
    :param: self, number
    :type: Card, int
    :returns: True or False
    :rtype: bool
    """
    def numberExists(self, number):
        query = "SELECT * FROM card WHERE number = '" + number + "';"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return False
        else:
            return True

    """
    This method checks if the password given is valid (4 numbers in a row)  
    :param: self, password
    :type: Card, int
    :returns: True or False
    :rtype: bool
    """
    def validPassword(self, password):
        password = str (password)
        if password.__len__() != 4 or password.isdigit() == False:
            return False
        else:
            return True

    """
    This method checks if the type given is valid (checking, credit or savings)  
    :param: self, type
    :type: Card, str
    :returns: True or False
    :rtype: bool
    """
    def validType(self, type):
        type = str (type)
        if type != "savings" and type != "credit" and type != "checking":
            return False
        else:
            return True

    """
    This method changes the Card password
    :param: self, newPassword
    :type: Card, int
    :returns: nothing
    """
    def changePassword(self, newPassword):
        assert type(newPassword) is int, "newPassword must be an int!"
        if newPassword == self.password:
            raise Exception("You have entered same password for a Card!")
        assert self.validPassword(newPassword) == True, "Password must be be 4 numbers from 0 to 9!"
        self.password = newPassword
        self.updatePassword()

    """
    This method updates the Card password in the database
    :param: self
    :type: Card
    :returns: nothing
    """
    def updatePassword(self):
        query = "UPDATE card SET password = %s WHERE id = %s;"
        val = (self.password, self.id)
        con.executeWithVal(query, val)

    """
    This method changes the Card balance
    :param: self, newBalance
    :type: Card, float
    :returns: nothing
    """
    def changeBalance(self, newBalance):
        assert type(newBalance) is float or type(newBalance) is int, "newBalance must be a float or an int!"
        assert newBalance > self.limit, "newBalance must me larger or equal to the limit"
        if newBalance == self.balance:
            raise Exception("You have entered same balance for a Card!")
        assert newBalance >= 0, "newBalance must be equal or more than 0!"
        self.balance = newBalance
        self.updateBalance()


    """
    This method gets the card balance from the database
    :param: self
    :type: Card
    :returns: balance
    :rtype: float/int
    """
    def getBalance(self):
        query = "SELECT balance FROM card WHERE id = '" + str (self.id) + "';"
        records = con.executeReturn(query)
        return records.__getitem__(0)[0]

    """
    This method checks if the Card given Exists in the database
    :param: self, card
    :type: Checking or Savings or Credit
    :returns: True or False
    :rtype: bool
    """
    def cardExists(self, card):
        assert type(card) == int, "You must enter the number of the Card!"
        query = "SELECT * FROM card WHERE number = " + str (card) + ";"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return False
        else:
            return True

    """
    This method returns amount of money user has with him
    :param: self, user_id
    :type: Card, int
    :returns: money 
    :rtype: float/int
    """
    def checkUserMoney(self, user_id):
        query = "SELECT money FROM user WHERE id = '" + str (user_id) + "';"
        records = con.executeReturn(query)
        return records.__getitem__(0)[0]

    """
    This method changes the Card valid status and deletes the Card if Card becomes invalid 
    :param: self, valid
    :type: Card, bool
    :returns: nothing
    """
    def changeValid(self, valid):
        assert type(valid) is bool, "valid must be a bool!"
        if valid == self.valid:
            raise Exception("You have entered same valid status for a Card!")
        self.valid = valid
        self.updateValid()

    """
    This method updates the Card valid status in the database
    :param: self
    :type: Card
    :returns: nothing
    """
    def updateValid(self):
        if self.valid == True:
            query = "UPDATE card SET valid = %s WHERE id = %s;"
            val = (self.balance, self.id)
            con.executeWithVal(query, val)
        else:
            self.deleteCard()

    """
    This method changes the Card limit
    :param: self, newLimit
    :type: Card, float
    :returns: nothing
    """
    def changeLimit(self, newLimit):
        assert type(newLimit) is float or type(newLimit) is int, "newLimit must be a float or an int!"
        if newLimit == self.limit:
            raise Exception("You have entered same limit for a Card!")
        assert newLimit >= 0, "newLimit must be equal or more than 0!"
        self.limit = newLimit
        self.updateValid()

        """
    This method updates the Card limit in the database
    :param: self
    :type: Card
    :returns: nothing
    """
    def updateLimit(self):
        query = 'UPDATE card SET "limit" = %s WHERE id = %s;'
        val = (self.limit, self.id)
        con.executeWithVal(query, val)

    """
    This method deletes the card from the database
    :param: self
    :type: Card
    """
    def deleteCard(self):
        query = "DELETE FROM card WHERE id = " + str (self.id) + ";"
        con.execute(query)

    """
    Returns string representation of the Card
    :param: self
    :type: Card
    :returns: string representation
    :rtype: str
    """
    def __str__(self):
        return f"id: {self.id}, number: {self.number}, password: {self.password}, " \
               f"type: {self.type}, balance: {self.balance}, valid: {self.valid}, " \
               f"limit: {self.limit}, leftToPay: {self.leftToPay}, account_id: {self.account_id}"
