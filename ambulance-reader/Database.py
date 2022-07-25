import time
import mysql.connector
from AmbulanceModel import AmbulanceModel

class Database:
    def __init__(self):
        self.connect()
    def connect(self, retries=10):
        try:
            while retries > 0:
                try:
                    self.db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="root",  
                    )
                except mysql.connector.errors.DatabaseError:
                    retries -= 1
                    time.sleep(2)
        except:
            print("Failed to init db")
        print("DB has been initialized.")
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

    def parse(self, row):
        if not row:
            return None
        name, number, days, times = row
        return AmbulanceModel(
            name=name,
            number=number,
            days_available=days,
            times_available=times
        ).serialize()