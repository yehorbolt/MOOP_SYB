import mysql.connector
from mysql.connector import Error


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
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


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
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


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
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
