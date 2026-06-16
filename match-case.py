# 1) Calculator
num1=float(input("Enter any number = "))
num2=float(input("Enter any number = "))

value=input("Enter any operation you want to perform = ")

match value:
    case "1":
        print("Your answer is = ", num1+num2)
    case "2":
        print("Your answer is = ", num1-num2)
    case "3":
        print("Your answer is = ", num1*num2)
    case "4":
        print("Your answer is = ", num1/num2)
    case _:
        print("Invalid operation")


# 2) days
value=int(input("Enter any number between 1 & 7 = "))
match value:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")


# 3) Grade system
grade=input("Enter your grade A/B/C/D/F")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")


# 4) even/odd
num=int(input("Enter any number = "))
match num%2:
    case 0:
        print("Entered number is even")
    case 1:
        print("Entered number is odd")
    case _:
        print("Invalid")
