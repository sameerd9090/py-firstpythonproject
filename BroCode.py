import math
import time

print('Hello World!')
print('sundar mai!')

#variable - for storing the values
#string - series of characters
name = 'sameer'
print("hello " + name)
print(type(name)) #checks the datatype
first_name = "bro "
last_name = "code"
full_name = first_name+last_name
print(full_name)

#int data type
age = 21 #note in double/single quote
age+=1
print(age)
print(type(age)) #checking datatype

age = "21"
#age+=1
print(type(age))
print('your age is '+ str(age)) #this is the typecasting

#float = floating point number (includes decimal portion)
height = 5.9
print(height)
print(type(height))
print("your height is " + str(height) + " feet")

#boolean -> only stores true or false, very useful in if statements
human = False
print(human)
print(type(human))

#multiple assignments -> writing code in single line
name = 'my name'
age = 23
attraction = True

sameer=yashwant=diwse=30
print("age of yashwant is "+ str(yashwant))

print(name)
print(age)
print(attraction)
print(name,age,attraction) #in single line

#string
name = "bro"
print("length : " +str(len(name)))
print(name.find('o'))
print(name.capitalize())
print("upper : " +name.upper())
print(name.isdigit()) #->checks if it contains only digit (boolean)
print(name.isalpha()) #->checks if it contains only alphabet
print(name.count('o'))
print(name.replace("o","a"))
print(name*4)

#typecasting -> changing the datatype value to another datatype
u = 2.0
z = "3"
x = 2
print(float(x))
print(int(u))
print(u)
print(int(z)+2)

#accepting user input in python
#name = input("what is you name :")
print("hello " + name)

#age = int(input("how old are you?"))
age +=1
print("you are "+str(age)+" years of age")

#height = float(input("how tall are you?"))
print("you are "+str(height)+"cm tall")

#Useful functions related to numbers
 #math is a module
pi = 3.14
print(round(pi))
print(math.ceil(pi)) #rounded up
print(math.floor(pi)) #rounded down
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
x=1
y=2
z=3
print(max(x,y,z))
print(min(x,y,z))

#String slicing
name = "bro code"
first_name = name[0:3]
print(first_name)

last_name = name[4:6]
print(name[4:6])
funky_name = name[0:5:2] #it is same as name[::2] but its last index is last index we've not specified it
funky_name = name[::-1] #to reverse the string
print(funky_name)

website = "http://www.google.com"
website2 = "http://www.wikipedia.com"
part = slice(11,-4 ) #this negative is counting from backside.
print(website[part])
print(website2[part])

#if statements -> block of code which will only execute
#                 if the condition mentioned is true.
#age = int(input("how old are you?"))
if age == 100:
    print("you have made to century")
elif age>18:
    print("you are eligible to vote")
elif age < 0:
    print("you are not born yet")
else:
    print("you can't vote")

#logical operators in python(and,or,not) -> used to check if two
#more conditional statements is true.

#temp = int(input("whats the temperature outside?"))
#if not (temp>=0 and temp<=30):
    print("temp is good today")
    print("go outside")
#elif not (temp < 0 or temp > 30):
    # print("the temp is bad today ")
    # print("better to stay inside")

#while loop
#while 1==1:
 #   print("help i'm stuck in a loop")

name = ""
#while len(name)==0:
   # name = input("enter your name")
print("hello "+name)

#for loop
for i in range(10):
    print(i)
for i in range (20,30+1):
    print(i)
for i in "sameer":
    print(i)
for seconds in range(10,0,-1):
    print(seconds)
   # time.sleep(1)
print("happy new year")

for i in range(10,20):
    print(i)

#Nested for loops
#rows = int(input("how many rows?"))
#columns = int(input("how many column?"))
#symbol = input("enter a symbol to use:")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="  ")
#     print()

#Loop Control Statements

#1.Break -> Used to terminate the loop entirely.
#2.Continue -> Skips to the next iteration of the loop.
#3.pass -> Does nothing, acts as a placeholder.

# while True:
#     name = input("Enter your name : ")
#     if name != "":
#         break
# print("hello " + name)

phone_number = "234-567-8977"
for i in phone_number:
    if i == "-":
        continue #It basically skips the character we have specified in double quotes.
    print(i, end='')

for i in range (1,21):
    if i == 13:
        pass
    else:
        print(i)

