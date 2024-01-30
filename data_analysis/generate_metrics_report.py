import matplotlib.pyplot as plt
import pandas as pd


class MetricsReporter:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def generate_report(self):
        active_connections = self.db_connection.get_active_connections()

        self.create_chart(active_connections, 'Active Connections', 'active_connections.png')

    def create_chart(self, data, title, filename):
        df = pd.DataFrame(data)
        df.plot(kind='bar')
        plt.title(title)
        plt.savefig(filename)
