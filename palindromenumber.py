num=int(input("Enter any number = "))
original=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev) 
if rev==original:
    print("The number entered is a Palindrome number")
else:
    print("The number entered is not a Palindrome number")

# A palindrome number is a number that remains the same when its digits are reversed

# Examples of palindrome number = 121,1331,454
