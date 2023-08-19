import mysql.connector
from faker import Faker;

fake = Faker();

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sample_data"
)

mycursor = mydb.cursor()

tablename = "users";
sql = "INSERT INTO " + tablename + "  (fullname, email, address, created_at) VALUES (%s, %s,%s, %s)"

count = 0
while count < 900:
    timestamp = fake.date_time_between(start_date='-1y', end_date='now')
    val = (fake.name(), fake.email(), fake.address(), timestamp)
    mycursor.execute(sql, val)
    count += 1
    
    
sql2 = "UPDATE " + tablename + " SET username = REPLACE(LOWER(fullname), ' ', '_') ";
mycursor.execute(sql2)

mydb.commit()

print("record inserted.")

