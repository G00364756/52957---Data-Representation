import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)

cursor = db.cursor()
sql="insert into shop (Product, Barcode, Price) values (%s,%s,%s),(%s,%s,%s),(%s,%s,%s)"
values = ("Vegetable Soup","1034555215643",210,"Eggs","1037713191222",320,"Milk","1032336985993",150)

cursor.execute(sql, values)

db.commit()
print("3 records inserted")