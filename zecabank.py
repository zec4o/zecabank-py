MENU = '''
-----------------MENU-----------------
[d] Deposit
[w] Withdraw
[s] Statement
[q] Exit
--------------------------------------

=> '''
MAX_WITHDRAWS = 3
WITHDRAW_LIMIT = 500.00
balance = 0.00
statement = ""
withdraw_counter = 0

while True:
    option = input(MENU)
    if option == "d":
        value = float(input("Enter the desired deposit amount: "))

        if value > 0:
            balance += value
            statement += f"Deposit: +${value:.2f}\n"
        else:
            print("Operation failed. The deposit amount is invalid.")

    elif option == "w":
        while withdraw_counter < 3:
            value = float(input("Enter the desired withdraw amount: "))
            if value > WITHDRAW_LIMIT:
                print(f"You can't withdraw more than ${WITHDRAW_LIMIT:.2f} at once")
            elif value > balance:
                print(f"You can't withdraw more than your balance. Your balance is ${balance:.2f}")
            elif value <= 0:
                print("Invalid value. try again.")
            elif balance == 0:
                print(f"Your balance is: ${balance:.2f}")
            else:
                balance -= value
                statement += f"Withdraw: -${value:.2f}\n"
                print(f"Success withdraw! Now your balance is ${balance:.2f}")
                withdraw_counter += 1
                break
        else:
            print(f"You have exceeded the limit of {MAX_WITHDRAWS} withdrawals per day.")
    elif option == "s":
        if statement == "":
            print("There's no transactions in your account.")
        else:
            print("================STATEMENT================")
            print(statement + f"\nBalance: ${balance:.2f}")
            print("=========================================")
    elif option == "q":
        break
    else:
        print("Invalid operation. Check if the option selected exists.")