import sqlite3

connect = sqlite3.connect("user_grades.db")

cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR (50) NOT NULL
        user id INTEGER,
        FOREIGN KEY (user) REFERENCES users(id)
    )
""")
connect.commit()


def create_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(grade, subject, user_id) VALUES (?, ?, ?)',
        (grade, subject, user_id)
    )
    connect.commit()
    print("grade added!!")

create_grade(1, 'Math', 4)
create_grade(2, 'Science', 3)
create_grade(2, 'Physics', 5)

def read_users_and_grades():
    cursor.execute(""""
    SELECT 
    """)