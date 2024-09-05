class Atm:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount: {amount}")
        else:
            print("Error: Enter a positive number")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn amount: {amount}")
            else:
                print("Error: You don't have sufficient balance")
        else:
            print("Error: Enter a positive amount")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def quit(self):
        print("Thank you for using this ATM")


def main():
    atm = Atm()  # Initialize ATM with default balance

    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")

        option = int(input("Select option 1-4: "))

        if option == 1:
            amount = float(input("Enter your deposit amount: "))
            atm.deposit(amount)
        elif option == 2:
            amount = float(input("Enter your withdrawal amount: "))
            atm.withdraw(amount)
        elif option == 3:
            atm.check_balance()
        elif option == 4:
            atm.quit()
            break
        else:
            print("Invalid input, please choose a valid option")


if __name__ == "__main__":
    main()































