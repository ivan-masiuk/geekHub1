### SIMPLE BANK MODEL ###


import sqlite3
import os


def restart():
    # remove all .db files 
    del_file_list = [ f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".db") ]
    for f in del_file_list:
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))

    # create users TABLE in database
    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mydata.db'))
    c = conn.cursor()
    c.execute('''CREATE TABLE users (
        id_ INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT,
        balance INTEGER)
    ''')

    # add default_users in database
    default_users = [('Ivan','abc',1000),('Misha','abc', 1000)]
    c.executemany('INSERT INTO users (name, password, balance) VALUES (?,?,?)', default_users)
    conn.commit()
    conn.close()

def startBank():
    input_name = input('Print your name: ')
    input_password = input('Print your password: ')
    input_data =(input_name, input_password)

    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mydata.db'))
    c = conn.cursor()

    try:
        c.execute('SELECT password FROM users WHERE (name =? AND password =?)', input_data)
        total_message = 'Welcome!'
        print(total_message) 
    except:
        total_message = 'Sorry, password is incorrect!'
        print(total_message) 

    conn.close()
    return(input_name)

def getMoney(name_user):
    desire = int(input('Print amount of money you want to get: '))
    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),'mydata.db'))
    c = conn.cursor()
    name = (name_user,)
    c.execute('SELECT balance FROM users WHERE name =?', name)
    start_balance = c.fetchone()[0]  

    if not(start_balance - desire < 0):
        new_balance = start_balance - desire
        print(f'----------------\nYou got {desire} UAH\nYour new balance: {new_balance} UAH \n----------------')
        
        users_data =(new_balance ,name_user) 
        c.execute('UPDATE users SET balance =? WHERE name =?', users_data)
        conn.commit()
    else:
        print('Not enough money!')
    
    conn.close()


# restart()
name_user= startBank()
getMoney(name_user)