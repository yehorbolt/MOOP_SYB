import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error
from User.User import *
from Account.Account import *
from Card.Card import *



connected = False
connection = ""
connection_config_dict= ""

"""
Connection to database.
"""
def db_connect():
    global connected
    global connection
    global connection_config_dict
    load_dotenv()
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DATABASE = os.getenv('DATABASE')
    connection_config_dict = {
        'user': USER,
        'password': PASSWORD,
        'host': HOST,
        'port': PORT,
        'database': DATABASE,
    }
    try:
        connection = mysql.connector.connect(**connection_config_dict)
        connected = True
    except Exception as e:
        print(e)



def getLastId(table):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            query = "SELECT id FROM " + table + ";"
            cursor.execute(query)
            records = tuple(cursor.fetchall())
            if records.__len__() == 0:
                return 0
            else:
                return records.__getitem__(-1)[-1]
            connection.commit()
            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)


"""
Execute the query in database
:param: query
:type: str 
:returns: nothing 
"""
def execute(query):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)


"""
Execute the query in database
:param: query, values
:type: str, int/float/str 
:returns: nothing 
"""
def executeWithVal(query, values):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)


"""
Execute the query in database and return the records from specific table
:param: query
:type: str 
:returns: all the records in specific table in database
:rtype: tuple
"""
def executeReturn(query):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            cursor.execute(query)
            records = tuple(cursor.fetchall())
            connection.commit()
            cursor.close()
            return records

    except Error as e:
        print("Error while connecting to MySQL", e)


"""
Execute the query in database and print the records from the specific table in the database
:param: query
:type: str 
:returns: nothing
"""
def executePrint(query):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Data: ", records)
            connection.commit()
            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)

"""
This method restores data about the User
:param: self, login
:type: self, str
:returns: User
"""
def restoreUser(login):
    global connected
    global connection
    try:
        if connected:
            cursor = connection.cursor()
            query = "SELECT * FROM user WHERE login = '" + str (login) + "';"
            cursor.execute(query)
            record = tuple (cursor.fetchall())
            data = [record.__getitem__(0)[1], record.__getitem__(0)[2], record.__getitem__(0)[3], True]
            connection.commit()
            cursor.close()
            return data

    except Error as e:
        print("Error while connecting to MySQL", e)

"""
This method restores data about the Account
:param: self
:returns: Account
"""
def restoreAccount(user_id):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            query = "SELECT * FROM account WHERE user_id = '" + str (user_id) + "';"
            cursor.execute(query)
            record = tuple (cursor.fetchall())
            account = Account(record.__getitem__(0)[1], record.__getitem__(0)[2], record.__getitem__(0)[4], user_id, True)
            connection.commit()
            cursor.close()
            return account

    except Error as e:
        print("Error while connecting to MySQL", e)

"""
This method restores data about the cards 
:param: nothing
:returns: cards 
:rtype: tuple
"""
def restoreCards(account_id):
    global connected
    global connection
    try:

        if connected:
            cursor = connection.cursor()
            query = "SELECT * FROM card WHERE account_id = '" + str (account_id) + "';"
            cursor.execute(query)
            record = tuple (cursor.fetchall())
            cards = list()
            c = 0
            for i in record:
                password = i[2]
                type = i[3]
                if type == "checking":
                    from Card.Checking import Checking
                    c = Checking(password, type, account_id,  True)
                if type == "credit":
                    from Card.Credit import Credit
                    c = Credit(password, type, account_id,  True)
                if type == "savings":
                    from Card.Savings import Savings
                    c = Savings(password, type, account_id,  True)
                cards.append(c)
            connection.commit()
            cursor.close()
            return cards

    except Error as e:
        print("Error while connecting to MySQL", e)
