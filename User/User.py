import ConnectToDB.ConnectToDb as con
class User:
  id = 0
  login = "default"
  password = "default"

  def __init__(self, login, password):
    # check exception here
    self.login = login
    self.password = password
    #query = "INSERT INTO user (id, login, password) VALUES (1," + "'" + login + "','" + password + "');"
    query = "INSERT INTO user (login, password) VALUES ('" + login + "','" + password + "');"
    #query = "INSERT INTO user (id, login, password) VALUES (%s, %s, %s);"
    #val = (1, login, password)
    con.execute(query)

  def changePassword(self, newPassword):
      # check exception here
      if newPassword != 0:
          self.password = newPassword

u = User("login", "pass")
query = "select * from user"
#query = "show tables"
con.executePrint(query)
