import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Patient_info(PATIENTname VARCHAR(50), PATIENTage int UNSIGNED, phoneNumber bigint UNSIGNED, patientID int UNSIGNED)")

mycursor.execute("CREATE TABLE Patient_Roominfo(PATIENTname VARCHAR(50), RoomNumber int UNSIGNED, Department VARCHAR(50))")

mycursor.execute("CREATE TABLE Nurse(NURSEname VARCHAR(50), NURSEphone bigint UNSIGNED, NURSEfield VARCHAR(50),  NURSEdaysPresent VARCHAR(50), NURSEtimePresent VARCHAR(50) )")

mycursor.execute("CREATE TABLE Patient_Medicines(PATIENTname VARCHAR(50), MedicineName VARCHAR(20), MedicineDose VARCHAR (20))")

mycursor.execute("CREATE TABLE Patien_DAIGNOSTICS(PATIENTname VARCHAR(50), procedureRoomNumber int UNSIGNED, ProcedureRAN VARCHAR(50))")

mycursor.execute("CREATE TABLE Patien_ExaminationResult(PATIENTname VARCHAR(50),  medicalissues VARCHAR(50), DepartmentAssigned VARCHAR(50))")

mycursor.execute("CREATE TABLE Ambulance(DriverName VARCHAR(50), AmbulanceNumber int UNSIGNED, AmbulanceDaysAvalible VARCHAR(60), AmbulanceTimeAvaliable VARCHAR(60))")

mycursor.execute("CREATE TABLE cleaningStaff(StaffName VARCHAR(50), StaffDaysAvaliable VARCHAR(70), StaffTimeAvaliable VARCHAR(20), StaffCleaningArea VARCHAR(30))")

mycursor.execute("CREATE TABLE BillingInfo(PATIENTname VARCHAR(50), MoneyOwed int UNSIGNED, MoneyDueBy VARCHAR(50))")

mycursor.execute("CREATE TABLE Docter(DOCname VARCHAR(50), DOCphone bigint UNSIGNED, DOCfield VARCHAR(50),  DOCdaysPresent VARCHAR(50), DOCtimePresent VARCHAR(50) )")

