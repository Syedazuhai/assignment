transactions = []

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        transactions.append(f"Deposited £{amount:.2f}")
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("You have insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        transactions.append(f"Withdrew £{amount:.2f}")
        return amount

def show_balance(balance):
    print(f"Your balance is £{balance:.2f}")

def show_transactions():
    print("Transaction History:")
    for transaction in transactions:
        print(transaction)

def main():
    balance = 900
    running = True
    pin = "1234"
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempt(s) left.")
    
    if attempts == 0:
        print("Access denied. Too many incorrect attempts.")
        return

    while running:
        print("\nATM Program")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Show Transactions")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            balance += deposit()
        elif choice == '2':
            balance -= withdraw(balance)
        elif choice == '3':
            show_balance(balance)
        elif choice == '4':
            show_transactions()
        elif choice == '5':
            running = False
        else:
            print("That is not a valid choice")

    print("Thank you! See you next time!")

if __name__ == '__main__':
    main()
