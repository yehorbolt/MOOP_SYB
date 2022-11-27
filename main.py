import mysql.connector
import os

db = mysql.connector.connect(
    host="bunu9twon1zilnedmecc-mysql.services.clever-cloud.com",
    user="uhdonzzoqdo00pjp",
    password="qWKPUK6GPDJ5WaR2vYsG",
    database="bunu9twon1zilnedmecc",
)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

print("-------------------------------------")
mycursor.execute("show global variables like '%connections%'")

for x in mycursor:
    print(x)

# Основний файл з запуском гри, atm_start.py запускає нашу систему MonkePal

# if __name__ == '__main__':
#    print("Hello, my dear friend!");
