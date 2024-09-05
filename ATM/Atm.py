class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs{amount:.2f}.")
        else:
            print("Deposit amount must be positive.")



    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew Rs{amount:}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current balance: Rs{self.balance:}")


def main():
    atm = ATM()

    while True:
        print("\nATM Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Quit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            try:
                amount=float(input("Enter the money you want to deposite"))
                atm.deposit(amount)
            except ValueError:
                print("Invaild input Please enter a vaild input")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invaild input Please enter a vaild input")

        elif choice == '3':
            atm.display_balance()
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()







