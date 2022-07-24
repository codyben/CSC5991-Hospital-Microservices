import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database=" HospitalServices2"
) 

mycursor = db.cursor()

mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Nick Advardo", 35, "8/1/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Tim Leoroy", 35, "8/1/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Colina Westwood", 40, "8/1/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Samuel Johsnson", 1804, " 1/23/23"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Mathew Quinton", 1515, " 10/18/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Erham Bienga", 1706, " 12/17/23"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Maxine Conti", 1107, "8/23/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("alexandra Anquilla", 1208,"8/26/22"  ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Adriana Tevez", 1290, "8/29/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Karen Mcvault", 1310, "9/13/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Anthony Selvestor", 1721, "12/13/22" ))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Anushka Kumail", 1522, "9/30/22"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Juan Vaccino", 1920, "2/29/23"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Megan Advardo", 1478, "10/17/22"))
mycursor.execute("INSERT INTO  BillingInfo (PATIENTname, MoneyOwed, MoneyDueBy) VALUES (%s,%s,%s)", ("Olivia Tamina", 1560, "10/32/22"))

db.commit()

