#ask user their name and age, and print greeting
"""
name= input("enter you name: ")
age = input("enter your age: ")
print("hello", name, "!! aged", age)
"""

#data identification

"""
value = input("Enter a value: ")
try:
    value = int(value)
except:
    try:
      value = float(value)
    except:
      value = str(value)
print(type(value))
"""

#list
"""
list_of_elements=[]

size=int(input("enter the size of list:"))

for i in range(size):
    element= input("enter an element in the list:")
    list_of_elements.append(element)  #modifying tuple

s2 = [s.upper() for s in list_of_elements]
print("printing the list in all upper case", s2)

remove_element= input("enter the element you want to remove:")
list_of_elements.remove(remove_element)

s2 = [s.upper() for s in list_of_elements]
print("after removing the speciifed element, the list will be:", s2)
"""

#unpacking tuples
"""
fruits = {"apple","mango"} #making tuple
(red,yellow)=fruits #unpacking tuple

print(red)
print(yellow)
"""

#dictionary 

"""
dict1 = {"x1": 'A', "x2": 'A+', "x3": 'B', "x4": 'B+', "x5": 'B-'}
print(dict1)
"""

#taking 2 lists as inputs and converting them into list and perform operations
"""
list1=[]
list2=[]
size=int(input('enter the number of elements:'))

for i in range(size):
    element=input(f"enter element {i+1} for list 1:")
    list1.append(element)

print('List 1:',list1)

for i in range(size):
    element2=input(f"enter element {i+1} for list 2: ")
    list2.append(element2)

print('List 2:',list2)

#converting the lists to sets
set1= set(list1)
set2= set(list2)

#printing union
print("the union of the two sets is", set1.union(set2))

#printing intersection
print("the intersection of the two sets is", set1.intersection(set2))

#printing difference
print("the difference of the two sets is", set1.difference(set2))
"""

#number checker
"""
number= int(input("please enter a number: "))
if number>0:
    if number%2==0:
     print("number is positive AND an even number")
    else:
       print("number is a positive and odd number")
elif number<0:
    if number%2==0:
        print("number is negative AND an even number")
    else:
       print("number is negative AND odd")
else:
    print("number is zero.")
"""

#printing 1 to 50 (fizzbuzz)
"""

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
"""
#calculating factorial
"""
number= int(input("enter a number for factorial:"))
fact=1
for i in range(1,number+1):
    fact = fact *i

print("the factorial is", fact)
"""   
#checking prime number
"""
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("enter a number: "))
print("prime" if prime(n) else "not prime")
"""


#returning the squares of a list
"""
def squares(list1):
	return [ n*n for n in list1]

#making a list and passing it to the def
list1=[]
size=int(input("enter the size: "))

for i in range(size):
    element=int(input(f"enter number {i+1}: "))
    list1.append(element)

    new_list=squares(list1)
print(new_list)
"""
#removing duplicates
"""
def remove_dup(l1):
    print(list(dict.fromkeys(l1))) 


list1=[]
size=int(input("enter the size: "))

for i in range(size):
    element=int(input(f"enter number {i+1}: "))
    list1.append(element)

    #calling function
remove_dup(list1) """

#checking palindrome using lambda function
"""
palindrome = lambda s : s == s[::-1]
palindrome("anna")

"""

#fibonacci Sequence Generator 
"""
def fib_seq(n):
    a,b= 0,1
    for i in range(n):
        print(b)
        a,b = b,a+b
        
size = int(input("enter range="))
fib_seq(size) """
#average calculator
"""
numbers=[]
size= int(input("enter the size of the list you want to create:"))
for i in range(size):
    data=int(input("enter a number: "))
    numbers.append(data)

print("the entered numbers are:",numbers)

total_sum=0
for number in numbers:
    total_sum += number

avg= total_sum/size
print("the average is", avg)
"""

#merging dictionaries
"""

dict1= {"a":10, "b":20}
dict2= {"b":90, "c":65}

merged_dict= dict1 | dict2
print(merged_dict)
"""
#nested loops: multiplication table
"""
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, space=" ")
    print()  
"""

#user registration system
"""
#taking credentials
username=input("enter your username: ")
password= input("enter your password: ")

registration_dict={}
registration_dict[username]=password
print("registration successful!! \n ")

#matching credentials for login
match_name=input("enter your username: ")
match_pass=input("enter your password:")

if match_name in registration_dict and registration_dict[match_name]==match_pass:
    print("login successful!!")
else:
    print("login failed :( \nusername or password did not match")

"""
#counting elements in a dictionary
"""
dict={"a":1,"b":10,"c":15,"d":20}
count=len(dict)
print(count)
"""
#temperature converter
"""

choice=int(input("press '1' to convert temp from Celsius to Fahrenheit, else press '2' to convert temp from Fahrenheit to Celsius:" ))
temp = float(input("Please enter the temperature: "))

if choice == 1:
    print("Fahrenheit:", (temp * 9/5) + 32)
elif choice==2:
      print("Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid choice")
"""