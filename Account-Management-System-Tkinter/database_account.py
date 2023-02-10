import sqlite3
def create():
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tableAccount(id INTEGER PRIMARY KEY,firstname TEXT, lastname TEXT, username TEXT, password TEXT,position TEXT, date TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount")
    rows = cur.fetchall()
    con.close()
    return rows

def search(firstname="", lastname="", username="", password="", position=""):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount WHERE firstname=? or lastname=? OR username=? OR password=? OR position=?", (firstname, lastname, username, password, position))
    rows = cur.fetchall()
    con.close()
    return rows
def add(firstname,lastname, username, password, position, date):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tableAccount VALUES(NULL,?,?,?,?,?,?)", (firstname, lastname, username, password, position, date))
    con.commit()
    con.close()
def update(id, firstname, lastname, username, password, position, date):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("UPDATE tableAccount SET firstname=?,lastname=?, username=?,password=?,position=?,date=? WHERE id=?", (firstname, lastname, username, password, position, date, id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tableAccount WHERE id=?",(id,))
    con.commit()
    con.close()
create()

