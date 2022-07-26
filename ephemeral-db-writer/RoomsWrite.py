import mysql.connector
from constants import MYSQL_CONNECT_OPTIONS

db = mysql.connector.connect(**MYSQL_CONNECT_OPTIONS)
mycursor = db.cursor()

mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Nick Advardo", 101, "X-Ray" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Tim Leoroy", 102, "X-Ray" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Colina Westwood", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Samuel Johsnson", 104, " Surgery"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Mathew Quinton", 105, " Surgery" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Erham Bienga", 106, " Surgery"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Maxine Conti", 107, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("alexandra Anquilla", 108,"Neurology"  ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Adriana Tevez", 109, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Karen Mcvault", 110, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Anthony Selvestor", 111, "Neurology" ))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Anushka Kumail", 112, "Emergency Room"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Juan Vaccino", 113, "Emergency Room"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Megan Advardo", 114, "Emergency Room"))
mycursor.execute("INSERT INTO  Patient_Roominfo (PATIENTname, RoomNumber, Department) VALUES (%s,%s,%s)", ("Olivia Tamina", 115, "Emergency Room"))

db.commit()

