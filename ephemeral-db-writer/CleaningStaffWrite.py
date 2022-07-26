import mysql.connector
from constants import MYSQL_CONNECT_OPTIONS

db = mysql.connector.connect(**MYSQL_CONNECT_OPTIONS)
mycursor = db.cursor()


mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Stanley Jackson", "Monday-Friday", "8am - 4pm", "Lounge/Hallway"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Miarana Tijax", "Monday-Friday", "8am - 4pm", "Rooms 101-108, DiningArea"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Jaquerius Tarshid", "Monday-Friday", "8am - 4pm", "Rooms 109-115, Bathrooms"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Tristan Foxworth", "Monday-Friday", "4pm - 12pm","Lounge/Hallway"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Janen anjickat", "Monday-Friday", "4pm - 2pm","Rooms 101-108, DiningArea"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Jose Sexton", "Monday-Friday", "4pm - 2pm","Rooms 109-115, Bathrooms"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Kareem Sidorty", "Tuesday-Sunday", "6am - 2pm","Lounge/Hallway"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Timothy Mcdougald", "Tuesday-Sunday", "8am - 4pm","Rooms 101-108, DiningArea"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("lisandra Malinski", "Tuesday-Sunday", "8am - 4pm","Rooms 109-115, Bathrooms"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Ricky Travis", "Tuesday-Sunday", "4pm - 12pm","Lounge/Hallway"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Richardo Lexenton",  "Tuesday-Sunday", "4pm - 10pm","Rooms 101-108, DiningArea"))
mycursor.execute("INSERT INTO cleaningStaff(StaffName, StaffDaysAvaliable, StaffTimeAvaliable, StaffCleaningArea) VALUES (%s,%s,%s, %s)", ("Hope devinco", "Tuesday-Sunday", "12am - 10pm","Rooms 109-115, Bathrooms"))


db.commit()