#logical operators:
#logical AND,logical OR,logical Not
print(True and True)
print(False and True)
print(True and False)
print(False and (True and False))
print(True and False)

print("----Numbers---")
print("----And operations---")

#Here when we give numbers it will check the first digit of that number or anything is true then it will check the second value,the output will be the second value
 #if the first one is false then the value is printed the first value it does not check the second value.
print (2 and 3)   #o/p: 3
print (3 and 2)   #o/p: 2
print (3 and "")  #o/p: empty string will be the output
print ("" and 0)  #o/p: empty string
print (-1 and 3)  #o/p: 3
print (0 and "")  #o/p: 0
print (False and 45)#o/p: False 
print (None and 3)#o/p: none

print("----OR operations---")

print(2 or 3)  #o/p:2
print("" or 2) #o/p:2
print(0 or "") #o/p: empty string
print(0 or True)#o/p: true
print(0 or 0 or 2)#o/p:2

print("----Not operations---")
# Note: it will gives output as boolean values.
print(not True)
print(not False)
print(not (2 or 3))
print(not("" and 3))


print("----Bitwise operations---")
#&,|,^,~,>>,<<
print("----and operation---")
print(4 & 3)
print(12 & 14)
#0100 & 0011 => 0000=0
#1100 & 1110 => 1100=12

print("----OR operations---")
print(12 | 14)
#1100 | 1110 => 1110=14
print("----XOR operations---")
print(12 ^ 14)
#1100 ^ 1110 =>0010=2

#left shift-->
#right shift-->
print (3 << 1) #o/p: 6
print (3 >> 1) #o/p: 2

print(29






