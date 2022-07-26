import time
import mysql.connector
from ExamModel import ExamModel
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
            print(e)
            # raise an exception
            cursor.close()
            return ()
        results = cursor.fetchall()
        cursor.close()
        return results

    def parse(self, row):
        if not row:
            return None
        name, medical_issues, department = row
        return ExamModel(
            name=name,
            issues=medical_issues,
            department=department
        ).serialize()