import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="ehorb",
  password="BolotovVehor1",
  database="atm",
  auth_plugin='mysql_native_password'
)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

print("-------------------------------------")
mycursor.execute("show global variables like '%connections%'")



for x in mycursor:
  print(x)

#Основний файл з запуском гри, atm_start.py запускає нашу систему MonkePal

# if __name__ == '__main__':
#    print("Hello, my dear friend!");
