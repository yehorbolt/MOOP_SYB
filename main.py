

print("-------------------------------------")
mycursor.execute("show global variables like '%connections%'")



for x in mycursor:
  print(x)

#Основний файл з запуском гри, atm_start.py запускає нашу систему MonkePal

# if __name__ == '__main__':
#    print("Hello, my dear friend!");
