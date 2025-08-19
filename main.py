import datetime

# Show Welcome message
print("WELCOME TO MEST ATM")
print("Please insert your atm card")

# Ask user to insert the card
user_card_name = input("Enter your name>> ")
user_card_number = int(input("Enter your serial number>> "))

# Global variables
user_pin = 4190
current_balance = 10000.00
transaction_history = []

def pin_authentication():
    while True:
        try:
            pin = int(input("Enter your pin>> "))
            if pin == user_pin:
                print("Login Successful")
                return True
            else:
                print("Authentication Failed")
        except ValueError:
            print("Invalid input. Please enter a number.")

def deposit():
    global current_balance
    global transaction_history
    try:
        amount = float(input("Enter the amount to deposit>> "))
        if amount > 0:
            current_balance += amount
            print(f"Successfully deposited GHS {amount:.2f}.")
            print(f"Your new balance is GHS {current_balance:.2f}.")
            # Add transaction to history
            transaction_history.append({
                'type': 'Deposit',
                'amount': amount,
                'balance': current_balance,
                'timestamp': datetime.datetime.now()
            })
        else:
            print("Invalid amount. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdrawal():
    global current_balance
    global transaction_history
    try:
        amount = float(input("Enter the amount to withdraw>> "))
        if amount <= 0:
            print("Invalid input.")
        elif amount <= current_balance:
            current_balance -= amount
            print("Withdrawal successful, please take your cash.")
            # Add transaction to history
            transaction_history.append({
                'type': 'Withdrawal',
                'amount': amount,
                'balance': current_balance,
                'timestamp': datetime.datetime.now()
            })
        else:
            print("Insufficient balance.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_transaction_history():
    print("\n--- Transaction History ---")
    if not transaction_history:
        print("No transactions have been made yet.")
    else:
        for transaction in transaction_history:
            print(f"Type: {transaction['type']}")
            print(f"Amount: GHS {transaction['amount']:.2f}")
            print(f"New Balance: GHS {transaction['balance']:.2f}")
            print(f"Timestamp: {transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 25)

def choices():
    while True:
        print("\n--- ATM Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Transaction History")
        print("5. Exit")
        
        options = input("Choose an option>> ")
        
        if options == "1":
            print(f"Your current balance is GHS {current_balance:.2f}")
        elif options == "2":
            deposit()
        elif options == "3":
            withdrawal()
        elif options == "4":
            show_transaction_history()
        elif options == "5":
            print("Thank you for using the MEST ATM. Goodbye!")
            break  
        # Exits the while loop and ends the program
        else:
            print("Invalid choice. Please choose from the options.")

# --- Main Program Flow ---
if pin_authentication():
    choices()