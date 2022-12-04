class Transfer:
    id = int (0)
    fromCard = int (0)
    toCard = int (0)
    amount = float (0)
    date = str ("default")
    type = str ("default")
    card_id = int (0)             # from which card (id) is transfer
    card_account_id = int (0)     # id of the account that has a card from which transfer takes place
    atm_id = int (0)              # id of the atm where transaction is taken
    atm_bank_id = int (0)         # bank id that has an atm
