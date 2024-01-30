import argparse

from data_analysis.generate_metrics_report import MetricsReporter
from db_connection.postgres import PostgreSQLConnection
from db_connection.mysql import MySQLConnection

# Define color codes for console output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to print an ASCII art header
def print_ascii_art_for_db_metrics():
    ascii_art = """ 
    ######  ######     #     # ####### ####### ######  ###  #####   #####  
    #     # #     #    ##   ## #          #    #     #  #  #     # #     # 
    #     # #     #    # # # # #          #    #     #  #  #       #       
    #     # ######     #  #  # #####      #    ######   #  #        #####  
    #     # #     #    #     # #          #    #   #    #  #             # 
    #     # #     #    #     # #          #    #    #   #  #     # #     # 
    ######  ######     #     # #######    #    #     # ###  #####   #####                                                                                                                                                                                     
    """
    print(Colors.HEADER + ascii_art + Colors.ENDC)

# Main function
def main():
    print_ascii_art_for_db_metrics()
    parser = argparse.ArgumentParser(
        description='Tool for finding long-running queries in PostgreSQL and MySQL databases.')

    parser.add_argument('--db_type', type=str, required=True,
                        help='Type of database. Choose "postgres" for PostgreSQL or "mysql" for MySQL.')
    parser.add_argument('--host', type=str, required=True, help='Database host, e.g., "localhost".')
    parser.add_argument('--database', type=str, required=False, help='Database name.')
    parser.add_argument('--user', type=str, required=True, help='Username for database access.')
    parser.add_argument('--password', type=str, required=True, help='Password for database access.')

    args = parser.parse_args()

    if args.db_type == 'postgres':
        db_connection = PostgreSQLConnection(host=args.host, port=5432, db_name=args.database, user=args.user,
                                             password=args.password)

    elif args.db_type == 'mysql':
        db_connection = MySQLConnection(host=args.host, port=3306, db_name=args.database, user=args.user,
                                        password=args.password)
    else:
        print(Colors.FAIL + "Unsupported database type" + Colors.ENDC)
        return

    try:
        db_connection.connect()
        print(Colors.OKGREEN + "Connected to the database" + Colors.ENDC)
        reporter = MetricsReporter(db_connection)
        reporter.generate_report()
        get_active_connections = db_connection.get_active_connections()
        print("Query Performance:")
        for row in get_active_connections:
            print(row)

        get_index_usage = db_connection.get_index_usage()
        print("Index Usage:")
        for row in get_index_usage:
            print(row)

        get_replication_status = db_connection.get_replication_status()
        print("Replication Status:")
        for row in get_replication_status:
            print(row)

        get_table_statistics = db_connection.get_table_statistics()
        print("Table Statistics:")
        for row in get_table_statistics:
            print(row)

    except Exception as e:
        print(Colors.FAIL + f"Error executing query: {e}" + Colors.ENDC)
    finally:
        db_connection.disconnect()
        print(Colors.WARNING + "Disconnected from the database" + Colors.ENDC)

if __name__ == "__main__":
    main()
