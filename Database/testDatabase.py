import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices"
) 

mycursor = db.cursor()

mycursor.execute("DESCRIBE Patient_info")
for x in mycursor:
    print(x)