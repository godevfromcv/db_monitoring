def formatted_query(func):
    def wrapper(self, *args, **kwargs):
        query = func(self, *args, **kwargs)
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            results = cursor.fetchall()
            formatted_results = [dict(zip(columns, row)) for row in results]
            return formatted_results

    return wrapper
