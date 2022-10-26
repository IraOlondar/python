import json
import sqlite3
import os.path
import configuration as cf

path_to_db = cf.db_name

def init_base():
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()
    cursor.execute(f''' 
        SELECT count(name) 
        FROM sqlite_master 
        WHERE type='table' AND name='{cf.table_name}' ''') 
    if cursor.fetchone()[0] != 1 :
        cursor.execute(f'''CREATE TABLE {cf.table_name}(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name text, 
            second_name text, 
            department text, 
            salary real
        )''')
        conn.commit()
    conn.close()


def add_user(name, second_name, department, salary):
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()
    sqlite_insert_with_param = f'''INSERT INTO {cf.table_name}
        (id, name, second_name, department, salary)
        VALUES (NULL, ?, ?, ?, ?);'''

    data_tuple = (name, second_name, department, salary)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    conn.close() 
    return cursor.lastrowid


def update_user(id, arr):
    text = ""
    first = True 
    for key, val in arr.items():
        if len(val) > 0:
            text += ("" if first else ", ") + key + " = '" + val + "'"
            first = False
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()
    cursor.execute(f'''UPDATE {cf.table_name} SET {text} WHERE id = {id}''')
    conn.commit()
    conn.close() 
    return True


def delete_user(id):
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()
    cursor.execute(f'''DELETE FROM {cf.table_name} WHERE id = {id}''')
    conn.commit()
    conn.close()
    return True


def sqlite_lower(value_):
    return str(value_).lower()


def find_contact(name):
    if_found = False
    a = []
    conn = sqlite3.connect(path_to_db)
    conn.create_function("LOWER", 1, sqlite_lower)
    cursor = conn.cursor()
    for row in cursor.execute(f'''
        SELECT * 
        FROM {cf.table_name} 
        WHERE 
            LOWER(name) LIKE "%{name.lower()}%" 
            or LOWER(second_name) LIKE "%{name.lower()}%"
            or LOWER(department) LIKE "%{name.lower()}%"
            or LOWER(salary) LIKE "%{name.lower()}%"
        ORDER BY id'''):
        a.append(row)
        if_found = True

    if not if_found:
        return False
    conn.close()    
    return a


def view_all_user():
    if_found = False
    a = []
    conn = sqlite3.connect(path_to_db)
    conn.create_function("LOWER", 1, sqlite_lower)
    cursor = conn.cursor()
    for row in cursor.execute(f'''
        SELECT * 
        FROM {cf.table_name} 
        ORDER BY id'''):
        a.append(row)
        if_found = True

    if not if_found:
        return False
    conn.close()    
    return a
