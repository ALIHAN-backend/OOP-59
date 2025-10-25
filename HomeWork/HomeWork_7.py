import sqlite3

# A4
connect = sqlite3.connect("users.db")

# Рука и Ручка
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
connect.commit()


# CRUD Create Read Update Delete

def create_user(name, age, hobby):
    #cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()
    print("user added!!")

create_user('Stas', 23, "Спать")

def update_user(rowid, name=None, age=None, hobby=None):
    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if hobby is not None:
        fields.append("hobby = ?")
        values.append(hobby)

    # Если нечего обновлять
    if not fields:
        print("Нет данных для обновления!")
        return

    values.append(rowid)
    sql_query = f"UPDATE users SET {', '.join(fields)} WHERE rowid = ?"

    cursor.execute(sql_query, values)
    connect.commit()
    print("Пользователь обновлен!")


def read_user_by_id(rowid):
    cursor.execute('SELECT rowid, * FROM users WHERE rowid = ?',
                   (rowid,))
    user = cursor.fetchone()

    if user:
        print(f"ID: {user[0]} | NAME: {user[1]} | AGE: {user[2]} | HOBBY: {user[3]}")
    else:
        print("Пользователь не найден!")

update_user(rowid=3, name="Nikita")
update_user(rowid=4, age=25)
update_user(rowid=5, hobby="Играть в шахматы")
update_user(rowid=6, name="Alex", age=30, hobby="Плавать")

read_user_by_id(6)