# 1) To fill data in empty dictionary and then delete
M={}
n=int(input("Enter number of students = "))
for i in range(n):
    rollno=int(input("Enter roll no. = "))
    name=input("Enter Name = ")
    M[rollno]=name
print(M)

a=input("If you entered wrong data please enter (YES) to change other enter (NO) = ").upper()

if (a=="YES"):
    print("To delete data")
    print(M)
    print("Check if you entered the wrong data")

    r=int(input("Enter Roll no:"))
    if r in M:
        del M[r]
        print("Roll no: ",r,"is deleted")
    else:
        print(M)
else:
    print("The entered data is correct")


# 2) To check highest marks/lowest marks/range 
M={}
n=int(input("Enter number of students = "))

for i in range(n):
    rollno = int(input("Enter roll no. = "))
    marks= int(input("Enter marks = "))
    M[rollno]= marks
print(M)

marks=list(M.values())
print(marks)
highest = marks[0]
i=0
while i < len(marks):
    if highest < marks[i]:
        highest = marks[i]
    i += 1
print("Highest:",highest)

lowest=marks[0]
i=0

while i < len(marks):
    if lowest>marks[i]:
        lowest=marks[i]
    i+=1
print("Lowest:",lowest)

i=0
highest=marks[0]
lowest=marks[0]

while i < len(marks):
    if marks[i]>highest:
        highest=marks[i]

    if marks[i]<lowest:
        lowest=marks[i]

    i+=1
range = highest - lowest
print("Range (Highest-Lowest) = ",range)

rollno=list(M.keys())
print(rollno)

largest=rollno[0]
i=0
while i < len(rollno):
    if largest<rollno[i]:
        largest=rollno[i]
    i+=1

print("largest:",largest)

smallest=rollno[0]
i=0
while i < len(rollno):
    if smallest>rollno[i]:
        smallest=rollno[i]
    i+=1

print("Smallest:",smallest)

i=0
largest=rollno[0]
smallest=rollno[0]

while i < len(rollno):
    if rollno[i]>largest:
        largest=rollno[i]
    if rollno[i]<smallest:
        smallest=rollno[i]

    i+=1

range = largest - smallest
print("Range (Largest - smallest):",range)


# 3) To get sum of even/odd index values of list of values of a dictionary
d={101:55,102:50,103:60,104:65,105:45}
v=list(d.values())
print(v)
sum=0
for i in range(len(v)):
    v[i]%2==0
    sum=sum + v[i]

print("Sum of even digits = ",sum)

sum=0
for i in range(len(v)):
    v[i]%2!=0
    sum=sum + v[i]

print("Sum of odd digits =",sum)


# 4) Adding new key-value pair in dictionary
d={"Name":"Ishita","Age":21,"Course":"MHon"}
d["Another course"]="AIA"
print(d)


# 5) Merging two dictionaries
dict1={"Name":"Ishu","Age":21}
dict2={"Course":"Maths Honours"}

dict1.update(dict2)
print("Merged dictionary = ",dict1)


# 6) Finding sum of all values of dictionary
d={101:50,102:55,103:60,104:65,105:45}
v=list(d.values())
sum=0
for i in range(len(v)):
    sum=v[i]+sum
print("Sum of digits = ",sum)


# 7) Checking key exist or not
dict={"a":10,"b":20,"c":30}
key=input("Enter key you wanna check = ")
if key in dict:
    print("Key exists in dictionary")
else:
    print("Key does not exists in dictionary")