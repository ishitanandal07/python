num=int(input("Enter any number = "))
original=num
square=num*num
sum=0

while square>0:
    rem=square%10
    sum=sum+rem
    square=square//10

print(sum)

if sum==num:
    print("Num is a neon number")

else:
    print("Num is not a neon number")

# A neon number is a number where the sum of the digits of its square is equal to the original number

# Examples of neon number 
# 9**2=81   8+1=9
# 1**2=1    1=1