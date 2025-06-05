for i in range(1,11):
    print(i)

for i in range(1,20):
    if i%2==0:
        print(i)

for i in range(1,20):
    if i%2==1:
        print(i)

sum=0
for i in range(1,100):
    sum=sum+i
print(sum)   

for i in range(1,6):
    print(i)

even=0
odd=0
for i in range(10,55):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1   
print("even",even)
print("odd",odd)    

    
list=[23,4,-6,23,-9,21,-3,-45,8] 
pos=[]
neg=[] 
for i in range(len(list)):
    if list[i]>0:
        pos.append(list[i])
    else:
        neg.append(list[i])
print(pos) 
print(neg)       

num1 =int(input("Enternum1 "))
num2 =int(input("Enternum2 "))
if num1>num2:
    print("num1 is greater than num 2")
elif num1<num2: 
    print("num2 is greater than num 1") 
else:
    print("equal")          

num1=int(input("enter num 1 "))
num2=int(input("enter num 2 "))
num3=int(input("enter num 3 "))
if num1>num2 and num1>num3:
    print("num 1 is greater")
elif num2>num1 and num2>num3:
    print("num 2 is greater")
elif num3>num1 and num3>num2:
    print("num3 is greater")
else:
    print("three are equal")     

for i in range(1,26):
    if i%5==0:
        i=i+1
    else:
        print(i)

sum=1
for i in range(1,7):
    sum=sum*i
print(sum)

list=[1,2,3,4,5]
sum=0
for i in range(len(list)):
    sum=sum+(list[i])
    avg=sum//(len(list))
print(avg)    

for i in range(1,11):
    print(i)

a=(input("enter a character"))
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("vowels")
else:
    print("constent")    

list=[10,20,30,40,10]
first=list[0]
last=len(list)-1
if first==list[last]:
    print("same")
else:
    print("not same")    

row=6
for i in range(1,row):
    print("*"*i)


sum=0
b=[1,2,5,5,7,4,2]
for i in range(len(list)):
    sum=sum+list[i]
print(sum)    




            