#Lists in python -> Used to store multiple items in a single variable.
food = ["pizza","water","varan-bhat","vada-pav","misal-pav"]
food[0] = "sushi"
if "pizza" in food: #We can do this with tuple but not
                     #with lists.
    print("it is true")
# print(food[0])
#Few useful functions of List
food.append("ice-cream")
food.remove("water")
food.pop() #Removes the last element.
food.insert(1,"cake")
food.sort() #Sorts in alphabetical order
food.clear() #This will remove all the elements in the list.
for x in food:
    print(x)

#2D lists (multidimensional lists) in python
drinks = ["coffe","soda","tea"]
dinner = ["pizza","burger","hotdogs"]
dessert = ["cake","ice-cream"]

food = [drinks,dinner,dessert]
print(food[2][1])

#Tuples -> collection which are ordered and unchangeable.
student = ("bro",21,"male")
print(student.count("bro"))
print(student.index("male"))
print("sameer")
for i in student:
    print(i)
if "bro" in student:  #Checking if "bro" is in tuple student.
    print("bro is here")

#Set -> Collection which unordered,unindexed and it
  # has no duplicate values.

utensils = {"fork","spoon","knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
dishes = {"bowl","plate","cup","knife"}
#utensils.update(dishes) #To add two sets.We can also
#do reverse. dishes.update(utensils)..
#dinner_table = utensils.union(dishes)

#for i in dinner_table:
 #   print(i)
print(dishes.difference(utensils))#This will print what utensils has which dishes doesn't
print(dishes.intersection(utensils))#common in both

#Dictionary -> A changeable, unordered collection
#of unique key:value pairs. It is fast because
#they use hashing, allow us to access the value
#quickly.

country_capitals = {'USA':'New-York','India':'Delhi','China':'Beijing','Russia':'Moscow'}
# print(country_capitals['USA'])
# print(country_capitals.get('Pak'))
# print(country_capitals.keys())
# print(country_capitals.values())
country_capitals.update({'germany':'berlin'})
print(country_capitals.keys())
country_capitals.update({'USA':'Pakistan'})
country_capitals.pop('China')
country_capitals.clear()
for key,value in country_capitals.items():
    print("hello "+key,value)

#Index operator in python ([])
name = "bro code"
if(name[0].islower()):
   name=name.capitalize()

first_name = name[:3].upper()
last_name = name[-4:].upper()
print(last_name)

#functions -> a block of code which is executed only when called.
def hello(name,age,aage):
    print("hello "+name+" "+age+str(aage)) #We have to cast integer
    #value to the string.

hello('sameer','code',20) #Passing arguments.

#Return statements -> Functions send python values/objects back to
#the caller. These values/objects are known as function's return
#values.

def multiply(number1, number2):
    return number1*number2  #We've done this various times in java.

x=multiply(3,4)
print(x)

#Keyword arguments -> previously we've studied positional arguments
#but now in this position won't matter.

hello(age="diwse",name="sameer",aage=20) #arguments preceded by the
#identifier.

#Nested function calls -> these are nothing but, passing the return
#values as an argument to the outer functions.

# num = input("enter the number.")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)      Instead of doing all this.

#print(round(abs((float(input("Enter the number :")))))) #Nested functions
# name = "bro"  this variable has local scope
def display_name():
    shame = "bro" #This shame variable has local scope.
    print(shame) #name has the local scope.
print("name is : " +name)

#*args -> We can add many more arguments as a pack, no need to specify.
def add_numbers(*nums): #after the asterics(*) we can write any variable name
    sum = 0             #'*' is variable.
    for i in nums:
        sum += i
    print("the sum is : " +str(sum))

add_numbers(1,2,3,4,5,6)

#**kwargs -> parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword
# arguments.
def add_numbers(**kwargs): #kwargs is just a conventional name we can
         # use anything after the double asteriks.
         for i,j in kwargs.items():  #we have to specify key,value
             print(str(kwargs[i]))


add_numbers(first = 2,second =3,third = 4,fourth = 5,fifth = 6)

# str.format() -> another approach to insert values into the string

animal = "dukkar"
item = "house"
# print("the {} ran into the {}".format(animal,item))
# print('the {1} ran into the {0}'.format(item,animal))

print("the {animal} ran into the {animal}".format(animal="cow",item="house"))
name = "akshay"
print("my name is : {}".format(name))
print("my name is : {:^10}".format(name))

number = 315
print("the number pi is {:.2f}".format(number))
print("the number pi is {:,}".format(number))