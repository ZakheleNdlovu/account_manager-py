from time import sleep

import mysql.connector

def mysql_connect():
    connect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='superunlock',
        database='accounts'
    )
    return connect

def signUp():
    name = input("Name: ")
    surname = input("Surname: ")
    password = input("Password: ")
    balance =int(input("Deposit: "))

    connect = mysql_connect()
    cursor = connect.cursor()
    try:
        query2 = f'insert into new_accounts(name,surname,password,balance)  values(%s,%s,%s,%s)'
        values = (name, surname, password, balance)
        cursor.execute(query2, values)
        connect.commit()
        cursor.close()
        connect.close()
        print("\nRegistration successful :)\n")
    except:
        query = f'create table new_accounts(id serial primary key,name varchar(50),surname varchar(50),password varchar(50), balance int(9))'
        cursor.execute(query)
        query2 = f'insert into new_accounts(name,surname,password,balance)  values(%s,%s,%s,%s)'
        values = (name, surname, password, balance)
        cursor.execute(query2, values)
        connect.commit()
        cursor.close()
        connect.close()
        print("\nRegistration successful :)\n")


def signIn(name,password):
    connect = mysql_connect()
    cursor = connect.cursor()
    try:
        query = f'select * from new_accounts where name = "{name}"'
        cursor.execute(query)
        results = cursor.fetchone()
        db_name = results[1]
        db_pass = results[3]

        if name == db_name:
            if password == db_pass:
                sleep(2)
                print("\nlog in successful :)")
                sleep(2)
            else:
                print("Incorrect password\n")

    except:
        print("Account not in database")

def deposit(name):
    amount = int(input("Amount: "))
    while amount < 0:
        print("Invalid amount!")
        amount = int(input("Amount: "))
    connect = mysql_connect()
    cursor = connect.cursor()
    query = f'select balance from new_accounts where name = "{name}"'
    cursor.execute(query)
    result = cursor.fetchone()
    db_balance = result[0]
    new_balance = db_balance + amount
    query2 = f'update new_accounts set balance = "{new_balance}" where name = "{name}"'
    cursor.execute(query2)
    connect.commit()
    cursor.close()
    connect.close()
    print("\nYour deposit was successful :)\nYour new balance is : R",new_balance)

def withdrawal(name):
    amount = int(input("Amount: "))
    connect = mysql_connect()
    cursor = connect.cursor()
    query = f'select balance from new_accounts where name = "{name}"'
    cursor.execute(query)
    result = cursor.fetchone()
    db_balance = result[0]

    while amount > db_balance:
        print("Insufficient funds")
        amount = int(input("Amount: "))
    new_balance = db_balance - amount
    query2 = f'update new_accounts set balance = "{new_balance}" where name = "{name}"'
    cursor.execute(query2)
    connect.commit()
    cursor.close()
    connect.close()
    print("\nYour new balance is : R",new_balance)

def accountDetails(name):
    connect = mysql_connect()
    cursor = connect.cursor()
    query = f'select * from new_accounts where name = "{name}"'
    cursor.execute(query)
    results = cursor.fetchone()
    print("\nName        : ",results[1],"\nSurname   : ",results[2],"\nPassword  : ",results[3],"\nBalance     : R",results[4])

def checkBalance(name):
    connect = mysql_connect()
    cursor = connect.cursor()
    query = f'select balance from new_accounts where name = "{name}"'
    cursor.execute(query)
    results = cursor.fetchone()
    balance = results[0]
    sleep(1)
    print("\nYour balance is : R",balance)

def updatePassword(name,new_password):
    connect = mysql_connect()
    cursor = connect.cursor()
    query = f'update new_accounts set password = "{new_password}" where name = "{name}"'
    cursor.execute(query)
    connect.commit()
    cursor.close()
    connect.close()
    print("Password updated successfully :)")

def transact(name):
    tran = int(input("\nTRANSACT\n\n1. Check Balance\n2. Deposit\n3. Withdrawal\n4. Account Details\n5. Update Password\n6. Exit\n: "))
    match tran:
        case 1:
            checkBalance(name)
        case 2:
            deposit(name)
        case 3:
            withdrawal(name)
        case 4:
            accountDetails(name)
        case 5:
          while True:
              new_password = input("Enter your new password: ")
              c_password = input("confirm your password: ")
              if new_password == c_password:
                  updatePassword(name, new_password)
                  break
              else:
                  print("Passwords don't match")
        case 6:
            print("\nThank you for using our services :)")
            exit(0)


def welcomeScreen():
    print("Press (e) to exit")
    answer = input("Welcome to ABC bank\nDo you have an account?\nPress (y) for Yes  or (n) for No: ")
    while True:
        print("Press (e) to exit")
        if answer.lower() == 'y':
            name = input("Name: ")
            if name == 'e':
                print("\nThank you for using our services :)")
                exit(0)
            password = input("Password: ")
            if password == 'e':
                print("\nThank you for using our services :)")
                exit(0)
            signIn(name, password)
            while True:
                transact(name)
                sleep(2)
        elif answer.lower() == 'n':

                signUp()
                print("Press (e) to exit")
                print('Log in')
                name = input("Name: ")
                if name.lower() == 'e':
                    print("\nThank you for using our services :)")
                    exit(0)
                password = input("Password: ")
                if password.lower() == 'e':
                    print("\nThank you for using our services :)")
                    exit(0)
                signIn(name,password)
                while True:
                    transact(name)

        elif answer.lower() == 'e':
            print("\nThank you for using our services :)")
            exit(0)
        else:
            print("Invalid input :(")

welcomeScreen()
