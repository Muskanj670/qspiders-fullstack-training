import sqlite3
conn = sqlite3.connect("data.db")   # Helps to connect .py file to .db file
cursor = conn.cursor()  # Helps to point a specific location in the database

# execute() --> To write and execute the sql query.
# ! Creating a table in database
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   NAME TEXT NOT NULL,
   email TEXT NOT NULL UNIQUE,
   age INTEGER,
   subject TEXT
    )
""")

#! Insert into table

cursor.execute("""
    Insert into student (id, name, email, age, subject) values (?,?,?,?,?)
""", (101, 'Muskan', 'muskan@gmail.com', 23, 'Python'))

conn.commit()
conn.close()  # Helps to disconnect 