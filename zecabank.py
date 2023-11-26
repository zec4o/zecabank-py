
# MAX_WITHDRAWS = 3
# WITHDRAW_LIMIT = 500.00
# balance = 0.00
# statement = ""
# withdraw_counter = 0

# while True:
#     option = input(MENU)
#     if option == "d":
#         value = float(input("Enter the desired deposit amount: "))

#         if value > 0:
#             balance += value
#             statement += f"Deposit: +${value:.2f}\n"
#         else:
#             print("Operation failed. The deposit amount is invalid.")

#     elif option == "w":
#         while withdraw_counter < 3:
#             value = float(input("Enter the desired withdraw amount: "))
#             if value > WITHDRAW_LIMIT:
#                 print(f"You can't withdraw more than ${WITHDRAW_LIMIT:.2f} at once")
#             elif value > balance:
#                 print(f"You can't withdraw more than your balance. Your balance is ${balance:.2f}")
#             elif value <= 0:
#                 print("Invalid value. try again.")
#             elif balance == 0:
#                 print(f"Your balance is: ${balance:.2f}")
#             else:
#                 balance -= value
#                 statement += f"Withdraw: -${value:.2f}\n"
#                 print(f"Success withdraw! Now your balance is ${balance:.2f}")
#                 withdraw_counter += 1
#                 break
#         else:
#             print(f"You have exceeded the limit of {MAX_WITHDRAWS} withdrawals per day.")
#     elif option == "s":
#         if statement == "":
#             print("There's no transactions in your account.")
#         else:
#             print("================STATEMENT================")
#             print(statement + f"\nBalance: ${balance:.2f}")
#             print("=========================================")
#     elif option == "q":
#         break
#     else:
#         print("Invalid operation. Check if the option selected exists.")

import textwrap

def menu():
    MENU = '''
    -----------------MENU-----------------
    [d] Deposit
    [w] Withdraw
    [s] Statement
    [nu] New user
    [na] New account
    [la] List accounts
    [q] Exit
    --------------------------------------

    => '''
    return input(textwrap.dedent(MENU))

def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        statement += f"Deposit: +${value:.2f}\n"
        print(f"Success deposit! Now your balance is ${balance:.2f}")
    else:
        print("Operation failed. The deposit amount is invalid.")
    return balance, statement

def withdraw(*, balance, value, statement, WITHDRAW_LIMIT, withdraw_counter, MAX_WITHDRAWS):
    exceed_WITHDRAW_LIMIT = value > WITHDRAW_LIMIT
    exceed_balance = value > balance
    exceed_MAX_WITHDRAWS = withdraw_counter >= MAX_WITHDRAWS

    if exceed_WITHDRAW_LIMIT:
        print(f"You can't withdraw more than ${WITHDRAW_LIMIT:.2f} at once")
    elif exceed_balance:
        print(f"You can't withdraw more than your balance. Your balance is ${balance:.2f}")
    elif exceed_MAX_WITHDRAWS:
        print(f"You have exceeded the limit of {MAX_WITHDRAWS} withdrawals per day.")
    elif value > 0:
        balance -= value
        statement += f"Withdraw: -${value:.2f}\n"
        print(f"Success withdraw! Now your balance is ${balance:.2f}")
        print("withdraw counter:", withdraw_counter)
        withdraw_counter += 1
    else:
        print("Invalid value. try again.")
    return balance, statement, withdraw_counter

def show_statement(balance, /, *, statement):
    if statement == "":
        print("There's no transactions in your account.")
    else:
        print("================STATEMENT================")
        print(statement + f"\nBalance: ${balance:.2f}")
        print("=========================================")

def create_user(users):
    cpf = input("Enter the new user's CPF (Only numbers): ")
    user = filter_user(cpf, users)

    if user:
        print("User already exists.")
        return
    name = input("Enter the new user's name: ")
    birth_date = input("Enter the new user's birth date (dd-mm-yyyy): ")
    address = input("Enter the new user's address (street, number - neighborhood - city/state): ")

    users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": address})

    print("User created successfully.")

def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

def create_account(AGENCY, account_number, users):
    cpf = input("Enter the user's CPF (Only numbers): ")
    user = filter_user(cpf, users)

    if user:
        print("Account created successfully.")
        return {"agency": AGENCY, "account_number": account_number, "user": user}
    
    print("User not found.")

def list_accounts(accounts):
    for account in accounts:
        line = f"""\
        -----------------ACCOUNT-----------------
        Agency: {account["agency"]}
        Account number: {account["account_number"]}
        User: {account["user"]["name"]}
        -----------------------------------------
        """
        print(textwrap.dedent(line))


def main():
    MAX_WITHDRAWS = 3
    WITHDRAW_LIMIT = 500.00
    AGENCY = "0001"

    balance = 0.00
    statement = ""
    withdraw_counter = 0
    users = []
    accounts = []

    while True:
        option = menu()
        if option == "d":
            value = float(input("Enter the desired deposit amount: "))
            balance, statement = deposit(balance, value, statement)
        elif option == "w":
            value = float(input("Enter the desired withdraw amount: "))
            balance, statement, withdraw_counter = withdraw(balance=balance, value=value, statement=statement, WITHDRAW_LIMIT=WITHDRAW_LIMIT, withdraw_counter=withdraw_counter, MAX_WITHDRAWS=MAX_WITHDRAWS)
        elif option == "s":
            show_statement(balance, statement=statement)
        elif option == "nu":
            create_user(users)
        elif option == "na":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)
        elif option == "la":
            list_accounts(accounts)
        elif option == "q":
            break
        else:
            print("Invalid operation. Check if the option selected exists.")

main()