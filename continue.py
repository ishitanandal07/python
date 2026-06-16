# 1) Index value
age=[10,20,30,40,50]
for i in age:
    if i==30:
        continue
    print(i)

# 2) Odd 
age=[10,21,30,41,50]
for i in range(len(age)):
    if age[i]%2==0:
        continue
    print(age[i])