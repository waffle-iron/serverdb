import mysql.connector
from mysql.connector import Error

class dbm:
    self.username = username
    self.password = password
    def connect(self, username, password):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=curdb
                                                 user=username
                                                 password=password)
            if connection.is_connected():
                print("Connected!")
            else:
                return connection.is_connected()
        except Error as e:
            e = err
    def 
