import json
import os

# data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'NAME_FILE.data')
# os.path.abspath - файл, де працюю
# os.path.dirname - папка
# os.path.join - об'єднання


# create users.data, {name}_balance.data, {name}_transactions.data
def createUsersData():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.data')
    users = {
    'Ivan':'password1',
    'Ann':'password2',
    'Misha':'password3'
    }
    with open(users_data, "w") as write_file:
        json.dump(users, write_file)
    write_file.close()

    for _ in users:
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{_}_balance.data')
        balance = 0
        with open(balance_data,"w") as write_file:
            json.dump(balance, write_file)
            write_file.close()
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{_}_transactions.data')
        transactions = []
        with open(transactions_data,"w") as write_file:
            json.dump(transactions, write_file)
            write_file.close()

   
# authorization
# def authorization():
#     name = str(input('Print your name: '))
#     users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.data')
#     with open(users_data, 'r') as data_names:
#         json_users = json.load(data_names)
#         # print(type(json_users))
#         if name in json_users:
#             password = str(input('Print your password: '))
#             if json_users[name] == password:
#                 print(f'{name}, wellcome!') 
#         else:
#             print(f'Sorry! Any users with {name} name!')
#         data_names.close()


# main function
def start():
    # authorization()
    name = str(input('Print your name: '))
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.data')
    with open(users_data, 'r') as data_names:
        json_users = json.load(data_names)
        # print(type(json_users))
        if name in json_users:
            password = str(input('Print your password: '))
            if json_users[name] == password:
                print(f'{name}, wellcome!') 
        else:
            print(f'Sorry! Any users with {name} name!')
        data_names.close()

    desire = int(input('Print 1 for CHECK BALANCE\nPrint 2 for GET CASH\nPrint 3 for TOP UP BALANCE\n'))
    if desire == 1:
        checkBalance(name)
    elif desire == 2:
        getCash(name)
    elif desire == 3:
        topUpBalance(name)
    else:
        print('Try again')

# check balance
def checkBalance(name):
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_balance.data')
    with open(balance_data, 'r') as balance:
        json_balance = json.load(balance)
        print('Your balance: ', json_balance, '$')
    balance.close()

# get cash
def getCash(name):
    desire = int(input('Print amount of money: '))
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_balance.data')
    with open(balance_data, 'r') as balance:
        json_balance = json.load(balance)
        if desire > json_balance:
            print('Not anough money on your balance!')
        else:
            with open(balance_data, 'w') as balance:
                new_balance = json_balance - desire
                json.dump(new_balance, balance)
            balance.close() 
            transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_transactions.data')
            with open(transactions_data, 'a') as new_transaction:
                transaction = f'GET cash: {desire}'
                json.dump(transaction,new_transaction)
            new_transaction.close()
    balance.close()   


# top up balance
def topUpBalance(name):
    desire = int(input('Print amount of money for top up: '))
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_balance.data')
    with open(balance_data, 'r') as balance:
        json_balance = json.load(balance)
        with open(balance_data, 'w') as balance:
            new_balance = json_balance + desire
            json.dump(new_balance, balance)
        balance.close() 
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_transactions.data')
        with open(transactions_data, 'a') as new_transaction:
            transaction = f'TOP UP balance: {desire}'
            json.dump(transaction,new_transaction)
        new_transaction.close()
    balance.close()   

start()