import psycopg2
import mysql.connector

# testing mysql
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="mydatabase",
    user="root",
    password="mypassword",
)

cur = conn.cursor()
cur.close()
conn.close()
print("mysql OK")


# testing postgresql
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mydatabase",
    user="myuser",
    password="mypassword",
)

cur = conn.cursor()
cur.close()
conn.close()

print("postgres OK")
