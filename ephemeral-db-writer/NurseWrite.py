import mysql.connector
from constants import MYSQL_CONNECT_OPTIONS

db = mysql.connector.connect(**MYSQL_CONNECT_OPTIONS)

mycursor = db.cursor()

mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Sarah", 5865431234, "Neurologists ", "Monday-Friday", "8:00am - 4:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Micheale", 5863132489, "Radiologists", "Monday-Friday", "10:00am - 6:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Anushka", 5869456789, "Emergency Medicine Specialists ", "Wednessday-Saturday", "6:00am - 2:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Choudry", 586098765, "orthopedic", "Wednessday-Saturday", "8:00pm - 4:00 am"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Nick", 5867129772, "Internists", "Monday-Friday", "12:00pm - 8:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Amit", 5868543421, "Oncologists", "Monday-Friday", "11:00am - 7:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurs Mishra", 5867789076, "Neurologists", "Monday-Friday", "8:00am - 4:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Tina", 5861109022, "Radiologists", "Monday-Friday", "10:00am - 6:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse March", 5861235231, "Emergency Medicine Specialists", "Wednessday-Saturday", "6:00am - 2:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse June", 5860872312, "orthopedic", "Wednessday-Saturday", "8:00pm - 4:00 am"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse April", 5867678753, "Internists", "Monday-Friday", "12:00pm - 8:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Koleta", 5862123221, "Oncologists", "Monday-Friday", "11:00am - 7:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Anthony", 5869879098, "Neurologists", "Monday-Friday", "8:00am - 4:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Mishra", 5867645341, "Radiologists", "Monday-Friday", "10:00am - 6:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Jose", 5862345787, "Emergency Medicine Specialists", "Wednessday-Saturday", "6:00am - 2:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Alex", 5862332158, "orthopedic", "Wednessday-Saturday", "8:00pm - 4:00 am"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Cameron", 5860908731, "Internists", "Monday-Friday", "12:00pm - 8:00 pm"))
mycursor.execute("INSERT INTO Nurse (NURSEname, NURSEphone, NURSEfield,  NURSEdaysPresent, NURSEtimePresent) VALUES (%s,%s,%s, %s, %s)", ("Nurse Edward", 5861190639, "Oncologists", "Monday-Friday", "11:00am - 7:00 pm"))


db.commit()
