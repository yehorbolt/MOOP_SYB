# this class is responsible for user's account in the bank, 1 -> 1 (1 user has 1 account)
class Account:
  id = 0
  name = "default"
  surname = "default"
  number = 0
  status = "default"
  user_id = 0
  bank_id = 0

  def __init__(self, name, surname, status):
      # check exception here
      self.name = name
      self.surname = surname
      self.status = status
      self.number = self.generateNumber(name, surname, status)

  def changeName(self, name):
    # check exception here
      if name != 0:
        self.name = name

  def chaneSurname(self, surname):
      # exceptions here
        if surname != 0:
            self.surname = surname

  def chaneStatus(self, status):
      # exceptions here
        if status != 0:
            self.status = status

  def generateNumber(self, name, surname, status):
      # this method should generate a number for self account
        return 
