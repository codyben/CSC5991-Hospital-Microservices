import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()


mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Samuel Johsnson", "Broken Right Ankle", " Surgery"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Mathew Quinton", "Broken Left Sholder ", " Surgery" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Erham Bienga", "Broken Tibia", " Surgery"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Maxine Conti", "Brain Tumor", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("alexandra Anquilla", "Leg Paralisis","Neurology"  ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Adriana Tevez", "Brain Contusion", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Karen Mcvault", "Brain Cancer", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Anthony Selvestor", "Brain Contusion", "Neurology" ))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Anushka Kumail", "Heart Attack", "Emergency Room"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Juan Vaccino", "Severe Brain Contution", "Emergency Room"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Megan Advardo", "Punctured Lung", "Emergency Room"))
mycursor.execute("INSERT INTO  Patien_ExaminationResult (PATIENTname, medicalissues, DepartmentAssigned) VALUES (%s,%s,%s)", ("Olivia Tamina", "Neck Fracture", "Emergency Room"))

db.commit()
