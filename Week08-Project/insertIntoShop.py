import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)

cursor = db.cursor()
sql="insert into shop (Product, Barcode, Price) values (%s,%s,%s)"
values = ("Vegetable Soup","1034555215643",2.10)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)