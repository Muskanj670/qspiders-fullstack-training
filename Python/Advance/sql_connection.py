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
""", (102, 'Khushi', 'khushi@gmail.com', 18, 'Political'))


# ! Insert multiple rows

data = [
    ('Nancy', 'nancy@gmail.com',24,'Maths'),
    ('Ravi', 'ravi@gmail.com',16,'Business'),
    ('Rivaa', 'rivaa@gmail.com',21,'Accountancy')    
        ]

cursor.executemany("""
    insert into student (name,email,age,subject) values (?,?,?,?)
""", data)


# ! Read the data
cursor.execute("""
    select * from student
    """)

print(cursor.fetchone())

print(cursor.fetchmany(2))

# for row in many_row:
#     print(row)


print(cursor.fetchall())
# for row in rows:
#     print(row)

# ! Update data

cursor.execute("""
    update student set subject = ? where subject = ?
    """, ('Computer Science', 'Python')
    )

# ! Delete data

cursor.execute("""
    delete from student where id = ?
    """, (102,))
cursor.execute("""
    delete from student
""")

cursor.execute("""
    DROP TABLE STUDENT
""")
conn.commit()
conn.close()  # Helps to disconnect 
