import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()


mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable)VALUES (%s,%s,%s, %s)", ("Jalen Howard", 1010, "Monday-Friday", "6am - 2pm"))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Tim Madden", 1010, "Monday-Friday", "2pm - 10pm" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Tina Ardmound", 1010, "Monday-Friday", "10pm - 6am" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Megan Nisstrick", 1011, "Monday-Friday", "6am - 2pm" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Lisara Mcdougald", 1011, "Monday-Friday", "10pm - 6am" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Jason Queston", 1011, "Monday-Friday", "2pm - 10pm" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Marlin Dick", 1012, "Tuesday-Saturday", "6am - 2pm" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Namia Rocker", 1012, "Tuesday-Saturday", "10pm - 6am" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Venessa Eastwood", 1012, "Tuesday-Saturday", "2pm - 10pm" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Kevin Richalson", 1013, "Tuesday-Saturday", "6am - 2pm" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Stephen Nickora", 1013, "Tuesday-Saturday", "10pm - 6am" ))
mycursor.execute("INSERT INTO Ambulance(DriverName, AmbulanceNumber, AmbulanceDaysAvalible, AmbulanceTimeAvaliable) VALUES (%s,%s,%s, %s)", ("Liana Rose", 1013, "Tuesday-Saturday", "2pm - 10pm" ))


db.commit()