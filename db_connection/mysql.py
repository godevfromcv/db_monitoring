from db_connection.database import DatabaseConnection
import mysql.connector
from mysql.connector import Error


class MySQLConnection(DatabaseConnection):
    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.db_name,
                user=self.user,
                password=self.password
            )
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            raise

    def disconnect(self):
        """
        Close the connection to the MySQL database.
        """
        if self.connection.is_connected():
            self.connection.close()
