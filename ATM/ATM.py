from ConnectToDB import ConnectToDb as con

"""
    This class is responsible for an ATM entity 
"""
class ATM:
    id = int(0)
    address = str("default")
    bank_id = int(1)

    """
    Constructor
    :param: self, address, bank
    :type: ATM, str, Bank
    :returns: nothing
    """
    def __init__(self, address):
        assert type(address) is str, "Address must be a string!"
        assert self.checkAddress(address, self.bank_id) == True, "ATM with such address is already existing! Create an ATM with another address!"
        self.id = con.getLastId("atm") + 1
        self.address = address
        self.createAtm()

    """
    Constructor for restoring ATM
    :param: self, address, bank
    :type: ATM, str, Bank
    :returns: nothing
    """
    def restoreAtm(self, atmId, address, ):
        self.id = atmId
        self.address = address

    """
    Checks if ATM with address and bank_id given is already in a database
    :param: self, address, bank_id
    :type: ATM, str, int
    :returns: True or False 
    :rtype: bool
    """
    def checkAddress(self, address, bank_id):
        query = "SELECT * FROM atm WHERE address = '" + address + "' AND bank_id = '" + str (bank_id) + "';"
        res = con.executeReturn(query)
        if res.__len__() == 0:
            return True
        else:
            return False

    """
    Creates ATM in database
    :param: self
    :type: ATM
    :returns: nothing
    """
    def createAtm(self):
        query = "INSERT INTO atm (id, address, bank_id) VALUES (%s, %s, %s);"
        val = (self.id, self.address, self.bank_id)
        con.executeWithVal(query, val)

    """
    Changes address of the ATM
    :param: self, newAdress
    :type: ATM, str
    :returns: nothing
    """
    def changeAdress(self, newAddress):
        assert type(newAddress) is str, "newAddress must be a string!"
        newAddress = str(newAddress)  # converts newAddress (object) into str
        assert newAddress != self.address, "You have entered same ATM address!"
        assert newAddress.__len__() >= 1, "You can't change the address of the ATM on a new one with length < 1!"
        assert self.checkAddress(newAddress, self.bank_id) == True, "ATM with such address is already existing! Change ATM's address on another one!"
        self.address = newAddress
        self.updateAddress()

    """
    Updates address of the ATM in the database
    :param: self
    :type: ATM
    :returns: nothing
    """
    def updateAddress(self):
        query = "UPDATE atm SET address = %s WHERE id = %s;"
        val = (self.address, self.id)
        con.executeWithVal(query, val)

    """
    Deletes the ATM from the database
    :param: self
    :type: ATM
    :returns: nothing
    """
    def deleteAtm(self):
        query = "DELETE FROM atm WHERE id = " + str (self.id) + ";"
        con.execute(query)

    """
    Returns string representation of the ATM
    :param: self
    :type: ATM
    :returns: string representation
    :rtype: str
    """
    def __str__(self):
        return f"id: {self.id}, address: {self.address}, bank_id: {self.bank_id}"
