from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for an user entity
"""
class User:
    id = int(0)
    login = str("default")
    password = str("default")
    money = float (0)

    """
    Constructor 
    :param: self, login, password, money
    :type: User, str, str, int
    :returns: nothing
    """
    def __init__(self, login, password, money, restore):
        assert type(login) is str, "Login must be a string!"
        assert type(password) is str, "Password must be a string!"
        assert type(money) is float or type(money) is int, "Money must be a float or an int!"
        if restore == False:
            assert self.checkLogin(login) == True, "This login is already used! Sign in or use another login!"
            assert password.__len__() >= 8, "Password must be longer than 7 symbols!"
            self.id = con.getLastId("user") + 1
            self.login = login
            self.password = password
            self.createUser()
        else:
            id = int (self.findUserId(login))
            self.restoreUser(id, login, password, money)


    """
    This method restored data about the user from the database
    :param: self, id, login, password, money
    :type: User, int, str, str, int
    :returns: nothing
    """
    def restoreUser(self, id, login, password, money):
            self.id = id
            self.login = login
            self.password = password
            self.money = money

    """
    This method finds a user id
    :param: self, login
    :type: User, str
    :returns: id
    :rtype: int
    """
    def findUserId(self, login):
        query = "SELECT id FROM user WHERE login = '" + str (login) + "';"
        return tuple (con.executeReturn(query)).__getitem__(0)[0]

    """
    Checks if User with login given is already in a database
    :param: self, login
    :type: User, str 
    :returns: True or False 
    :rtype: bool
    """
    def checkLogin(self, login):
        query = "SELECT * FROM user WHERE login = '" + login + "';"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return True
        else:
            return False

    """
    Creates user in database
    :param: self
    :type: User
    :returns: nothing
    """
    def createUser(self):
        query = "INSERT INTO user (id, login, password) VALUES (%s, %s, %s);"
        val = (self.id, self.login, self.password)
        con.executeWithVal(query, val)

    """
    Changes the password of the User
    :param: self, new password
    :type: User, str 
    :returns: nothing
    """
    def changePassword(self, newPassword):
        assert type(newPassword) is str, "newPassword must be a string!"
        newPassword = str(newPassword)  # converts newPassword (object) into str
        if newPassword == self.password:
            raise Exception("You have entered same password!")
        if newPassword.__len__() < 8:
            raise Exception("You can't change the password on a new one with length < 8!")
        self.password = newPassword
        self.updatePassword()

    """
    Update the password of the User in database
    :param: self
    :type: User
    :returns: nothing
    """
    def updatePassword(self):
        query = "UPDATE user SET password = %s WHERE id = %s;"
        val = (self.password, self.id)
        con.executeWithVal(query, val)

    """
    Changes the money of the User
    :param: self, new money
    :type: User, float/int
    :returns: nothing
    """
    def changeMoney(self, newMoney):
        assert type(newMoney) is float or type(newMoney) is int, "newMoney must be a float or an int!"
        assert newMoney >= 0, "newMoney must be more than -1"
        if newMoney == self.newMoney:
            raise Exception("You have entered same amount of money!")
        self.password = newMoney
        self.updateMoney()

    """
    Update amount of the money the User has in database
    :param: self
    :type: User
    :returns: nothing
    """
    def updateMoney(self):
        query = "UPDATE user SET money = %s WHERE id = %s;"
        val = (self.money, self.id)
        con.executeWithVal(query, val)

    """
    This method updates user balance
    :param: self
    :type: User
    :returns: nothing
    """
    def getMoneyDb(self):
        query = "SELECT money FROM user WHERE id = '" + str (self.id) + "';"
        records = con.executeReturn(query)
        self.money = records.__getitem__(0)

    """
    Deletes the User from the database
    :param: self
    :type: User 
    :returns: nothing
    """
    def deleteUser(self):
        query = "DELETE FROM user WHERE id = " + str (self.id) + ";"
        con.execute(query)

    """
    Returns string representation of the User 
    :param: self
    :type: User 
    :returns: string representation
    :rtype: str
    """
    def __str__(self):
        return f"id: {self.id}, login: {self.login}, password: {self.password}, money: {self.money}"
