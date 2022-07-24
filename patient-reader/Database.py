import mysql.connector
from PatientModel import PatientModel

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",  
) 

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",  
        )

    def transaction(self, query) -> tuple:
        cursor = self.db.cursor()
        try:
            query(cursor)
        except:
            # raise an exception
            cursor.close()
            return (False, ())
        results = cursor.fetchall()
        cursor.close()
        return results