acc=int(input("Enter your account number = "))
account_number=1234567
current_balance=50000
if acc==1234567:
    print("Select from below option")
    print("1.Cash Withdrawal")
    print("2.Cash Deposit")
    print("3.Pin change")
    print("4.Cheque deposit")

    op=int(input("Enter your choice = "))
    if op==1:
        withdrawal_amount=int(input("Enter amount to be withdrawn = "))
        available_balance=current_balance - withdrawal_amount
        print("Available balance = ",available_balance)
        minimum_left_amount=3000
        if available_balance>=minimum_left_amount:
            print("Withdrawal allowed")
        elif available_balance<minimum_left_amount:
            print("Withdrawal not allowed")

    elif op==2:
        deposit_amount=int(input("Enter amount to be deposit = "))
        available_balance=current_balance + deposit_amount
        print("Available balance = ",available_balance)

    elif op==3:
        old_pin=2208
        pin=int(input("Enter new pin = "))

        if old_pin==pin:
            new_pin=int(input("Enter new pin = "))
            print("PIN successfully changed")
        else:
            print("Incorrect PIN")

    elif op==4:
        print("Cheque deposit selected")

    else:
        print("Invalid option chosen")
else:
    print("Invalid account number")
    
