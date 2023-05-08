from Web_Scraping import WebScraping
import sqlite3


class Database:
    def __init__(self, db_name, table_name):
        self.dataBase_name = db_name
        self.table_name = table_name
        self.web_scraped = WebScraping()

    def get_scraped_data(self):
        data = self.web_scraped.get_data()
        return data

    def connect(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print("Database created and successfully connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print(f'Error while connecting to sqlite {error}')

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def createTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)

            sqlite_create_table_query = f'''CREATE TABLE {self.table_name}(
                                            country TEXT, 
                                            carbon_emission REAL)'''

            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print('SQLite table created')
            cursor.close()

        except sqlite3.Error as error:
            print('Error while creating as a sqlite table', error)

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print('sqlite connection is closed.')

    def insert(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')

            data = self.get_scraped_data()
            for key, value in data.items():
                country = key
                carbon_emission = value
                sqlite_insert_query = f'''INSERT INTO {self.table_name}
                (country, carbon_emission) VALUES(?, ?)'''

                # Convert data into a tuple format
                data_tuple = (country, carbon_emission)
                cursor.execute(sqlite_insert_query, data_tuple)
                sqliteConnection.commit()
            print('File inserted successfully as into a table')
            cursor.close()

        except sqlite3.Error as error:
            print(f'Failed to insert data into sqlite table {error}')

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print(f'The sqlite connection is closed')

    def readTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print('connected to SQLite')
            sqlite_select_query = f"SELECT * from {self.table_name}"
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print(f'Total rows are: {len(records)}')
            print("Printing each row")

            for row in records:
                print(f'{row[0]}')
                print(f'{row[1]}')

            cursor.close()

        except sqlite3.Error() as error:
            print(f'Failed to read data from sqlite table {error}')

        finally:
            sqliteConnection.close()
            print('The SQLite connection is closed')

    def deleteRecord(self, name):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            # Deleting single record now
            sql_delete_query = f'''DELETE from {self.table_name} where country = {name}'''
            cursor.execute(sql_delete_query)
            sqliteConnection.commit()
            print("Record deleted successfully ")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("the sqlite connection is closed")
    def fetch(self):
        con = sqlite3.connect(self.dataBase_name)
        cursorObj = con.cursor()
        data = []
        sel = f"SELECT * from {self.table_name}"
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()

        carbon_dict = {}
        for row in rows:
            carbon_dict[row[0]] = row[1]

        return carbon_dict


s = Database('SQLite_Python.db', 'Database')
#s.get_scraped_data()
#s.connect()
#s.createTable()
#s.insert()
#s.readTable()
#print(s.fetch())
