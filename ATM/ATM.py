import Bank

# class that is responsible for ATMs
class ATM:
    id = 0
    adress = "default"
    bank_id = 0

    def __init__(self, id, adress):
        self.id = id
        self.adress = adress

    #changes adress
    def changeAdress(self, adress):
        if (adress != 0 & self.adress != adress):
            self.adress = adress

    def updateLastId(Bank, id):
        Bank = id

    #prints ui output
    # def printOutput(self):
    #   print(uiOutput)

    #updates id if other atm was deleted
    #def updateId(self, id):
    #work with DB here
