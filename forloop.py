# 1) even number between 1 to 50 
for i in range (1,51):
    if (i%2==0):
        print(i)

# 2) odd number between 1 to 50 
for i in range (1,51):
    if (i%2==1):
        print(i)

# 3) multiplication table of 7
for i in range (1,11):
    print("7 *", i , "=", 7*i)


# 4) square of numbers from 1 to 20
for i in range(1,21):
    print(i**2)

# 5) cube of numbers from 1 to 10 
for i in range(1,11):
    print(i**3)

# 6) numbers from 1 to 10 
for i in range(1,11):
    print(i)

# 7) numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

# 8) number divisible by 3
for i in range (1,101):
    if (i%3==0):
        print(i)

# 9) string count
s="ishita"
count=0
for ch in s:
    count=count+1
print(count)

# 10) string
s="Nandal"
for ch in s:
    print(ch)

# 11) count vowels in a string
s="ishita"
vowels="aeiou AEIOU"
count=0
for ch in s:
    if ch in vowels:
        count=count+1
    print("vowels = ",count)


# 12) count consonant in a string
s="ishita"
vowels="aeiou AEIOU"
count=0
for ch in s:
    if ch not in vowels:
        count=count+1
    print("consonant",count)


# 13) Print only consonant in a string
s="ishita"
vowels="aeiou AEIOU"
for ch in s:
    if ch not in vowels:
        print(ch)


# 14) Print only vowels in a string
s="ishita"
vowels="aeiou AEIOU"
for ch in s:
    if ch in vowels:
        print(ch)


# 15) reverse a string
s="ishita nandal"
rev=""
for ch in s:
    rev=ch+rev
print("reversed string = ",rev) 


# 16) to get power (n) of any number 
def power(n):
 for i in range(1,11):
    print(n**i)
    
num=int(input("Enter any number = "))
power(num)


# 17) reverse of a list
age=(12,18,20,14,21)
for i in range(-1,-6,-1):
    print(age[i])

# 18) printing list using range of its length
list=[100,200,300,400,500,600] 
for i in range(len(list)):
    print(list[i])
