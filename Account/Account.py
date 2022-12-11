from ConnectToDB import ConnectToDb as con
import random

"""
    This class is responsible for an Account entity
"""
class Account:
    id = int (0)
    name = str ("default")
    surname = str ("default")
    number = int (0)
    status = str ("default")
    user_id = int (0)
    bank_id = int (1)

    """
    Constructor 
    :param: self, name, surname, status, user_id, bank_id
    :type: Account, str, str, str, int, int
    :returns: nothing
    """
    def __init__(self, name, surname, status, user_id, restore):
        assert type(name) is str, "Name must be a string!"
        assert type(surname) is str, "Surname must be a string!"
        assert type(status) is str, "Status must be a string!"
        assert type(user_id) is int, "You must give int that is user_id!"
        assert self.validName(name) == True, "Name is invalid! Enter the valid one"
        assert self.validSurname(surname) == True, "Surname is invalid! Enter the valid one"
        assert self.validStatus(status) == True, "Stauts is invalid! Enter the valid one"
        if restore == False:
            self.id = con.getLastId("account") + 1
            self.name = name
            self.surname = surname
            self.number = self.generateNumber()
            self.status = status
            self.user_id = int (user_id)
            self.createAccount()
        else:
            id = self.findAccountId(user_id)
            number = self.findAccountNumber(user_id)
            self.restoreAccount(id, name, surname, number, status, user_id)

    """
    This method finds an account id
    :param: self, user_id
    :type: Account, int
    :returns: id
    :rtype: int
    """
    def findAccountId(self, user_id):
        query = "SELECT id FROM account WHERE user_id = '" + str (user_id) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    This method finds an account number
    :param: self, user_id
    :type: Account, int
    :returns: id
    :rtype: int
    """
    def findAccountNumber(self, user_id):
        query = "SELECT number FROM account WHERE user_id = '" + str (user_id) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    Constructor for restoring Account
    :param: self, id, name, surname, status, user_id, bank_id
    :type: Account, int, str, str, str, int, int
    :returns: nothing
    """
    def restoreAccount(self, id, name, surname, number, status, user_id):
        self.id = id
        self.name = name
        self.surname = surname
        self.number = number
        self.status = status
        self.user_id = user_id

    """
    Creates Account in database
    :param: self
    :type: Account 
    :returns: nothing
    """
    def createAccount(self):
        query = "INSERT INTO account (id, name, surname, number, status, user_id, bank_id) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        val = (self.id, self.name, self.surname, self.number, self.status, self.user_id, self.bank_id)
        con.executeWithVal(query, val)


    """
    This method checks the name of the user in his Account 
    :param: self, name
    :type: Account, str
    :returns: True or False (if name has no number -> True, else -> False)
    :rtype: bool
    """
    def validName(self, name):
        return name.isalpha()

    """
    This method checks the surname of the user in his Account 
    :param: self, name
    :type: Account, str
    :returns: nothing
    """
    def validSurname(self, surname):
        return surname.isalpha()

    """
    This method checks the status of the user in his Account 
    :param: self, name
    :type: Account, str
    :returns: nothing
    """
    def validStatus(self, status):
        if status == "working" or status == "workless":
            return True
        else:
            return False

    """
    This method changes name of the user in his Account 
    :param: self, name
    :type: Account, str
    :returns: nothing
    """
    def changeName(self, newName):
        assert type(newName) is str, "newName must be a string!"
        newName = str(newName)  # converts newName (object) into str
        assert self.validName(newName) == True, "Name can't have numbers in it!"
        assert newName != self.name, "You have entered same user name!"
        assert newName.__len__() >= 1, "You can't change the name of the user on a new one with length < 1!"
        self.name = newName
        self.updateName()

    """
    This method updates name of the Account in the database
    :param: self
    :type: Account
    :returns: nothing
    """
    def updateName(self):
        query = "UPDATE account SET name = %s WHERE id = %s;"
        val = (self.name, self.id)
        con.executeWithVal(query, val)

    """
    This method changes surname of the user in his Account 
    :param: self, surname
    :type: Account, str
    :returns: nothing
    """
    def changeSurname(self, newSurname):
        assert type(newSurname) is str, "newSurname must be a string!"
        newSurname = str(newSurname)  # converts newName (object) into str
        assert self.validSurname(newSurname) == True, "Surname can't have numbers in it!"
        assert newSurname != self.surname, "You have entered same user surname!"
        assert newSurname.__len__() >= 1, "You can't change the surname of the user on a new one with length < 1!"
        self.surname = newSurname
        self.updateSurname()

    """
    This method updates surname of the Account in the database
    :param: self
    :type: Account
    :returns: nothing
    """
    def updateSurname(self):
        query = "UPDATE account SET surname = %s WHERE id = %s;"
        val = (self.surname, self.id)
        con.executeWithVal(query, val)


    """
    This method changes status of the user in his Account 
    :param: self, status
    :type: Account, str
    :returns: nothing
    """
    def changeStatus(self, newStatus):
        assert type(newStatus) is str, "newStatus must be a string!"
        newStatus = str(newStatus)  # converts newName (object) into str
        assert self.validStatus(newStatus) == True, "Status you've entered is wrong!"
        assert newStatus != self.status, "You have entered same user status!"
        self.status = newStatus
        self.updateStatus()

    """
    This method updates status of the Account in the database
    :param: self
    :type: Account
    :returns: nothing
    """
    def updateStatus(self):
        query = "UPDATE account SET status = %s WHERE id = %s;"
        val = (self.status, self.id)
        con.executeWithVal(query, val)

    """
    This method generates the number of the user's account in the bank 
    :param: self
    :type: Account
    :returns: number
    :rtype: int
    """
    def generateNumber(self):
        number = str (random.randint(0,9))
        for i in range(6):
           number += str (random.randint(0,9))
        while self.numberExists(number) == True:
            newNumber = str (random.randint(0,9))
            for i in range(6):
                newNumber += str (random.randint(0,9))
            number = newNumber
        return number

    """
    This method checks if the account number exists in the database  
    :param: self, number
    :type: Account, int
    :returns: True or False
    :rtype: bool
    """
    def numberExists(self, number):
        query = "SELECT * FROM account WHERE number = '" + number + "';"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return False
        else:
            return True

    """
    Deletes the Account from the database
    :param: self
    :type: Account
    :returns: nothing
    """
    def deleteAccount(self):
        query = "DELETE FROM account WHERE id = " + str (self.id) + ";"
        con.execute(query)

    """
    Returns string representation of the Account 
    :param: self
    :type: Account
    :returns: string representation
    :rtype: str
    """
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, surname: {self.surname}, number: {self.number}, status: {self.status}, user_id: {self.user_id}, bank_id: {self.bank_id}"
