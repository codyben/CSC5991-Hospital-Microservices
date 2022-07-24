import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()



mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Samuel Johsnson", " Ibuprofen", 20))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Mathew Quinton"," Advil" , 40 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Erham Bienga", " Ibuprofen", 30))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Maxine Conti","Adrenaline ", 20 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("alexandra Anquilla","NAcamprosate tablets", 25  ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Adriana Tevez","Amantadine ", 30 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Karen Mcvault", "Apomorphine", 51 ))
mycursor.execute("INSERT INTO  Patient_Medicines (PATIENTname, MedicineName, MedicineDose) VALUES (%s,%s,%s)", ("Anthony Selvestor","Amisulpride ", 31 ))


db.commit()