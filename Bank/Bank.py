from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for a bank entity 
"""
class Bank:
    id = int (0)
    name = str ("default")
    headquarters = str ("default")
    branch = str ("default")

    """
    Constructor
    :param: self, name, headquarters, branch
    :type: Bank, str, str, str
    :returns: nothing
    """
    def __init__(self, name, headquarters, branch):
        assert type(name) is str, "Name must be a string!"
        assert type(headquarters) is str, "Headquarters must be a string!"
        assert type(branch) is str, "Branch must be a string!"
        assert self.checkName(name) == True, "Bank with such name is already existing! Create a bank with another name!"
        self.id = con.getLastId("bank") + 1
        self.name = name
        self.headquarters = headquarters
        self.branch = branch
        self.createBank()


    """
    Checks if User with login given is already in a database
    :param: self, login
    :type: User, str 
    :returns: True or False 
    :rtype: bool
    """
    def checkName(self, name):
        name = str (name)
        query = "SELECT * FROM bank WHERE name = '" + name + "';"
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
    def createBank(self):
        query = "INSERT INTO bank (id, name, headquarters, branch) VALUES (%s, %s, %s, %s);"
        val = (self.id, self.name, self.headquarters, self.branch)
        con.executeWithVal(query, val)

    """
    Changes name of the bank
    :param: self, newName
    :type: Bank, str
    :returns: nothing
    """
    def changeName(self, newName):
        assert type(newName) is str, "newName must be a string!"
        newName = str(newName)  # converts newName (object) into str
        assert newName != self.name, "You have entered same bank name!"
        assert newName.__len__() >= 1, "You can't change the name of the bank on a new one with length < 1!"
        self.name = newName
        query = "UPDATE bank SET name = %s WHERE id = %s;"
        val = (self.name, self.id)
        con.executeWithVal(query, val)

    """
    Changes bank's headquarters 
    :param: self, headquarters
    :type: Bank, str
    :returns: nothing
    """
    def changeHeadquarters(self, newHeadquarters):
        assert type(newHeadquarters) is str, "newHeadquarters must be a string!"
        newHeadquarters = str(newHeadquarters)  # converts newHeadquarters (object) into str
        assert newHeadquarters != self.headquarters, "You have entered same bank headquarters!"
        assert newHeadquarters.__len__() >= 1, "You can't change the headquarters of the bank on a new one with length < 1!"
        self.headquarters = newHeadquarters
        query = "UPDATE bank SET headquarters = %s WHERE id = %s;"
        val = (self.headquarters, self.id)
        con.executeWithVal(query, val)

    """
    Changes bank's branch 
    :param: self, branch
    :type: Bank, str
    :returns: nothing
    """
    def changeBranch(self, newBranch):
        assert type(newBranch) is str, "newBranch must be a string!"
        newBranch = str(newBranch)  # converts newBranch (object) into str
        assert newBranch != self.name, "You have entered same branch of the bank!"
        assert newBranch.__len__() >= 1, "You can't change the branch of the bank on a new one with length < 1!"
        self.branch = newBranch
        query = "UPDATE bank SET branch = %s WHERE id = %s;"
        val = (self.branch, self.id)
        con.executeWithVal(query, val)

    """
    Deletes the Bank from the database
    :param: self
    :type: Bank 
    :returns: nothing
    """
    def deleteBank(self):
        query = "DELETE FROM bank WHERE id = " + str (self.id) + ";"
        con.execute(query)

    """
    Returns string representation of the Bank 
    :param: self
    :type: Bank
    :returns: string representation
    :rtype: str
    """
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, headquarters: {self.headquarters}, branch: {self.branch}"
