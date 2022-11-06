import mysql.connector

db = mysql.connector.connect(
  user="severhin1",
  password="AVNS_6rTR6l_ji_IFCMJbuSj",
  host="db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com",
  port="25060",
  database="defaultdb",
)


mycursor = db.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


#Основний файл з запуском гри, atm_start.py запускає нашу систему MonkePal
