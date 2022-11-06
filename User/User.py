class User:
  login = "default"
  password = "default"
  name = "default"
  surname = "default"

  def __init__(self, login, password):
    # check exception here
    self.login = login
    self.password = password

  def changePassword(self, newPassword):
      # check exception here
      if newPassword != 0:
          self.password = newPassword
