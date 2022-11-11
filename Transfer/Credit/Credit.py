from Transfer.Transfer import Transfer
from Transfer.Credit import CreditSystem

class Credit(Transfer):
    fromCard = ""
    toCard = ""
    amount = 0
    leftToPay = 0
    bankInterest = 0

    #use CreditSystem to check if the bank can give for a user a credit
    def checkIfValid(self):
        return CreditSystem(self.fromCard, self.toCard, self.amount, self.bankInterest)
