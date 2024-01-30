from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    def __init__(self, host, port, db_name, user, password):
        """
        Initialize the DatabaseConnection with connection parameters.

        Parameters:
        host (str): Database server host or IP.
        port (int): Database server port.
        db_name (str): Database name.
        user (str): Database user.
        password (str): Database password for the user.
        """
        self.host = host
        self.port = port
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = None

    @abstractmethod
    def connect(self):
        """
        Establish a connection to the database.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Close the connection to the database.
        """
        pass
