import sqlite3

# A4
connect = sqlite3.connect("users.db")

# Hand and Pen
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXIST users (
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,,
        hobby TEXT
    )
""")
connect.commit()

# CRUD Create Read Update Delete

def create_user(name, age, hobby):
    # cursor.execute(f"INSERT INTO Users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}") ")
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?, ?, ?,)",
        (name, age, hobby)
    )
    connect.commit()
    print("User created successfully")

create_user('Ardager', 23, 'Sleep')

def read_user():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchone()

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    print(users)

read_user()

def update_user(new_name, rowid):
    # cursor.execute(f'UPDATE users SET name = "{new_name}" WHERE rowid = {rowid}')
    cursor.execute(
        f'UPDATE users SET name=? WHERE rowid=?',
        (new_name, rowid)
    )
    connect.commit()
    print("User updated successfully")

update_user("John", 3)

read_user()

def delete_user(rowid):
    cursor.execute(
            "DELETE FROM users WHERE rowid= '{rowid}'",
    )
    connect.commit()
    print("User deleted successfully")

delete_user(2)
