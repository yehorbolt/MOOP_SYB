# class that is responsible for the Bank
class Bank:
    id = int (0)
    name = str ("Monkey Bank")
    headquarters = str ("Kyiv")
    branch = str ("Main")

    #change name of the bank
    def changeName(self, newName):
        if newName != 0 & self.name != newName:
            self.name = newName;

    #add ATM to th bank
    def changeHeadquarters(self, headquarters):
        if headquarters != 0 & self.headquarters != headquarters:
            self.headquarters = headquarters;

    #add ATM to th bank
#    def addATM(self, ATM):

    #delete ATM to th bank
#    def delATM(self, ATM):
