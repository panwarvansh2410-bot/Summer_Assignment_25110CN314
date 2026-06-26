balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Available Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Deposit Successful!")
            print("Updated Balance:", balance)

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")