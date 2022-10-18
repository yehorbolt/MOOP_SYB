class User:
  login = "default"
  password = "default"

  def User(self, login, password):
#    if login == null || password == null:
#        throw
    self.login = login
    self.password = password

  def changePassword(self, newPassword):
      if newPassword != 0:
          self.password = newPassword


