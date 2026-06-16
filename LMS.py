roll_no=int(input("Enter your roll no. = "))
password=int(input("Enter your password = "))

if roll_no>100 and roll_no<=120 and password==12345:
    print("Please select your department")
    print("1 Mechanical dept.")
    print("2 Chemistry dept.")
    print("3 Computer dept.")
    print("4 English dept. ")

    choice=int(input("Enter your choice = "))

    if choice>=1 and choice<=4:
        print("Select which information you required")
        print("1 Your attendence status")
        print("2 Your fees")
        print("3 Book issued")
        print("4 Calculate your percentage")

        option=int(input("Enter chosen option = "))
        if option==1:
            total_attendence=int(input("Enter total working days of sem = "))
            attended_days=int(input("Enter no.of classes you attended = "))
            attendence=attended_days/total_attendence*100
            print("Your attendence status(percentage) is = ")

        elif option==2:
            total_fees=24000
            fees_paid=int(input("Enter fees you have paid = "))
            pending_fees=total_fees - fees_paid
            advance_deposit=fees_paid - total_fees

            if fees_paid==total_fees:
                print("Your fees is paid")
            elif fees_paid<total_fees:
                print("Your pending fees is = ",pending_fees)
            elif fees_paid>total_fees:
                print("You have paid advance fees = ",advance_deposit)
            else:
                print("Invalid amount entered")
    
        elif option==3:
            issued_book=int(input("Enter no. of books you have issued = "))
            ret=int(input("Enter no. of books you have returned = "))
            days=int(input("Enter no. of days you kept books = "))
            if days>10:
                fine=(days-10)*2
                print("You have to pay fine",fine)

            else:
                print("You have no fine")
        
        elif option==4:
            s1=int(input("Enter your first subject marks = "))
            s2=int(input("Enter your second subject marks = "))
            s3=int(input("Enter your third subject marks = "))

            percentage=(s1+s2+s3)/300*100
            print("Your percentage is = ",percentage)
    
        else:
            print("Invalid option")
    else:
        print("Invalid department choice")
else:
    print("Invalid login credential")


