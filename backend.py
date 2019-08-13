import sqlite3


def connect():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY,name TEXT,leaveBalance INTEGER)")
    conn.commit()
    conn.close()


def search(name="", leaveBalance=""):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee WHERE name=? OR leaveBalance=?", (name, leaveBalance))
    rows = cur.fetchall()
    conn.close()
    return rows


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * From employee")
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(name, leaveBalance):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT into employee VALUES (NULL,?,?)", (name, leaveBalance))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM employee WHERE id =?", (id,))
    conn.commit()
    conn.close()


def update(id, name, leaveBalance):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE employee SET name=?,leaveBalance=? WHERE id=?", (name, leaveBalance, id))
    conn.commit()
    conn.close()


connect()
# insert("vigneshwar", 10)
# insert("lokesh", 7)
# insert("sabari", 5)
# insert("yuvith", 2)
# insert("shyam", 1)
# insert("kathir", -2)
# insert("girija radhakrishnan", 8.5)
# insert("raghunath", 4)
# insert("kousik", 2)
# update(1, "vigneshwar", 10.5)
# print(view())
# print(search(name ="kathir"))
# delete(1)