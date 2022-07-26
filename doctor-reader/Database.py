import time
import mysql.connector
from DoctorModel import DoctorModel
from constants import MYSQL_CONNECT_OPTIONS

class Database:
    def __init__(self):
        self.connect()
    def connect(self, retries=10):
        try:
            while retries > 0:
                try:
                    self.db = mysql.connector.connect(**MYSQL_CONNECT_OPTIONS)
                    retries = -1
                    print("DB has been initialized.")
                except mysql.connector.errors.DatabaseError:
                    retries -= 1
                    time.sleep(2)
        except:
            print("Failed to init db")
    def transaction(self, query) -> tuple:
        cursor = self.db.cursor()
        try:
            query(cursor)
        except Exception as e:
            print(e, flush=True)
            # raise an exception
            cursor.close()
            return ()
        results = cursor.fetchall()
        cursor.close()
        return results

    def parse(self, row):
        if not row:
            return None
        name, phone, field, present, times = row
        return DoctorModel(
            name=name,
            phone=phone,
            field=field,
            times=times,
            present=present
        ).serialize()