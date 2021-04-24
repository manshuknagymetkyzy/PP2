import psycopg2

#(Connecting to the PostgreSQL database server)
conn = psycopg2.connect(
    host = "localhost",
    database = "pp2",
    user = "postgres",
    password = "manshuk2003"
)

cur = conn.cursor()
#(Creating new PostgreSQL tables in Python)
cur.execute("CREATE TABLE students (id SERIAL PRIMARY KEY, name VARCHAR);")

#(Inserting data into the PostgreSQL table in Python)
names = ["Aiaru", "Aldiyar", "Aliya", "Zangar", "Daniyar", "Eldana"]
for name in names:
   cur.execute("INSERT INTO students (name) VALUES(%s)", (name, ))

cur.execute("SELECT * FROM students")
print(cur.fetchall())

#(Updating data in the PostgreSQL table in Python)
cur.execute("UPDATE students SET name = 'Aigerim' WHERE id = 1;")
cur.execute("SELECT * FROM students")
print(cur.fetchall())

#(Querying data from the PostgreSQL tables)
cur.execute("SELECT * FROM students ORDER BY name DESC;")
print(cur.fetchall())

cur.execute("SELECT * FROM students WHERE name LIKE 'Al%'")
print(cur.fetchall())

# (Deleting data from PostgreSQL tables in Python)
cur.execute("DELETE FROM students WHERE id > 5")
cur.execute("SELECT * FROM students")
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()