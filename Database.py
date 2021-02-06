import sqlite3

from Log import *

class Database:

    def createTable(self):

        try:

            self.sqliteConnection = sqlite3.connect('sql_save_login.db')
            self.sqlite_create_table_query = '''CREATE TABLE SaveLogin (
                                            id INTEGER PRIMARY KEY,
                                            login TEXT NOT NULL,
                                            password TEXT NOT NULL,
                                            description TEXT NOT NULL);'''
            self.cursor = self.sqliteConnection.cursor()
            Log("Connected to sqlite")
            self.cursor.execute(self.sqlite_create_table_query)
            self.sqliteConnection.commit()
            Log("SQLite table created")
            self.cursor.close()

        except sqlite3.Error as error:

            Log(error)

    def dropTable(self):

        try:

            self.sqliteConnection = sqlite3.connect('sql_save_login.db')
            self.sqlite_drop_table_query = '''DROP TABLE SaveLogin;'''

            self.cursor = self.sqliteConnection.cursor()
            Log("Connected to sqlite")
            self.cursor.execute(self.sqlite_drop_table_query)
            self.sqliteConnection.commit()
            Log("SQLite delete table")
            self.cursor.close()

        except sqlite3.Error as error:

            Log(error)

    def insertLogin(self, login, password, description):

        try:
            self.sqliteConnection = sqlite3.connect('sql_save_login.db')
            self.sqlite_insert_table_query = '''INSERT
                                                INTO
                                                SaveLogin
                                                (login, password, description)
                                                VALUES
                                                ('{}', '{}', '{}');'''.format(
                                                login,
                                                password,
                                                description)

            self.cursor = self.sqliteConnection.cursor()
            Log("Connected to sqlite")
            self.cursor.execute(self.sqlite_insert_table_query)
            self.sqliteConnection.commit()
            Log("SQLite insert value")
            self.cursor.close()
        except sqlite3.Error as error:

            Log(error)

    def readLogin(self):
        try:

            self.sqliteConnection = sqlite3.connect('sql_save_login.db')
            self.cursor = self.sqliteConnection.cursor()
            Log("Connected to sqlite")

            self.sqlite_select_query = """SELECT * from SaveLogin"""
            self.cursor.execute(self.sqlite_select_query)
            self.records = self.cursor.fetchall()

            print("Quantidade de logins: [{}]".format(len(self.records)))
            for row in self.records:
                print("\n")
                print("id: ", row[0])
                print("login: ", row[1])
                print("password: ", row[2])
                print("description: ", row[3])
                print("\n")

            self.cursor.close()

        except sqlite3.Error as error:

            Log(error)
