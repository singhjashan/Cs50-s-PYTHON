#


import sys

def main():
    bnk = Bank()
    # print("Enter choice between /")
    while True:
        ch = input("Enter Y OR y to continue: ")
        if ch == 'Y' or ch == 'y':
            # print("Enter open or Open to open new account." )
            # print("Enter display or Display to view the Pass-Book.")
            # print("Enter deposit or Deposit to deposit the ammount.")
            # print("Enter withdraw or Withdraw to Withdraw the ammount.")
            print("{:<20} {:<50}".format('Command', 'Description'))
            print("{:<20} {:<50}".format('open OR Open', 'Open a new account'))
            print("{:<20} {:<50}".format('display OR Display', 'View the Pass-Book'))
            print("{:<20} {:<50}".format('deposit OR Deposit', 'Deposit the amount'))
            print("{:<20} {:<50}".format('withdraw OR Withdraw', 'Withdraw the amount'))

            choice = input("Which operation you want do :")

            if choice.lower() == "deposit":
                amunt = float(input("Enter amount to deposit in account :"))
                bnk.deposit(amunt)

            elif choice.lower() == "display":
                bnk.display()


            elif choice.lower() == "withdraw":
                amunt = float(input("Enter amount to withdraw from account :"))
                bnk.withdraw(amunt)

            elif choice.lower() == "open" :
                ac_no = int(input("Enter account number :"))
                name = input("Enter name of customer :")
                balance = float(input("Enter initial balance of this account :"))
                bnk.open(ac_no, name, balance)

            else:
                sys.exit("Invalid Input")


        else:
            sys.exit("Invalid Input")



class Bank:
    def __init__(self, ac_no=0, name="", balance=0):
        self.ac_no = ac_no
        self.name = name
        self.balance = balance

    def open(self, ac_no, name, balance):
        self.ac_no = ac_no
        self.name = name
        self.balance = balance
        return self.display()


    def display(self):
        account_details = {
            "Account number": self.ac_no,
            "Customer name": self.name,
            "Balance": self.balance
        }
        for key, value in account_details.items():
            print(f"{key}: {value}")

        return account_details

    def deposit(self, amount):
        self.balance += amount
        return self.display()

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.display()




if __name__ == "__main__":
    main()
