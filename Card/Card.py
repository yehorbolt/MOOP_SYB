from Account.Account import Account
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
    gold = bool (0)
    balance = float (0)
    limit = float (0)
    valid = bool (0)
    account_id = int (0)

    """
    Constructor 
    :param: self
    :type: Card
    :returns: nothing
    """
    def __init__(self, password, cardType, gold, balance, limit, valid, account):
        assert type(password) is int, "Card password must be an int!"
        assert self.validPassword(password) == True, "Password must be be 4 numbers from 0 to 9!"
        assert self.validType(cardType) == True, "You've entered invalid Card type!"
        assert type(gold) is bool, "Gold must be a boolean!"
        assert type(balance) is float or type(balance) is int, "Balance must be a float or an int!"
        assert type(limit) is float or type(balance) is int, "Limit must be a float or an int!"
        assert balance >= 0, "Balance must be 0 or more!"
        assert limit >= 0, "Limit must be 0 or more!"
        assert type(valid) is bool, "Valid must be a bool!"
        assert type(account) is Account, "You must give Account as the last parameter to a constructor!"
        self.id = con.getLastId("card") + 1
        self.number = self.generateNumber()
        self.password = password
        self.type = cardType
        self.balance = balance
        self.gold = gold
        self.valid = valid
        self.limit = limit
        self.account_id = account.id
        self.createCard()

    """
    This method creates Card in the database
    :param: self
    :type: Card
    :returns: nothing
    """
    def createCard(self):
        query = 'INSERT INTO card (id, number, password, type, balance, gold, valid, "limit", account_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
        val = (self.id, self.number, self.password, self.type, self.balance, int (self.gold), int (self.valid), self.limit, self.account_id)
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
           number + str (random.randint(0,9))
        while self.numberExists(number) == True:
            newNumber = str (random.randint(0,9))
            for i in range(6):
                newNumber + str (random.randint(0,9))
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
        query = "UPDATE card SET balance = %s WHERE id = %s;"
        val = (self.balance, self.id)
        con.executeWithVal(query, val)

    """
    This method changes the Card gold status
    :param: self, gold
    :type: Card, bool
    :returns: nothing
    """
    def changeGold(self, gold):
        assert type(gold) is bool, "gold must be a bool!"
        if gold == self.gold:
            raise Exception("You have entered same gold status for a Card!")
        self.gold = gold
        query = "UPDATE card SET gold = %s WHERE id = %s;"
        val = (self.gold, self.id)
        con.executeWithVal(query, val)

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
               f"type: {self.type}, balance: {self.balance}, gold: {self.gold}, " \
               f"valid: {self.valid}, limit: {self.limit}, account_id: {self.account_id}"
