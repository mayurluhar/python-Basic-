import sqlite3

db="todo.db"
table_name="todo"
conn=sqlite3.connect(db)
c= conn.cursor()

def createTable():
    sql = 'CREATE TABLE ' + table_name + \
          '(ID INTEGER PRIMARY KEY AUTOINCREMENT, TaskName text)'
    c.execute(sql)

def data_entry(task):
    c.execute("INSERT INTO " + table_name + " (TaskName) VALUES (?)", [task])
    print("data added")
    conn.commit()

def data_print():
    sql = "SELECT * FROM " + table_name
    c.execute(sql)
    for row in c.fetchall():
        print(row[0] ,"-->", row[1])

def delete_data(id):
    c.execute("DELETE FROM "+ table_name + " WHERE ID=? ", (id, ))
    print("Data Deleted")

def close():
    c.close()
    conn.close()
