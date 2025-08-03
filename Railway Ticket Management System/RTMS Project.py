import random

class Account():
    users = {}

    def create_account(self, username, password):
        if username in Account.users:
            print("Username already Exists. Please use a New one: ")
            return False
        Account.users[username] = password
        print("Account Created Successfully")
        return True
    
    def login(self, username, password):
        if username in Account.users and Account.users[username] == password:
            print("Login Successfull")
            return True
        else:
            print("Invalide Username or Password")
            return False
        
# ---------------------------------------------------------------------------------------------------------------------------------

class Train():
    def __init__(self, number, source, destination, seats):
        self.number = number
        self.source = source
        self.destination = destination
        self.seats = seats

    def display(self):
        print(f"Train No: {self.number} --> From: {self.source} | Destination: {self.destination} | Seats Available: {self.seats}")

# ---------------------------------------------------------------------------------------------------------------------------------
        
class Passenger():
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

# -----------------------------------------------

class Ticket():
    def __init__(self, train, passengers):
        self.train = train
        self.passengers = passengers
        self.pnr = self.generate_pnr()

    def generate_pnr(self):
        return "PNR" + str(random.randint(4000, 9999))
    
    def display_ticket(self):
        print(f"\n--- Ticket Confirmed ---\nPNR: {self.pnr}")
        print(f"Train: {self.train.number} | {self.train.source} to {self.train.destination}")

        for p in self.passengers:
            print(f"Passenger: {p.name}\nAge: {p.age}\nGender: {p.gender}\nPhone: {p.phone}")
        print("---------------------------")


# --------------------- Main Program ----------------------------

class RailwaySystem():

    def __init__(self):
        self.account = Account()

        self.trains = [
            Train("101", "Hyderabad", "Delhi", 5),
            Train("202", "Mumbai", "Chennai", 6),
            Train("303", "Bangalore", "Kolkata", 9)
        ]

        self.logged_in_user = None

    def Menu(self):
        while True:
            print("\n--- Railway Ticket Management System ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Book Ticket")
            print("4. Logout")
            print("5. Exit")


            choice = input("Enter Choice: ")

            if choice == '1':
                uname = input("Enter Username: ")
                pwd = input("Enter Password: ")

                self.account.create_account(uname, pwd)

            elif choice == '2':
                uname = input("Enter username: ")
                pwd = input("Enter password: ")

                if self.account.login(uname, pwd):
                    self.logged_in_user = uname

            elif choice  == '3':
                if not self.logged_in_user:
                    print("You must log in First to Book Tickets!")
                    continue

                self.book_tickets()   # We will Define Later, Keep it aside.
            
            elif choice == '4':
                self.logged_in_user = None
                print("Logged Out Successfully")

            elif choice == '5':
                print("Thank you for using Railway Ticket System!")
                break
            else:
                print("Invalid Choice. Try Again: ")
            

    def book_tickets(self):    # Now Defining it... Cool
        print("\nAvailable Trains: ")

        for trains in self.trains:
            trains.display()

        train_num = input("Enter Train Number to Book: ")
        selected_train = None

        for train in self.trains:
            if train.number == train_num:
                selected_train = train
                break
        
        if not selected_train:
            print("Invalid Train Number: ")
            return
        

        try:
            count = int(input("Enter Number of Tickets to Book: "))
            if count > selected_train.seats:
                print("Not enough seats available.")
                return
        except ValueError:
            print("Please Enter a valid Number.")
            return
        

        passengers = []

        for i in range(count):
            print(f"\nEnter details for Passenger {i+1}: ")
            name = input("Name: ")
            try:
                age = int(input("Age: "))
                if age < 0 or age > 120:
                    print("Invalid Age!")

            except ValueError:
                print("Invalid Age!")
                return
            
            gender = input("Gender [Male or Female]: ")
            phone = input("Enter your 10 Digit Mobile Number: ")

            if not phone.isdigit() or len(phone) != 10:
                print("Invalid phone number!")
                return
            
            passengers.append(Passenger(name, age, gender, phone))

        selected_train.seats -= count

        ticket = Ticket(selected_train, passengers)

        ticket.display_ticket()


if __name__ == "__main__":
    system = RailwaySystem()
    system.Menu()       



            
    











        



            





            



            

            


