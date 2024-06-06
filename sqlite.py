import sqlite3
con = sqlite3.connect("users.db")
def channels():
    users = []
    for row in con.execute("SELECT username FROM users "):
        users.append(row[0])
    return users

def add_channel(user, id):
    cur = con.execute(f"SELECT username FROM users WHERE username = '{user}'")
    a = cur.fetchone()
    if a:
        return 0
    else:
        con.execute(f"INSERT INTO users(username, userid) VALUES ('{user}', '{id}')")
        con.commit()
        return 1

def name_from_user(user):
    try:
        cur = con.execute(f"SELECT username FROM users WHERE username LIKE '{user}%'")
        return cur.fetchone()[0]
    except TypeError:
        return 0

def get_user():
    cur = con.execute(f"SELECT username FROM users")
    a = cur.fetchall()
    return a

def add_group(argument, user):
    con.execute(f"UPDATE users SET groups = '{argument}' WHERE username = '{user}'")
    con.commit()

def get_group_user(argument):
    cur = con.execute(f"SELECT username FROM users WHERE groups LIKE '{argument}%'")
    a = cur.fetchall()
    return a

def get_group(user):
    cur = con.execute(f"SELECT groups FROM users WHERE username = '{user}'")
    a = cur.fetchone
    return a

def userids():
    cur = con.execute(f"SELECT userid FROM users")
    a = cur.fetchall()
    return a