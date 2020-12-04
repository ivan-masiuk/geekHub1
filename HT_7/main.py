import json
import os
import csv
import random

# restart function
def restart():
    # remove all .data files 
    del_file_list = [ f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".data") ]
    for f in del_file_list:
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
    # remove all .csv files     
    del_file_list = [ f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".csv") ]
    for f in del_file_list:
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
    # remove all .json files 
    del_file_list = [ f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".json") ]
    for f in del_file_list:
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))            
    # create users.csv
    users = {
        'Ivan': '1',
        'Misha': '2',
        'admin':'admin'
    }
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),'users.csv')
    with open(users_data, 'w', newline='') as write_file:
        writer = csv.writer(write_file, delimiter = ';')
        writer.writerow(['Name_user','Password_user'])
        for user in users:
            writer.writerow([f'{user}', f'{users[user]}'])
    # add banknotes.json
    banknotes_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banknotes.json')
    with open(banknotes_data, 'w') as write_file:
        banknotes = {'500':100, '200':100, '100':100, '50':100, '20':100}
        json.dump(banknotes, write_file)
    # create <name>_balance.data
    for user in users:
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_balance.data')
        with open(balance_data, 'w') as write_file:
            start_balance = 1000
            json.dump(start_balance, write_file)
    # create <name>_transactions.csv
    for user in users:
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_transactions.csv')
        with open(transactions_data, 'w', newline='') as write_file:
            writer = csv.writer(write_file, delimiter = ';')
            writer.writerow(['Transaction','Amount'])            

# add new user function
def addUser():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),'users.csv')
    with open(users_data, 'r') as read_file:
        reader = csv.DictReader(read_file, delimiter = ';')
        users = {}
        for row in reader:
            users[row['Name_user']] = row['Password_user']
    amount = int(input('Print amount of new users please: '))
    new_users = {} #dict of new users (that will be added)
    for _ in range(amount):
        new_users_name = input(f'Print new user*s name #{_ + 1}: ')
        new_users_password = input(f'Print new user*s password #{_ + 1}: ')
        users[new_users_name] = new_users_password
        new_users [new_users_name] = new_users_password
    with open(users_data, 'w', newline='') as write_file:
        writer = csv.writer(write_file, delimiter = ';')
        writer.writerow(['Name_user','Password_user'])
        for user in users:
            writer.writerow([f'{user}', f'{users[user]}'])
    # pretty print
    print('You added: ', end='')
    for user in new_users:
        print(f'{user}, ', end='')
    print('\n')
    # create NEW <name>_balance.data
    for user in new_users:
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_balance.data')
        with open(balance_data, 'w') as write_file:
            start_balance = 1000
            json.dump(start_balance, write_file)
    # create NEW <name>_transactions.data
    for user in new_users:
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_transactions.csv')
        with open(transactions_data, 'w', newline='') as write_file:
            writer = csv.writer(write_file, delimiter = ';')
            writer.writerow(['Transaction','Amount'])


# autoriation user in system
def autoriationUser():
    status_user = False
    user_name = input('Print your name: ')
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.csv')
    with open(users_data, 'r') as users_data:
        reader = csv.DictReader(users_data, delimiter = ';')
        users_dict = {}
        for row in reader:
            users_dict[row['Name_user']] = row['Password_user']      
    if user_name in users_dict:
        user_password = str(input ('Print your password: '))
        counter = 2
        for _ in range(3):
            if users_dict[user_name] == user_password:
                print(f'\n{user_name}, welcome!')
                status_user = True
                break
            else:
                print(f'Incorrect password! Try again, you have {counter} attempt more')
                counter -= 1             
                user_password = str(input ('Print your password again: '))                 
    else:
        print(f'Any users with {user_name} name.')
    return(status_user, user_name)

# get money function
def getMoney(user_name):
    desire = int(input('Print amount of money: '))
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open(balance_data, 'r') as read_file:
        users_balace = json.load(read_file)
    if desire <= users_balace:
        new_users_balace = users_balace - desire
        desire1 = desire
        # banknotes print
        counter500 = desire//500
        desire -= 500 * counter500
        counter200 = desire//200
        desire -= 200 * counter200
        counter100 = desire//100
        desire -= 100 * counter100
        if (desire - 50) % 20 == 0:
            counter50 = desire//50
            desire -= 50
            counter20 = desire // 20
        else:
            counter50 = 0
            counter20 = desire // 20
        # balance.data update
        with open(balance_data, 'w') as write_file:
            json.dump(new_users_balace, write_file)
        # transaction.data update
        transaction_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_transactions.csv')
        with open(transaction_data, 'a', newline='') as write_file:
            writer = csv.writer(write_file, delimiter = ';')
            writer.writerow(['GOT maney',f'{desire1}'])
        print(f'Get money: {desire1} UAH!\nBanknotes: 500 UAH x {counter500}, 200 UAH x {counter200}, 100 UAH x {counter100}, 50 UAH x {counter50}, 20 UAH x {counter20}')
    else:
        print('Not enought money!')


