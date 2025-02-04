#Conversions form integer:
num1=123
print (int(num1))#output:123

#integer to float:
num1=123
int=(float(num1))
print(float)  #output: 123.0

#integer to string:
num = 123
str_num = str(num)
print(str_num)  # Output: "123"

#integer to boolean:
num=1
bool=bool(num)
print(bool)   #output: "True"

#integer to list:
num1=123
list=list(num1)
print(num1)    #output:type error

integer to tuple:
num1=123
tuple=tuple(num1)
print(tuple)   # output: type error

#integer to dictinary:
num1=123
print(dict(num1))

#integer to range:
x = range(54)
print(x) #output: range(0, 54)

#conversions from float:

#float to int:
float = 12.99
int= int(float)
print(int)  # Output: 12

#float to float:
a=22.566
b=float(a)
print(b) #output:22.566

#float to string:
a = str(5.8)  
print(a) # Output: '5.8'

#float to bool:
a = bool(0.0)  
b = bool(5.8)
print(a) # Output: False
print(b) # Output: True

#float to list
a = list(5.8)
print(a) # TypeError

#float to tuple
a = tuple(5.8)
print(a) # TypeError

#float to set:
a = set(5.8)
print(a) # TypeError

#float to dict
a = dict(5.8)
print(a) # TypeError

#float to range
a = range(5.8)  
print(a) # TypeError

#string conversions

#string to integer:


c = int("123")
print(c) # Output: 123

#str to float:

c = float("123.45")
print(c) # Output: 123.45

#str to str:
c = str("hello")
print(c) # Output: 'hello'

#str to bool:
c = bool("True")
print(c) # Output: True
d = bool("")
print(d) # Output: False

#str to list:
c = list("hello")
print(c) # Output: ['h', 'e', 'l', 'l', 'o']

#str to tuple
c = tuple("hello")
print(c) # Output: ('h', 'e', 'l', 'l', 'o')

#str to set:
c = set("hello")
print(c) # Output: {'h', 'e', 'l', 'o'}

#str to dict:
import json
c = json.loads('{"key": "value"}')
print(c) # Converts a valid JSON string to a dictionary

#str to range:
# A string cannot be directly converted to a range, first we need to convert the string to an integer and then create a range.
number = int("5")
print(range(number))  # Output: range(0, 5)


bool conversions:

#bool to int:
a = int(True)
print(a) # Output: 1
b = int(False)
print(b) # Output: 0

#bool to float:
a = float(True)
print(a) # Output: 1.0
b = float(False)
print(b) # Output: 0.0

#bool to str:
a = str(True)
print(a) # Output: 'True'
b = str(False)
print(b) # Output: 'False'

#bool to bool:
a = bool(True)
print(a) # Output: True
b = bool(False)
print(b) # Output: False

#bool to list:
a = list(True)
print(a) # TypeError

#bool to tuple:
a = tuple(True)
print(a) # TypeError 

#bool to set:
a = set(True)
print(a) # TypeError

#bool to dict:
a = dict(True)
print(a) # TypeError

#bool to range:
# A boolean cannot be directly converted to a range, first we need to convert the string to an integer and then create a range.
a = range(int(True))
print(a) # Output: range(0, 1)


#list conversions:

#list to int:
my_list = [1, 2, 3]
int(my_list[0])  # Output: 1 (converting only the first element)

#list to float:
my_list = [1.1, 2.2, 3.3]
print(float(my_list[0]))  # Output: 1.1 (converting only the first element)

#list to str:
my_list = ['a', 'b', 'c']
print(str(my_list))  # TypeError

#list to bool:
a = bool([1, 2, 3])
print(a) # Output: True
b = bool([])
print(b) # Output: False

#list to list:
my_list = [1, 2, 3]
print(list(my_list))  # Output: [1, 2, 3]

#list to tuple:
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

#list to set:
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

#list to dict:
my_list = ['1','2','44']
print(dict(my_list)) # TypeError

list to range:
my_list = [0, 5]
print(range(my_list)) # TypeError


#tuple conversions:

