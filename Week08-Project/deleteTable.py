import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="project"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS shop"

mycursor.execute(sql)