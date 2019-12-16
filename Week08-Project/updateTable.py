import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)

cursor = db.cursor()
sql="update student set Product= %s, Barcode=%s, Price=%s  where id = %s"
values = ("Eggs","1034550600026",3.60)

cursor.execute(sql, values)

db.commit()
print("update done")