from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for an user entity
"""
class User:
    id = int(1)
    login = str("default")
    password = str("default")

    """
    Constructor 
    :param timestamp: query
    :type timestamp: str 
    :returns: all the records in specific table in database
    :rtype: tuple
    """
    def __init__(self, login, password):
        assert type(login) is str, "Login must be a string!"
        assert type(password) is str, "Password must be a string!"
        assert self.checkLogin(login) == True, "This login is already used! Sign in or use another login!"
        assert password.__len__() >= 8, "Password must be longer than 7 symbols!"
        self.id = con.getLastId("user") + 1
        self.login = login
        self.password = password
        self.createUser()

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
        query = "UPDATE user SET password = %s WHERE id = %s;"
        val = (self.password, self.id)
        con.executeWithVal(query, val)

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
        return f"id: {self.id}, login: {self.login}, password: {self.password}"
