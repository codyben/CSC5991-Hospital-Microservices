import mysql.connector
from constants import MYSQL_CONNECT_OPTIONS

db = mysql.connector.connect(**MYSQL_CONNECT_OPTIONS)

mycursor = db.cursor()


mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Nick Advardo", 101, "X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Tim Leoroy", 102, "X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Colina Westwood", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Samuel Johsnson", 101, " X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Mathew Quinton", 102, " X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Erham Bienga", 103, " Ultra-Sound"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Maxine Conti", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("alexandra Anquilla", 103,"Ultra-Sound"  ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Adriana Tevez", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Karen Mcvault", 103, "Ultra-Sound" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Anthony Selvestor", 102, "X-Ray" ))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Anushka Kumail", 101, "X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Juan Vaccino", 102, "X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Megan Advardo", 101, "X-Ray"))
mycursor.execute("INSERT INTO  Patien_DAIGNOSTICS (PATIENTname, procedureRoomNumber, ProcedureRAN) VALUES (%s,%s,%s)", ("Olivia Tamina", 103, "Ultra-Sound"))

db.commit()
