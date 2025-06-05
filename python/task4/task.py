a=10
if (a>0):
    print("postive")
else:
    print("negative")    

a=50
if(a%2==0):
    print("add")
else:
    print("even")    

a=5
b=2
print(5*5)

a=2
if (a>=0):
    print("greater")
else:
    print("smaller")    
  

total=100
if total>=90 and total<=100:
       print("a")
elif total>=80 and total<=89:
     print("b")
elif total>=70 and total<=79:
     print("c")
elif total>=60 and total<=69:
     print("d") 
else:
     print("fail") 


age=int(input("enter your age"))
if age<16:
    print("you cant drive")
elif 16<= age <=17:
    print("you can drive but not vote")
elif 18<= age <=24:
    print("you can vote but not rent a car")
else:
    print("you can do pretty much everything")            

year=2025
if year %4==0 or year %100==0:
    print("leap year")
else:
    print("not leap year")    

year=2000
if year %400==0 or year %100==0:
    print("leap year")
else:
    ("not leap year")   

for i in range (1,100):
    if i%3==0 and i%5==0:
        print("fizz,buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz") 
    else:
        print(i)           
