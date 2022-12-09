import mysql.connector
from mysql.connector import Error

from ATM.ATM import ATM
from Bank.Bank import Bank
from User.User import User
from ATM.ATM import ATM

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
This method restores the data about Banks
:param: nothing
:returns: nothing
"""
def restoreBanks(self):
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
            record1 = tuple()
            record2 = tuple()
            for i in range(2):
                query = "SELECT * FROM bank WHERE id = " + str (i) + ";"
                cursor.execute(query)
                if i == 0:
                    record1 = tuple (cursor.fetchall())
                if i == 1:
                    record2 = tuple (cursor.fetchall())
            bank1 = Bank.restoreBank(record1[0][0], record1[0][1], record1[0][2], record1[0][3])
            bank2 = Bank.restoreBank(record2[0][0], record2[0][1], record2[0][2], record2[0][3])
            banks = tuple (bank1, bank2)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            return banks

"""
This method restores the data about Atms
:param: nothing
:returns: nothing
"""
def restoreAtms(self):
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
            record1 = tuple()
            record2 = tuple()
            record3 = tuple()
            record4 = tuple()
            record5 = tuple()
            record6 = tuple()
            for i in range(6):
                query = "SELECT * FROM atm WHERE id = " + str (i) + ";"
                cursor.execute(query)
                if i == 0:
                    record1 = tuple (cursor.fetchall())
                if i == 1:
                    record2 = tuple (cursor.fetchall())
                if i == 2:
                    record3 = tuple (cursor.fetchall())
                if i == 3:
                    record4 = tuple (cursor.fetchall())
                if i == 4:
                    record5 = tuple (cursor.fetchall())
                if i == 5:
                    record6 = tuple (cursor.fetchall())
            atm1 = ATM.restoreAtm(record1[0][0], record1[0][1], record1[0][2])
            atm2 = ATM.restoreAtm(record2[0][0], record2[0][1], record2[0][2])
            atm3 = ATM.restoreAtm(record3[0][0], record3[0][1], record3[0][2])
            atm4 = ATM.restoreAtm(record4[0][0], record4[0][1], record4[0][2])
            atm5 = ATM.restoreAtm(record5[0][0], record5[0][1], record5[0][2])
            atm6 = ATM.restoreAtm(record6[0][0], record6[0][1], record6[0][2])
            atms = tuple (atm1, atm2, atm3, atm4, atm5, atm6)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            return atms
