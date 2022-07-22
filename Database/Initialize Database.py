import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    
) 

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE HospitalServices ")