#tuple to int:
my_tuple = (1, 2, 3)
print(int(my_tuple[0])) # Output: 1 (converting only the first element)

#tuple to float:
my_tuple = (1.1, 2.2, 3.3)
float(my_tuple[0]) # Output: 1.1 (converting the first element)

#tuple to str:
my_tuple = ('a', 'b', 'c')
print(str(my_tuple)) # Output: ('a', 'b', 'c')

#tuple to bool:
printbool((1, 2, 3))) # Output: True
print(bool(())) # Output: False

#tuple to list:
print(list((1, 2, 3)))  # Output: [1, 2, 3]

#tuple to tuple:
my_tuple = (1, 2, 3)
print(tuple(my_tuple))  # Output: (1, 2, 3)

#tuple to set:
print(set((1, 2, 2, 3)))  # Output: {1, 2, 3}

#tuple to dict:
my_tuple = (1, 2, 3)
print(dict(my_tuple))  # TypeError

#tuple to range:
my_tuple = (0, 5)
print(range(my_tuple))  # TypeError


#set conversions:

#set to int:
my_set = {1, 2, 3}
print(int(list(my_set)[0]))  # Output: 1 (converting only the first element)

#set to float:
my_set = {1.1, 2.2, 3.3}
print(float(list(my_set)[0]))  # Output: 1.1 (converting only the first element)

#set to str:
my_set = {'a', 'b', 'c'}
print(str(my_set))  # TypeError

#set to bool:
print(bool({1, 2, 3}))  # Output: True
print(bool(set()))      # Output: False

#set to list:
print(list({1, 2, 3}))  # Output: [1, 2, 3] (order is not guaranteed)

#set to tuple
print(tuple({1, 2, 3}))  # Output: (1, 2, 3) (order is not guaranteed)

#set to set:
my_set = {1, 2, 3}
print(set(my_set))  # Output: {1, 2, 3}

#set to dict:
my_set = {'1','2', '3'}
print(dict(my_set)) # TypeError

#set to range:
my_set = {0, 5}
print(range(my_set)) # TypeError


dict conversions:
#dict to int:
my_dict = {'a': 1, 'b': 2}
print(int(my_dict['a'])) # Output: 1 (converting only a value)

#dict to float:
my_dict = {'a': 1.1, 'b': 2.2}
print(float(my_dict['a'])) # Output: 1.1 (converting a value)

#dict to str:
my_dict = {'a': 1, 'b': 2}
print(str(my_dict)) # Output: "{'a': 1, 'b': 2}"

#dict to bool:
print(bool({'a': 1})) # Output: True
print(bool({})) # Output: False

#dict to list:
print(list({'a': 1, 'b': 2}))  # Output: ['a', 'b']

#dict to tuple:
print(tuple({'a': 1, 'b': 2}))  # Output: ('a', 'b')

#dict to set
print(set({'a': 1, 'b': 2}))  # Output: {'a', 'b'}

#dict to dict:
my_dict = {'a': 1, 'b': 2}
print(dict(my_dict))  # Output: {'a': 1, 'b': 2}

#dict to range:
my_dict = {'a': 0, 'b': 5}
print(range(my_dict))  # TypeError


#range conversions:

prinrange to int:
my_range = range(1, 5)
int(list(my_range)[0]) # Output: 1 (converting the first element)

#range to float:
my_range = range(1, 5)
float(list(my_range)[0]) # Output: 1.0 (converting the first element)

#range to str:
my_range = range(1, 5)
print(str(list(my_range))) # Output: [1, 2, 3, 4]

#range to bool: 
print(bool(range(1, 5))) # Output: True
print(bool(range(0))) # Output: False

#range to list:
print(list(range(1, 5))) # Output: [1, 2, 3, 4]

#range to tuple:
print(tuple(range(1, 5))) # Output: (1, 2, 3, 4)

#range to set:
print(set(range(1, 5))) # Output: {1, 2, 3, 4}

 #range to dict:
my_range = range(1, 5)
print(dict(my_range))# TypeError

#range to range:
my_range = range(1, 5)
print(range(my_range))  #TypeError




