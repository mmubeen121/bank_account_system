from app.services.account_manager import AccountManager

def main():
    manager = AccountManager()
    while True:
        print("\n--- Bank Account System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter account holder name: ")
                balance = float(input("Enter opening balance: "))
                account = manager.create_account(name, balance)
                print(f"Account created successfully. Account No: {account.account_no}")

            elif choice == "2":
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                manager.deposit_to_account(acc_no, amount)
                print("Amount deposited successfully")

            elif choice == "3":
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                manager.withdraw_from_account(acc_no, amount)
                print("Amount withdrawn successfully")

            elif choice == "4":
                acc_no = int(input("Enter account number: "))
                details = manager.get_account_details(acc_no)
                print(details)

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")

        if __name__ == "__main__":
            main()