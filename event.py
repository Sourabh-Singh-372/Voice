import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = #your password,
    database = #your database name
)

mycursor = db.cursor()

mycursor.execute("use events")
mycursor.execute("create table new(name char(20), profession varchar(50), age int(4))")
mycursor.execute("insert into new(name, profession, age) values ('Ravi', 'software engineer', 24), ('Akash', 'software engineer', 23), ('Bhanu', 'mechanical engineer', 22), ('Mukund', 'electrical engineer', 24)")
mycursor.execute("select name, email, mobile from new")
data = mycursor.fetchall()

for name, email, mobile in data:
    print(name, email, mobile)
