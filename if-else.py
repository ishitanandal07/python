# 1) GRADE-SYSTEM
marks=int(input("Enter your marks = "))
if marks>90:
    print("GRADE A")
elif marks>80:
    print("GRADE B")
elif marks>70:
    print("GRADE C")
elif marks>60:
    print("GRADE D")
else:
    print("Fail")



# 2) to check entered number is +ve, -ve or zero
num=int(input("Enter any number = "))

if num<0:
    print("Number is negative")
elif num>0:
    print("Number is positive")
else:
    print("Number is zero")


# 3) Among three numbers which is greater 
num1=int(input("Enter value of num1 = "))
num2=int(input("Enter value of num2 = "))
num3=int(input("Enter value of num3 = "))
if (num1>num2 and num1>num3):
    print("num1 is the greatest number")
elif (num2>num1) and (num2>num3):
    print("num2 is the greatest number")
else:
    print("num3 is the greatest number")


# 4) percentage of 5 numbers
s1=int(input("Enter Maths marks = "))
s2=int(input("Enter English marks = "))
s3=int(input("Enter Hindi marks = "))
s4=int(input("Enter Science marks = "))
s5=int(input("Enter social science marks = "))
percentage=(s1+s2+s3+s4+s5)/500*100
print("Your percentage is = ",percentage)
if percentage<91:
    print("A+")
elif percentage<81:
    print("A")
elif percentage<71:
    print("B")
elif percentage<61:
    print("C")
elif percentage<51:
    print("D")
elif percentage<41:
    print("E")
else:
    print("Fail")


# 5) checking vowel or consonant
a1=str(input("Enter any alphabet = "))
if a1=='a' or a1=='e' or a1=='i' or a1=='o' or a1=='u' or a1=='A' or a1=='E' or a1=='I' or a1=='O' or a1=='U':
    print("Vowel")
else:
    print("Consonant")


# 6) Leap year
y=int(input("Enter any year = "))
if (y%4==0 or y%100==0 or y%400==0):
    print("It is a leap year")
else:
    print("It is not a leap year")


# 7) Types of Triangle
s1=int(input("Enter one side of triangle = "))
s2=int(input("Enter second side of triangle = "))
s3=int(input("Enter third side of triangle = "))
if s1==s2 and s1==s3 and s2==s3:
    print("Equilateral triangle")
elif s1==s2 and s2==s3 or s3==s1:
    print("Isoceles triangle")
else:
    print("Scalene triangle")


# 8) Finding SI
CP=float(input("Enter cost price = "))
SP=float(input("Enter selling price = "))
loss=CP-SP
profit=SP-CP
if CP>SP :
    print("Loss",loss)
else:
    print("Profit",profit)


