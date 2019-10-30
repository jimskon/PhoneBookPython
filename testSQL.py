import mysql.connector

HOST = "localhost"
USER = "skon"
DB = "skon"
PASS="PhilanderChase"
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASS,
    database=DB
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM PhoneBook")

myresult = mycursor.fetchall()

for x in myresult:
      print(x)
    
