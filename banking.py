class BankAccount:
    def __init__(self): #feeding customer user name password and balance
        self.accounts = {'gautham': {'password': '12345', 'balance': 100, 'transactions': []},
                         'alex': {'password': 'qwerty', 'balance': 400, 'transactions': []}}

    def login(self, username, password): #checking user name and password
        if username in self.accounts and self.accounts[username]['password'] == password:
            return True
        else:
            return False

    def deposit(self, username, amount): # adding deposited amount
        self.accounts[username]['balance'] += amount
        self.accounts[username]['transactions'].append(f"Deposited: {amount}")

    def withdraw(self, username, amount): #checking suffiennt balance
        if amount > self.accounts[username]['balance']:
            print("Sorry, you don't have enough money in your account.")
        else:
            self.accounts[username]['balance'] -= amount
            self.accounts[username]['transactions'].append(f"Withdrew: {amount}")

    def check_balance(self, username): #display current balance
        print(f"Your current balance is: {self.accounts[username]['balance']}")

    def view_transactions(self, username): #transaction history
        print("Transaction History:")
        for transaction in self.accounts[username]['transactions']:
            print(transaction)

bank = BankAccount()

username = input("Enter your username:")
password = input("Enter your password:")

if bank.login(username, password):
    print("Login successful.")
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Transactions\n5. Exit")
        choice = input("Please select any option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(username, amount)
            bank.check_balance(username)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(username, amount)
            bank.check_balance(username)
        elif choice == '3':
            bank.check_balance(username)
        elif choice == '4':
            bank.view_transactions(username)
        elif choice == '5':
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid username or password. Please try again.")
