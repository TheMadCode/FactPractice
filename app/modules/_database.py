import threading
import time
import json
from mysql.connector import connect
from mysql.connector import pooling

class Database:
    __slots__ = [
            'poll_name'
            'polling', 
    ]

    def __init__(self, database, poll_name):
        with open("./set_up.json") as json_file:
            self.polling = pooling.MySQLConnectionPool(
                pool_name=poll_name,
                pool_reset_session=True,
                database=database,
                autocommit=True,
                **json.load(json_file)["database"]
            )


    def add(self, inTable, columns, values):
        if type(columns) != type(""):
            columns = list(columns)
            for i in range(len(columns)):
                columns[i] = f"`{columns[i]}`"
            columns = ", ".join(columns)
        
        if type(values) != type(""):
            values = list(values)
            for i in range(len(values)):
                values[i] = f"'{values[i]}'"
            values = ", ".join(values)

        self.cursor.execute(self.SQL_INSERT % (inTable, f"({columns})", f"({values})"))        

    def get(self, columns, fromTable, findParams = None):
        """
            >>> First argument: columns\n
            >>> Second argument: fromTable\n
            >>> Third argument: findParams (optional)\n
        """
        if type(columns) != type(""):
            columns = ", ".join(columns)
            oneParam = False
        else:
            oneParam = True

        if findParams == None:
            self.cursor.execute(self.SQL_GET % (columns, fromTable))
        else:
            val = str(tuple(findParams.values())[0]).replace("'", "`")
            self.cursor.execute(f"{self.SQL_GET % (columns, fromTable)} WHERE (`{tuple(findParams.keys())[0]}` = '{val}')")
        
        resp = self.cursor.fetchall()

        if oneParam:
            resp = resp[0]

        if len(resp) == 1:
            return resp[0]
        else:
            return resp


    def update(self, row, withValues, inTable):
        """
            >>> First argument: row\n
            >>> Second argument: withValues\n
            >>> Third argument: inTable\n
        """
        val = str(tuple(row.values())[0]).replace("'", "`")
        for key, value in withValues.items():
            self.cursor.execute(f"update {inTable} SET `{key}` = '{value}' WHERE (`{tuple(row.keys())[0]}` = '{val}')")
    
    def fetch_from_db(self, cursor, name, data):
        cursor.callproc(name, data)
        for results in cursor.stored_results():
            return results.fetchall()

    def call_procedure(self, name, data:list=[]) -> list:
        connection = self.polling.get_connection()
        connection.set_charset_collation("utf8mb4", "utf8mb4_unicode_ci")
        cursor = connection.cursor(dictionary=True, buffered=True)
        response = self.fetch_from_db(cursor, name, data)
        cursor.close()
        connection.close()
        return response