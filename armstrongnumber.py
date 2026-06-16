num=int(input("Enter any number = "))
original=num
sum=0

a=str(num)
count=0

for ch in a:
    count=count+1

while num>0:
    rem=num%10

    if count==3:
        sum=sum+(rem*rem*rem)
    elif count==4:
        sum=sum+(rem*rem*rem*rem)
    elif count==5:
        sum=sum+(rem*rem*rem*rem*rem)
    elif count==6:
        sum=sum+(rem*rem*rem*rem*rem*rem)
    else:
        print("invalid")
    
    num=num//10

if original==sum:
    print("Number is Armstrong number")
else:
    print("Number is not an Armstrong number")


# Examples of armstrong number
# 153   1**3=1     5**3=125    3**3=27  1+125+27=153
# 370   3**3=27    7**3=343    0**3=0   27+343+0=370
# 371   3**3 + 7**3 + 1**3=371
# 407   4**3 + 0**3 + 7**3=407
# Four digits number examples = 1634,8208,9474

# An armstrong number is a number that is equal to sum of its digits raised to the power of total number of digits

