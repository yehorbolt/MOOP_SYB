import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySQLPass_11",
  database="atm",
  auth_plugin="mysql_native_password"
)

mycursor = db.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


#Основний файл з запуском гри, atm_start.py запускає нашу систему MonkePal

# if __name__ == '__main__':
#    print("Hello, my dear friend!");
