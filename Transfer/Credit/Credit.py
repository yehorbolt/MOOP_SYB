from MOOP_SYB.Transfer import Transfer
import CreditSystem

class Credit(Transfer):
    id = 0
    fromCard = ""
    toCard = ""
    amount = 0
    date = "default"
    type = "default"
    leftToPay = 0           # left to pay for the credit
    bankInterest = 0        # bank interest
    card_id = 0             # from which card (id) is transfer
    card_account_id = 0     # id of the account that has a card from which transfer takes place
    atm_id = 0              # id of the atm where transaction is taken
    atm_bank_id = 0         # bank id that has an atm



    #use CreditSystem to check if the bank can give for a user a credit
    def checkIfValid(self):
        return CreditSystem(self.fromCard, self.toCard, self.amount, self.bankInterest)