# top up balance function
def topUpBalance(user_name):
    desire = int(input('Print amount of money: '))
    # get start balance
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open(balance_data, 'r') as read_file:
        users_balace = json.load(read_file)
    users_balace += desire
    # update balance
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open(balance_data, 'w') as write_file:
        json.dump(users_balace, write_file)
    # add transaction
    transaction_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_transactions.csv')
    with open(transaction_data, 'a', newline='') as write_file:
        writer = csv.writer(write_file, delimiter = ';')
        writer.writerow(['TOP UP balance',f'{desire}'])
    print(f'You have replenished the balance by {desire} UAH\n')

# check balance function
def checkBalance(user_name):
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open (balance_data, 'r') as read_file:
        balance = json.load(read_file)
    print('Your balance: ', balance, 'UAH')

# top up banknotes function
def topUpBanknotes():
    banknotes_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banknotes.json')
    with open(banknotes_data, 'r') as read_file:
        banknotes = json.load(read_file)
    for banknote in banknotes:
        count = int(input(f'How much {banknote} banknotes would you add? '))
        banknotes[banknote] = banknotes[banknote] + count
    with open(banknotes_data, 'w') as write_file:
        json.dump(banknotes, write_file)
    print('Success!')

# check banknotes balance function
def checkBanknotesBalance():
    banknotes_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banknotes.json')
    with open(banknotes_data, 'r') as read_file:
        banknotes = json.load(read_file)
    money = 0
    print('')
    for banknote in banknotes:
        print(f'{banknote} UAH x', banknotes[banknote])
        money += int(banknote) * banknotes[banknote]
    print('Money in cashbox: ', money, ' UAH')

# Сheck for required files
def checkRequiredFilse():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.csv')
    status = os.path.isfile(users_data)
    if status == False:
        restart()
    return(status)

# random bonus for users function
def randomBonus(user_name):
    if random.randint(1,10) == 1:
        # get start balance
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
        with open(balance_data, 'r') as read_file:
            users_balace = json.load(read_file)
        users_balace += 100
        # update balance
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
        with open(balance_data, 'w') as write_file:
            json.dump(users_balace, write_file)
        # add transaction
        transaction_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_transactions.csv')
        with open(transaction_data, 'a', newline='') as write_file:
            writer = csv.writer(write_file, delimiter = ';')
            writer.writerow(['BONUS',f'{100}'])
        print('Good news! You win 100 UAH!')


# start function
def start():
    checkRequiredFilse()
    user_status, user_name = autoriationUser()
    if user_name == 'admin' and user_status:
        # main menu for ADMINS
        while True:
            desire = int(input('\nAdmin menu:\nPrint 0 for EXIT\nPrint 1 for TOP UP BANKNOTES\nPrint 2 for RESTART DATAS\nPrint 3 for ADD NEW USER(S)\nPrint 4 for CHECK BANKNOTES BALANCE\nPrint 5 for CHANGING USER\n'))
            if desire == 1:
                topUpBanknotes()
            elif desire == 0:
                break
            elif desire == 2:
                restart()
            elif desire == 3:
                addUser()
            elif desire == 4:
                checkBanknotesBalance()
            elif desire == 5:
                user_status = False
                os.system(f'python "{__file__}"')
                break
            else:
                print('Try again')
                break
    else:
        if user_status:
            # random bonus for USERS
            randomBonus(user_name)
            # main menu for USERS
            while True:
                desire = int(input('\nMenu:\nPrint 0 for EXIT\nPrint 1 for CHECK BALANCE\nPrint 2 for GET CASH\nPrint 3 for TOP UP BALANCE\nPrint 4 for CHANGING USER\n'))
                if desire == 1:
                    checkBalance(user_name)
                elif desire == 2:
                    getMoney(user_name)
                elif desire == 3:
                    topUpBalance(user_name)
                elif desire == 4:
                    user_status = False
                    os.system(f'python "{__file__}"')
                    break
                elif desire == 0:
                    break
                else:
                    print('Try again')
                    break

start()