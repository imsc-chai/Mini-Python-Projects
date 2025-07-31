class Account:
    def __init__(self, username):
        self.username = username
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}/-")
        print(f"Deposited {amount}/- successfully.\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance.\n")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}/-")
            print(f"Withdrawn {amount}/- successfully.\n")

    def check_balance(self):
        print(f"Current Balance: {self.balance}/-\n")

    def mini_statement(self):
        print(f"--- Mini Statement for {self.username} ---")
        for t in self.transactions[-5:]:  
            print(t)
        print(f"Available Balance: {self.balance}/-")
        print("----------------------------------------\n")
        
        
class BankManagement:
    def __init__(self):
        self.users = {}  

    def create_account(self):
        username = input("Enter a unique username: ")
        if username in self.users:
            print("Username already exists. Try a different one.\n")
            return

        password = input("Enter password: ")
        confirm = input("Confirm password: ")

        if password != confirm:
            print("Passwords do not match. Try again.\n")
            return

        self.users[username] = (password, Account(username))
        print("Account created successfully!\n")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username][0] == password:
            print(f"Welcome {username}! You have successfully logged in.\n")
            return self.users[username][1]  
        else:
            print()
            print("==========================================================")
            print("Incorrect username or password.\n[Hint]: Create an Account If you haven't already.")
            print("==========================================================")
            return None

def main():
    bank = BankManagement()

    while True:
        print()
        print("====== Welcome to MSC Bank ======")
        print()
        print("1. Create Account")
        print()
        print("2. Login")
        print()
        print("3. Exit")
        print()
        choice = input("Please choose an option between [1-3]: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            account = bank.login()
            if account:
                while True:
                    print("----- Logged In Menu -----")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Mini Statement")
                    print("5. Logout")

                    option = input("Choose an option (1-5): ")

                    if option == "1":
                        amount = int(input("Enter amount to deposit: "))
                        account.deposit(amount)

                    elif option == "2":
                        amount = int(input("Enter amount to withdraw: "))
                        account.withdraw(amount)

                    elif option == "3":
                        account.check_balance()

                    elif option == "4":
                        account.mini_statement()

                    elif option == "5":
                        print("Logged out successfully.\n")
                        break

                    else:
                        print("Invalid choice. Try again.\n")

        elif choice == "3":
            print()
            print("======================================")
            print()
            print("Thank you for using MSC Bank. Goodbye!")
            print()
            print("======================================")
            break

        else:
            print("Invalid choice. Please try again.\n")

main()        