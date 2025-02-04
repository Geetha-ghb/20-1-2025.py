print("-----control-statements: controls flow of execution of a code-----")
#there are 3 types of control statements---> conditional statements,loop and jump statements.

print("---control statements---")
num1 = 1
if num1 == 1:
    print("Pushpa The Rise")
else:
    print("Pushpa The Rule")
# if num>0 then print positive else print negative:
num = 1
if num > 0:
    print("positive")
else:
    if num == 0:   #if we want to give num=0 then we can write code like this:
        print("ZERO")
    else:
        print("Negative")
        if num == 1:
            print("ONE")
        else:
            print("positive")
            
#-----else is ->elif-----------

            
num = 1
if num > 0:
    print("positive")
elif num==1:
    print("ONE")
elif num==0:
     print("ZERO")
elif num==-1:
    print("negative")
elif num==-2:
    print("-2")

else:
    print("negative")


n=int(input("Enter units"))
if n <= 100:
   a = n*50 
   print(a)
else:
   if  n <= 201:
        print(n*100)
else


            
    
