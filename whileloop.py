# 1) find the largest number in a list
age=[100,22,310,40,85,21,800,89,500,52]
largest=age[0]
i=0
while i<len(age):
    if largest<age[i]:
        largest=age[i]
    i=i+1
print("Largest number = ",largest)

# 2) Find the smallest number in a list
age=[100,200,300,400,500,600]
smallest=age[0]
i=0
while i<len(age):
    if smallest>age[i]:
        smallest=age[i]
    i=i+1
print("Smallest number = ",smallest)

# 3) finding sum of all elements of digits
age=[100,200,300,400,500,600]
sum=0
i=0
while i<len(age):
    sum=sum+age[i]
    i=i+1
print("Sum = ",sum)

# 4) finding total number of elements in a list 
numbers=[22,8,24,54,70,92,30,89,50,52]
count=0
i=0
while i<len(numbers):
    count=count+1
    i+=1
print("Total number of elements are ",count)

# 5) to find how many even numbers are there in a list
numbers=[100,23,310,40,85,21,500,89,50,52]
even_count=0
i=0
while i<len(numbers):
    if numbers[i]%2 !=0:
        even_count+=1
        print(numbers[i])

    i+=1
print("Total Number of even numbers = ",even_count)

# 6) to find average 
numbers=[100,22,310,40,85,21,500,89,50,52]
i=0
total=0
while i<len(numbers):
    total += numbers[i]
    i+=1
    average=total/len(numbers)
    print("Average = ",average)

# 7) to find product
numbers=[2,3,4,5]
i=0
product=1

while i<len(numbers):
    product *= numbers[i]
    i += 1
    print("Product = ",product)

# 8) find the range (difference between largest and smallest)
numbers=[100,22,310,40,85,21,500,89,50,52]
i=0
largest=numbers[0]
smallest=numbers[0]

while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    if numbers[i]<smallest:
        smallest=numbers[i]
    
    i += 1
range=largest - smallest
print("Range (largest-smallest):",range)

# 9) finding total number of repeating elements (frequency)
numbers=[1,2,2,3,4,1,2,3]
frequency={}
i=0

while i<len(numbers):
    element=numbers[i]
    if element in frequency:
       frequency[element] +=1
    else:
        frequency[element]=1
    i += 1 
print("Frequency (number of repeating elements)",frequency)


# 10) reversed list
numbers=[1,2,3,4,5]

reversed_list=[]
i=len(numbers)-1

while i>=0:
    reversed_list.append(numbers[i])
    i -= 1
print(reversed_list)

# 11) average 
age=(10,20,30,40,50)
sum=0
i=0
while i<len(age):
    sum=sum+age[i]
    i=i+1
print("average:",sum/len(age))
