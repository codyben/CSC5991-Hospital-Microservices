import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Nick Advardo", 22, 2485984283, 12101))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Tim Leoroy", 41, 2487987283, 12102))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Colina Westwood", 19, 5860987393, 12103 ))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Samuel Johsnson", 51, 3137087804,12104))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Mathew Quinton", 77, 3132181290, 12105))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Erham Bienga", 39, 2489912283,12106))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Maxine Conti", 33, 2481287182,12107))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("alexandra Anquilla", 48, 5865906203, 12108))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Adriana Tevez", 28, 5861081293, 12109))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Karen Mcvault", 78, 5869312102, 1210))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Anthony Selvestor", 27, 3139872832, 1211))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Anushka Kumail", 61, 3139118083, 1212))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Juan Vaccino", 36, 2481207170, 1213))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Megan Advardo", 51, 2486583256, 1214))
mycursor.execute("INSERT INTO Patient_info (PATIENTname, PATIENTage, phoneNumber,  patientID) VALUES (%s,%S,%S, %S)", ("Olivia Tamina", 46, 5869321382, 1215))

mycursor.commit()




    
    
