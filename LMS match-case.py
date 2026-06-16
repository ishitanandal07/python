print("Please select your department")
print("1. Mechanical dept.\n 2. Chemistry dept.\n 3. Computer dept.\n 4.English dept.")

dept=int(input("Enter your department = "))

match dept:
    case 1:
        print("Welcome to Mechanical dept.")
    case 2:
        print("Welcome to Chemistry dept.")
    case 3:
        print("Welcome to Computer dept.")
    case 4:
        print("Welcome to english dept.")
    case _:
        print("Invalid department")

        if dept>0 and dept<=4:

            print("Select what you want to check")
            print("1.Attendence status\n 2.Fees status\n 3.Books issued\n 4.Calculate percentage")
        else:
            print("Invalid Department")

choice=int(input("Enter your choice here = "))

match choice:
    case 1 :
        total_attendence=int(input("Enter total working days of sem = "))
        attended_days=int(input("Enter total days you attended classes = "))
        attendence=attended_days/total_attendence*100
        print("You attendence status is = ",attendence)

    case 2 :
        total_fees=24000
        fees_paid=int(input("Enter fees you have paid"))
        pending_fees=total_fees - fees_paid
        advance_deposit=fees_paid - total_fees

        if fees_paid==total_fees:
            print("Your fees is paid")
        elif fees_paid<total_fees:
            print("Your fees is pending")
            print("Your pending fees is = ",pending_fees)
        elif fees_paid>total_fees:
            print("You have paid advance deposit")
            print("Your advance deposit is = ",advance_deposit)
        else:
            print("Invalid amount")
    
    case 3:
        issued_book=int(input("Enter number of books you have issued = "))
        ret=int(input("Enter number of books you have returned = "))
        days=int(input("Enter number of days you kept books = "))
        if days>10:
            fine=(days-10)*2
            print("Your fine is = ",fine)
        else:
            print("You have no fine")
    case 4:
        s1=int(input("Enter your first subject marks = "))
        s2=int(input("Enter your second subject marks = ")) 
        s3=int(input("Enter third subject marks = "))     

        percentage=(s1+s2+s3)/300*100
        print("Your percentage is = ",percentage)

    case _:
        print("Invalid choice")