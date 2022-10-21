import ConnectToDB.ConnectToSQL as db

db.ConnectToSQL.connect(db)
select = "DELETE FROM user WHERE iduser = 1"
db.ConnectToSQL.execute(db, select)
print("---------------------------------------------")
select = "SELECT * FROM user"
db.ConnectToSQL.execute(db, select)

#Основний файл з запуском гри, atm_start.py запускає нашу систему MonkePal
