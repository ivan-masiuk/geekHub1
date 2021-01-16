import sqlite3
import os


def restart():
    # remove all .db files 
    del_file_list = [ f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".db") ]
    for f in del_file_list:
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))

    # create users TABLE in database and add default_users
    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mydata.db'))
    c = conn.cursor()
    c.execute('''CREATE TABLE users (
        name TEXT,
        password TEXT,
        balance INTEGER)
    ''')
    default_users = [('Ivan','abc',1000),('Misha','abc', 1000)]
    c.executemany('INSERT INTO users VALUES (?,?,?)', default_users)
    conn.commit()
    conn.close()


def updateBalance(desire):
    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mydata.db'))
    c = conn.cursor()    

# get balance
    input_name = (input('Print name: '),)
    c.execute("SELECT * FROM users WHERE name=?", input_name)
    new_balance = c.fetchone()[2] + desire

    print(c.fetchone()[2])

# rewrite balance
    new_users_data = ('Ivan','abc', f'{new_balance}')
    c.execute('INSERT INTO users VALUES (?,?,?)', new_users_data)
    conn.commit()

# check
    c.execute("SELECT * FROM users WHERE name=?", input_name)
    print(c.fetchone()[2])

    conn.close()

updateBalance(-100)



# restart()