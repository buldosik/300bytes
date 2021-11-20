import sqlite3


def create_new_user(login, name, rate):
    user = sqlite3.connect('users.db')
    curs = user.cursor()

    for value in curs.execute("SELECT * FROM users"):
        if value[0] == login:
            user.close()
            return 0

    curs.execute("INSERT INTO users VALUES (?,?,?)", (login, name, rate))
    user.commit()
    user.close()

def del_user(login):
    user = sqlite3.connect('users.db')
    curs = user.cursor()

    curs.execute("DELETE from users WHERE login = ?", (login,))

    user.commit()
    user.close()
    return 0


def create_new_marker(x, y, name, date, time):
    mark = sqlite3.connect('markers.db')
    curs = mark.cursor()

    for value in curs.execute("SELECT * FROM markers"):
        if value == (x, y, name, date, time):
            mark.close()
            return 0

    curs.execute("INSERT INTO markers VALUES (?,?,?,?,?)", (x, y, name, date, time))
    mark.commit()
    mark.close()


def del_merker(name):
    mark = sqlite3.connect('markers.db')
    curs = mark.cursor()

    curs.execute("DELETE from markers WHERE name = ?", (name,))

    mark.commit()
    mark.close()
    return 0

def show_table_user():
    user = sqlite3.connect('users.db')
    curs = user.cursor()

    curs.execute("SELECT * FROM users")
    print(curs.fetchall())

    user.commit()
    user.close()
    return 0


def show_table_markers():
    mark = sqlite3.connect('markers.db')
    curs = mark.cursor()

    curs.execute("SELECT * FROM markers")
    print(curs.fetchall())

    mark.commit()
    mark.close()
    return 0

def show_table_markerss():
    mark = sqlite3.connect('markers.db')
    curs = mark.cursor()

    lst = list(curs.execute("SELECT * FROM markers"))

    mark.commit()
    mark.close()
    return lst

print(show_table_markerss())
