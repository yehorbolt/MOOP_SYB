from Transfer.Transfer import Transfer
from multiprocessing import Process
from datetime import datetime, timedelta

"""
    This class is responsible for a Daemon entity
"""
class Daemon(Transfer):
    id = int (0)
    fromCard = int (0)
    toCard = int (0)
    amount = float (0)
    date = str ("default")
    type = str ("daemon")
    frequency = int (0)
    nextDate = str (0)
    process = 0
    increase = bool (0)
    active = bool (1)
    card_id = int (0)             # from which card (id) is transfer
    card_account_id = int (0)     # id of the account that has a card from which transfer takes place
    atm_id = int (1)              # id of the atm where transaction is taken
    atm_bank_id = int (1)         # bank id that has an atm

    """
    Constructor
    :param: self, fromCard, toCard, amount, date, transferType, card_id, card_account_id, atm_id, atm_bank_id
    :type: Credit, int, int, float/int, date, str, int, int, int, int
    :returns: nothing
    """
    def __init__(self, fromCard, toCard, amount, frequency, increaseMoney,card_id, card_account_id):
        super(Transfer, self).__init__(fromCard, toCard, amount, "daemon",  0, frequency, card_id, card_account_id)
        assert type(increaseMoney) == bool, "You must give a bool as one of the parameters that will be responsible for increasing or decreasing card balance!"
        self.increase = increaseMoney
        if self.increase == False: # for checking card
            self.nextDate = datetime.strptime(self.getTime(), "%Y-%m-%d %H:%M:%S") + timedelta(minutes=self.frequency)
            self.process = Process(target=self.transferMoney(), daemon=True)
            self.process.start()
        if self.increase == True: # for savings card
            self.nextDate = datetime.strptime(self.getTime(), "%Y-%m-%d %H:%M:%S") + timedelta(minutes=self.frequency)
            self.process = Process(target=self.getMoney(), daemon=True)
            self.process.start()

    """
    This is the task that will be runned by Daemon process
    :param:self, nextDate
    :type: Daemon, date
    :returns: nothing
    """
    def transferMoney(self):
        date = self.getTime()
        if date == self.nextDate:
            if self.enoughMoney(self.fromCard, self.amount):
                self.changeBalance(self.fromCard, self.amount, False)
                self.changeBalance(self.toCard, self.amount, True)
                self.nextDate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=self.frequency)
            else:
                self.process.daemon = False
                self.process.terminate()


    """
    This is the task that will be runned by Daemon process
    :param:self, nextDate
    :type: Daemon, date
    :returns: nothing
    """
    def getMoney(self):
        date = self.getTime()
        if date == self.nextDate:
            self.amount = self.amount * 1.08
            self.changeBalance(self.fromCard, self.amount, True)
            self.nextDate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=self.frequency)

    """
    This is the task that will be runned by Daemon process
    :param:self, nextDate
    :type: Daemon, date
    :returns: nothing
    """
    def increaseBalance(self):
        date = self.getTime()
        if date == self.nextDate:
            self.changeBalance(self.fromCard, self.toCard, self.amount, True)
            self.nextDate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=self.frequency)

    """
    This method changes Frequency of the daemon
    :param: self, newFrequency
    :type: Daemon, float/int
    :returns: nothing
    """
    def changeFrequency(self, newFrequency):
        assert type(newFrequency) == float or int, "You can't change frequency of the Daemon, if you don't enter float or int!"
        self.frequency = newFrequency
