#jump statements:-->Break,continue,pause-Pause statement can only used in python not in other languages.
# break and Continue -> we use in loops

for i in range(0, 21):# no.of iterations:1 and then the output will be-->0
    if i%2 == 0:
        print(i)
    if i==0:
        break
for i in range (0,31):
    print(i)
    break
for i in range(0, 31):
    if i==2:
        break
    print(i)#no of iterations=3 o/p--> 0 1 2 when we give print statement before break statement it can gives output of 
# if we can give print statement it will output as--> 0 1  
#"------ continue--------":
for i in range(0,10):
    print(i, "iteration")
    if i==5 or i==6:
        continue
    print(i)   #
for i in range (0, 21):
    continue
    break      #for this code break is not used the loop will iterate with only contiue.
#break and continue foe nested loops:
for cls1 in range(1, 11):
    for roll in range (1, 31):
        if cls1 ==5:
            continue
        print(cls1, roll)# if we use use continue statement in this it will skip the class5 and continue the iteration and print remaining classes.
for cls1 in range(1, 11):
    for roll in range (1, 31):
        if cls1 ==5:
            break
        print(cls1, roll)
#if we want to skip roll no from above 15 from class 3.
for cls1 in range(1, 11):
    for roll in range (1, 30):
        if cls1 == 3 and roll > 15:
            continue
        print(cls1, roll)
#"-----pass------"
#by using this pass statement we can not get error but it can give o/p as empty.


num1 = 15
if num1%7 ==0:
   pass 
else:
    print("1234") #o/p----> empty
#terinary operator:
n1 = 5
n2 = 10
n1 =10 if n2%10 == 0 else 8
print(n1)
