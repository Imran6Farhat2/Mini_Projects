pin = "1234"
balance = 5000

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Deposit Successful.")
            print("New Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful.")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid Choice.")
else:
    print("Incorrect PIN.")