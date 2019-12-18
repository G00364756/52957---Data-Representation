import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)

cursor = db.cursor()
sql="CREATE TABLE shop (id INT AUTO_INCREMENT PRIMARY KEY, Product VARCHAR(255), Barcode VARCHAR(255), Price INT)"

cursor.execute(sql)