import sqlite3

connect = sqlite3.connect('unior_new.db')
cursor = connect.cursor()

# Создание 1 таблицы в БД (USERS)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    chat_id INTEGER)
''')
connect.commit()

# Создание 2 таблицы в БД (USERS_ZAYVKA)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users_zayvka (
    id INTEGER PRIMARY KEY,
    Child_Name TEXT,
    Child_DateOfBirth TEXT,
    Child_Education TEXT,
    Child_Contacts TEXT,
    Mother_Name TEXT,
    Father_Name TEXT,
    Parents_Contacts TEXT)
''')
connect.commit()
cursor.close()
