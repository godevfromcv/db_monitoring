import psycopg2
from db_connection.database import DatabaseConnection
from psycopg2.errors import Error
from utils.decorators import formatted_query


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        try:
            self.connection = psycopg2.connect(
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
        if self.connection:
            self.connection.close()

    def get_connection(self):
        return self.connection

    @formatted_query
    def get_active_connections(self):
        return """
        SELECT datname, count(*) FROM pg_stat_activity GROUP BY datname;
        """

    @formatted_query
    def get_index_usage(self):
        return """
        SELECT relname, indexrelname, idx_scan, idx_tup_read, idx_tup_fetch
        FROM pg_stat_user_indexes JOIN pg_indexes ON indexrelname = indexname;
        """

    @formatted_query
    def get_replication_status(self):
        return """
        SELECT * FROM pg_stat_replication;
        """

    @formatted_query
    def get_table_statistics(self):
        return """
        SELECT relname, seq_scan, seq_tup_read, idx_scan, idx_tup_fetch, n_tup_ins, n_tup_upd, n_tup_del, n_tup_hot_upd
        FROM pg_stat_user_tables;
        """
