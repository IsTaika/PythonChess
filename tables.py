import sqlite3


# registration:

def registration_table_create():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE PROFILE
                        (ID       INT PRIMARY KEY   NOT NULL,
                        NAME    TEXT          NOT NULL,
                        COUNTRY TEXT         NOT NULL,
                        WINS    INT                      ,
                        LOSES   INT                   ,
                        GAMES   INT                    ,
                        PERCENT FLOAT                  );''')
    cursor.close()

def get_games_profile():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    games = ""
    for row in cursor.execute("SELECT games from PROFILE"):
        games = row
    return games


def get_country_profile():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    country = ""
    for row in cursor.execute("SELECT country from PROFILE"):
        country = row
    return country

def get_wins_profile():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    wins = ""
    for row in cursor.execute("SELECT wins from PROFILE"):
        wins = row
    return wins

def get_loses_profile():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    loses = ""
    for row in cursor.execute("SELECT loses from PROFILE"):
        loses = row
    return loses

def get_precent_profile():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    precent = False
    for row in cursor.execute("SELECT percent from PROFILE"):
        if row is not None:
            precent = row
    return precent


def games_table_create():
    conn = sqlite3.connect('games.sqlite')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE GAMES
                        (ID       INT PRIMARY KEY   NOT NULL,
                        SECOND TEXT                         ,
                        RESULT TEXT                        ,
                        AMOUNT INT                          ,
                        INFO   TEXT);''')
    cursor.close()


def table_test():
    result = True
    try:
        f = open('table.txt')
        print(result)
    except FileNotFoundError:
        result = False
        print("Table not found!")
        registration_table_create()
        games_table_create()
        f = open('table.txt', 'w+')
        f.write(str(0))
        f.close()
        print(result)
    print(result)
    return result


def last_id():
    f = open('table.txt', 'r+')
    q = f.readline()
    f.close()
    f = open('table.txt', 'w+')
    new_id = int(q) + 1
    f.write(str(new_id))
    f.close()
    return int(q)


def registration_table_append(name, country):
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    _id = last_id()
    name_1 = "'" + name + "'"
    country_1 = "'" + country + "'"
    append = "INSERT INTO PROFILE (ID, NAME, COUNTRY) VALUES (" + str(_id) + ", " + name_1 + ", " + country_1 + ")"
    cursor.execute(append)
    conn.commit()
    print("Учётная запись успешно создана! ")
    conn.close()


def profile_table_change():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    conn2 = sqlite3.connect('games.sqlite')
    cursor2 = conn2.cursor()
    win = 0
    lose = 0
    games = 0
    for row in cursor2.execute("SELECT id, result from GAMES"):
        if row[1] == 'win':
            games += 1
            win += 1
        else:
            games += 1
            lose += 1
    procent = 0.0
    if win != 0 and lose != 0:
        procent = (win / games)*100
    conn.execute("UPDATE PROFILE set GAMES = " + str(games) + " where ID = " + "0")
    conn.commit()
    conn.execute("UPDATE PROFILE set WINS = " + str(win) + " where ID = " + "0")
    conn.commit()
    conn.execute("UPDATE PROFILE set LOSES = " + str(lose) + " where ID = " + "0")
    conn.commit()
    if procent != 0.0:
        conn.execute("UPDATE PROFILE set PERCENT = " + str(procent) + " where ID = " + str(0))
        conn.commit()
    conn.close()
    conn2.commit()
    conn2.close()


def games_table_append(second, result, amount, info):
    conn = sqlite3.connect('games.sqlite')
    cursor = conn.cursor()
    _id = last_id()
    second_1 = "'" + second + "'"
    result_1 = "'" + result + "'"
    info_1 = "'" + info + "'"
    append = "INSERT INTO GAMES (ID, SECOND, RESULT, AMOUNT, INFO) VALUES (" + str(
        _id) + ", " + second_1 + ", " + result_1 + ", " + str(amount) + ", " + info_1 + ")"
    cursor.execute(append)
    conn.commit()
    print("game add to table ")
    conn.close()


def get_name():
    conn = sqlite3.connect('profile.sqlite')
    cursor = conn.cursor()
    name = ""
    for row in cursor.execute("SELECT name from PROFILE"):
        name = row
    return name
