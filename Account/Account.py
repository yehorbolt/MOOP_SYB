from ConnectToDB import ConnectToDb as con

"""
    Execute the query in database and return the records from specific table
"""
class Account:
    id = int (0)
    name = str ("default")
    surname = str ("default")
    number = int (0)
    status = str ("default")
    user_id = int (0)
    bank_id = int (0)

    """
    Constructor 
    :param: self, name, surname, status
    :type: User, str, str, str
    :returns: nothing
    """
    def __init__(self, name, surname, status):
        # check exception here
        self.name = name
        self.surname = surname
        self.status = status
        self.number = self.generateNumber(name, surname, status)

    """
    This method changes name of the user in his account 
    :param: self, name
    :type: User, str
    :returns: nothing
    """
    def changeName(self, name):
        # check exception here
        if name != 0:
            self.name = name

    """
    This method changes surname of the user in his account 
    :param: self, surname
    :type: User, str
    :returns: nothing
    """
    def chaneSurname(self, surname):
        # exceptions here
        if surname != 0:
            self.surname = surname

    """
    This method changes status of the user in his account 
    :param: self, status
    :type: User, str
    :returns: nothing
    """
    def chaneStatus(self, status):
        # exceptions here
        if status != 0:
            self.status = status

    """
    This method generates the number of the user's account in the bank 
    :param: self
    :type: User
    :returns: number
    :rtype: int
    """
    def generateNumber(self):
        pass
