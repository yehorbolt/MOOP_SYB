# class that is responsible for the Bank
class Bank:
    id = 1
    name = "Monkey Bank"
    headquarters = "Kyiv"
    branch = "Main"
    atmlist = ()
    lastATMID = 0

    #add ATM to th bank
#    def addATM(self, ATM):

    #delete ATM to th bank
#    def delATM(self, ATM):

    #set last ATM id
    def setLastATMID(self, newid):
        self.lastATMID = newid

    #get last ATM id
    def пetLastATMID(self):
        return self.lastATMID
