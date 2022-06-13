import mysql.connector

class SqlDatabase:
    """
    Admbk databse connection
    """
    def __init__(self, query : str):
        self.query = query

    def drop_table(self):
        """
        Drops table in sql
        """
        try:
            connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
            cursor = connection.cursor()
            mySql_query = self.query
            cursor.execute(mySql_query)
            connection.commit()
        except mysql.connector.Error as error:
            print("Failed to drop MySQL table {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    def db_ddl(self):
        """
        Executes ddl file
        """
        try:
            connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                    user='s206016',
                                                    password='tgbF5PriPdYWNJquI2MvL')
            cursor = connection.cursor()
            with open(self.query) as f: #PATH for ADMBKddl.sql
                 cursor.execute(f.read(), multi=True)        
        except mysql.connector.Error as error:
                     print("Failed to excecute MySQL table {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    def db_dml(self):
        """
        Executes dml file with courses
        """
        try:
                    connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                        database='s206016',
                                                        user='s206016',
                                                        password='tgbF5PriPdYWNJquI2MvL')
                    cursor = connection.cursor()
                    with open(self.query) as v:
                        query = v.read().strip()
                        cursor.execute(f'''{query}''', multi=True)
                    connection.commit()
        except mysql.connector.Error as error:
                    print("Failed to insert into MySQL table {}".format(error))