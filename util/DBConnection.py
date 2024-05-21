import pyodbc
from .PropertyUtil import PropertyUtil


class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            connection_string = PropertyUtil.getPropertyString()
            try:
                DBConnection.connection = pyodbc.connect(connection_string)
            except pyodbc.Error as e:
                print(f"Error while connecting to SQL database: {e}")
        return DBConnection.connection
