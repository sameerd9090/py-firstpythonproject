import math

print("Hello World!...")
name = "Sameer"
age = 10
print("my name is "+name)
print (age)

age = 24.0
print(age)

is_adult = True
print(is_adult)

#name = input("Who is your favourite superhero?")
#print(name+" is my favourite superhero")

#old_age = input("enter your old age : ")
#new_age =int(old_age)+2
#print(new_age)

number = 10
print(float(number))

#first = input("enter first number : ")
#second = input("enter second number : ")
#print(first+second)

name = "rony starl"
print(name.lower())
print(name.find('rony'))
print(name.replace("rony","iron"))

print("m" in name) #will return true or false
print("star" in name)

print(5/2)
print(5//2) #won't print numbers after decimal
print(5%5)
print(7 ** 2) #power operator
i=2
i+=6
print(i)

#arithmetic precedence
print(2+3//3)

#comparative operator
print(3<2)
print(3==3)
print(3!=3)

#Logical operator
print(2>3 or 2>1)
print(5>2 and 3>1)
print(not 2>3)

#Conditional operators
age = 45
if age < 20:
    print("You are an adult")
elif age > 30 and age <50:
    print("you are not young")
else :
    print("you are going to die")

#Build a calculator
first=input("enter first number : ")
operator = input("enter operator (+, -, *, /) : ")
second = input("enter second number : ")
first = int(first)
second = int(second)
if operator == "*":
    print(first*second)
elif operator == "-":
    print(first-second)
elif operator == "+":
    print(first+second)
elif operator == "/":
    print(first/second)
else:print("this is an invalid operation")

print(range(5))

print(1)
print(2)
print(3)
print(4)
print(5)

i=1
while i < 5 :
    print(i*"*")
    i+=1

for a in range(5):
    print(a)

marks=[1,2,3,4,5,7,8,8]
print(marks[-1])
marks.append(34)
marks.insert(0,99)

print(marks[0:2])

for score in marks:
    print(score)

print(99 in marks) #checks if element exists in list
print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i += 2

marks.clear() #empty the list
print(marks)

students = ["ram", "shyam" ,"radhika", "kishan"]
for student in students:
    if student == "radhika":
        break
    print(student) #wont print after shyam.

for student in students:
    if student =="shyam":
        continue  #skips the shyam
    print(student)

#Tuple
marks = (23,45,32,32,32)
print(marks.count(32))
print(marks.index(32))
people = "first", "second", "third", "fourth"
print(people)


#[] -> list
#() -> Tuple
#{} -> Set
#Set
Scores = {2,4,6,34,34,5,43,23}
print(Scores)
#Set doesn't have indexes, therefore they are called unordered.
#dictionary is like map in java, always in key and values.{key:value}
for score in Scores:
    print(score)

marks={"maths":99, "science":23, "marathi":45}
print(marks["marathi"])
print(marks["science"])
#we can change the existing marks
marks["marathi"]=00
print(marks)

#there are three types of functions
#1. In-Built functions
#2. Module functions
#3. User defined functions
#math is a module functions
from math import sqrt
print(int(sqrt(89)))

print(int(math.sqrt(90)))

#user defined function
#def function_name (parameters):

def print_sum(first,second):
    print(first+second)

print_sum(2,5)

