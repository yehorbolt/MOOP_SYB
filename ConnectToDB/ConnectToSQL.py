import mysql.connector

class ConnectToSQL:
  mydb = None
  mycursor = None

  def disconnect(self):
    self.mycursor.close()
    self.mydb.close()
    self.mycursor = None
    self.mydb = None

  def connect(self):
    self.mydb = mysql.connector.connect(
        host="bunu9twon1zilnedmecc-mysql.services.clever-cloud.com",
        user="uhdonzzoqdo00pjp",
        password="qWKPUK6GPDJ5WaR2vYsG",
        database="bunu9twon1zilnedmecc",
    )
    self.mycursor = self.mydb.cursor(buffered=True)

  def execute(self, SQLstring):
    self.mycursor.execute(SQLstring)
    self.mydb.commit()
    for x in self.mycursor:
        print(x)

  def fetch(self):
    return self.mycursor.fetchall()
