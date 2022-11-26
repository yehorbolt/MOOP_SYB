class Transfer:
    id = 0
    fromCard = ""
    toCard = ""
    amount = 0
    date = "default"
    type = "default"
    card_id = 0             # from which card (id) is transfer
    card_account_id = 0     # id of the account that has a card from which transfer takes place
    atm_id = 0              # id of the atm where transaction is taken
    atm_bank_id = 0         # bank id that has an atm
