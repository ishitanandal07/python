num=int(input("Enter a number = "))
sum=0
for digit in str(num):
    sum+=int(digit)

if num%sum==0:
    print("Niven number")
else:
    print("Not a niven number")

# Examples of niven number = 18,21,24,1729,100,102,108,120,1000,1008,1010,1020
# 18   1+8=9    18/9=2
# 12   1+2=3    12/3=4
# 21   2+1=3    21/3=7
# 24   2+4=6    24/6=4
# 100  1+0+0=1  100/1=100
# 102  1+0+2=3  102/3=34
# 108  1+0+8=9  108/9=12
# 120  1+2+0=3  120/3=40
# 1008 1+0+0+8=9 1008/9=112
# 1010 1+0+1+0=2 1010/2=505

# A niven number is a number that is divisible by sum of its digits