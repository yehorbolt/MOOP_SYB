import mysql.connector
from mysql.connector import Error
from User.User import User
from Account.Account import *
from Card.Card import *

"""
Get the last id inserted in the database.
:param: table name
:type: str 
:returns: number 
:rtype: int 
"""
def getLastId(table):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT id FROM " + table + ";"
            cursor.execute(query)
            records = tuple(cursor.fetchall())
            if records.__len__() == 0:
                return 0
            else:
                return records.__getitem__(-1)[-1]

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()


"""
Execute the query in database
:param: query
:type: str 
:returns: nothing 
"""
def execute(query):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()


"""
Execute the query in database
:param: query, values
:type: str, int/float/str 
:returns: nothing 
"""
def executeWithVal(query, values):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query, values)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()


"""
Execute the query in database and return the records from specific table
:param: query
:type: str 
:returns: all the records in specific table in database
:rtype: tuple
"""
def executeReturn(query):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            records = tuple(cursor.fetchall())

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            return records


"""
Execute the query in database and print the records from the specific table in the database
:param: query
:type: str 
:returns: nothing
"""
def executePrint(query):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Data: ", records)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()

"""
This method restores data about the User
:param: self, login
:type: self, str
:returns: User
"""
def restoreUser(login):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT * FROM user WHERE login = '" + str (login) + "';"
            cursor.execute(query)
            record = tuple (cursor.fetchall())
            user = User(record.__getitem__(0)[0], record.__getitem__(0)[1], record.__getitem__(0)[2], record.__getitem__(0)[3], True)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            return user

"""
This method restores data about the Account
:param: self
:returns: Account
"""
def restoreAccount(user_id):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT * FROM account WHERE user_id = '" + str (user_id) + "';"
            cursor.execute(query)
            record = tuple (cursor.fetchall())
            account = Account(record.__getitem__(0)[0], record.__getitem__(0)[1], record.__getitem__(0)[2], record.__getitem__(0)[3], user_id, True)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            return account

"""
This method restores data about the cards 
:param: nothing
:returns: cards 
:rtype: tuple
"""
def restoreCards(account_id):
    try:
        connection_config_dict = {
            'user': 'severhin1',
            'password': 'AVNS_6rTR6l_ji_IFCMJbuSj',
            'host': 'db-mysql-lon1-41175-do-user-12692486-0.b.db.ondigitalocean.com',
            'port': '25060',
            'database': 'defaultdb',
        }
        connection = mysql.connector.connect(**connection_config_dict)

        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT * FROM card WHERE account_id = '" + str (account_id) + "';"
            cursor.execute(query)
            record = tuple (cursor.fetchall())
            for i in record:
                cards = Card(record.__getitem__(i)[0], record.__getitem__(i)[1], record.__getitem__(i)[2], record.__getitem__(i)[3], record.__getitem__(i)[4],  True,)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            return tuple (cards)
