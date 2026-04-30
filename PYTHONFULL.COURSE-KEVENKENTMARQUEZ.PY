print("Hello, World!")

name = "Kevin kent Marquez"
age = 19
floating = 3.14
is_new = True

# input.
name = input('What is Your name:')
favorite_color = input('What is your favorite color:' )
print(name + 'liked' + favorite_color)

# Typecasting Converting value to a String to integers etc
birth_year = input('Birthyear: ')
print(type(birth_year)) # String
age = 2025 - int(birth_year)
print(type(age)) # Integer
print(age)

# Converting Kg to lbs
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
#single of Double Quote
course = 'BSIT "Course"'
print(course)
# Triple Quote

BSIT = '''

PYTHON
C++
C 
RUBY
JAVA
JAVASCRIPT

'''

print(BSIT)

Course = ('BSIT')
print(Course[0]) # Indexing
print(Course[-2]) # Negative comes from End 
print(Course[0:3]) # Slicing

#formating String

first = 'kevin'
last = 'smith'
output = f'{first} [{last}] is a coder'
print(output)

#Strings methods

course = "BSIT"
print(len(course)) # len()count a number of a string
course.upper() # uppercase
course.lower() # Lowercase
course.find('B') # Finding 
course.replace('BSIT', 'BSCE')) # Replace
course.Title() # Capitalize Characters
print('BSIT' in course) # Checking

#Math Function

x = 2.9
print(round(x)) # Rounding absolute value
print(abs(-2.9)) # Possitive Results 2.9

#math modules 
import math

print(math.ceil(2.9))
print(math.floor(2.9))

# if statement

is_hot = True
is_cold = False

if is_hot:
    print("It's a Hot Day") 
    print("Drink Plenty Of Water")
elif is_cold:
    print("It's a Cold Day")
    print("Wear Warm Clothes")
else:
    print("It's a Lovely Day")
    print("Wear Warm Clothes")
print("Enjoy Your Day") # False Value

#Sample
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment : ${down_payment}")

#Logical Operator
has_high_income = True
has_good_credit = True

if has_high_income and had_good_credit: # Combine
    print("Eligible For loan")
if has_high_income or had_good_credit: # Combine
    print("Eligible For loan")

# comparison
if temperature > 30:
    print("Its a Hot Day")
else:
    print("Its not a Hot Day")

name = 'keven'

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name Must be A Maximum of 50 Characters")
else:
    print("Name looks Good")
    
#Project : Weight Converter

weight = int(input('Weight : '))
unit = input = ('(L) lbs or (K)kg: ')

if unit.upper == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


#while Loops

i = 1
while i<= 5:
    print(i)
    i = i + 1
print("Done") #Stopping Loop

i = 1
while i<= 5:
    print('*' * i)
    i = i + 1
print("Done")

#While Loop Guessing Game

secret_number = 24
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("Sorry You Failed")
    
# Example Game Car

command = ""
started = False
while command.lower != "quit":
    command = input(">: ").lower()
    if command == "start":
        if started:
            print("Car is already Started")
        else:
            started = True
            print('Car Started ...')
    elif command == "Stop":
        if not started:
            print("Car is Already Stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
    Start - Start the Car
    stop - Stop the Car
    quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I Dont Understand That")
        
# For Loops
for item in 'Python':
    print(item)
for item in ['Kevin', 'Steven', 'Gian']:
    print(item)
# Range
for item in range(10): 
    print(item)

# Example
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total" : {Total}")

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
        
# Sample
numbers = [5, 2, 5 , 2, 2]
for x in numbers:
    print('x' * x ) # cheat

numbers = [5, 2, 5 , 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#Lists
names = ['Kevin','Mark', 'Ash', 'joy']
print(name[0]) #kevin
print(name(0:3)) # Slicing
names[0] = 'Jon'  #Change

#Example
numbers = [3 ,6 ,8 ,2 ,4 ,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D List
matrix = [
     [1, 2 ,3],
     [4, 5, 6],
     [7, 8, 9]
]
matrix[0][2]
matrix[0][2] = 20
print(matrix[0][2])

#Loops
matrix = [
     [1, 2 ,3],
     [4, 5, 6],
     [7, 8, 9]
]
for row in matrix:
    for items in row:
        print(items)

#Lists Method
numbers = [4, 4, 9, 3, 10, 20]
numbers2 = numbers.copy()
numbers.append(100) #2nd doesnt copy that you append
numbers.append(30) #add
numbers.insert(0, 25) # add based index
numbers.remove(20) #remove item
numbers.clear() #remove all from the list
numbers.pop() #remove the last number from lists
print(numbers.index(4)) # Result 0 index 4 = 0
print(numbers)
print(50 in numbers) # False
print(numbers.count(4)) #2 double 4
numbers.sort()
numbers.reverse() #Reverse The numbers in lists
print(numbers) #All numbers in lists

#Example removing duplicates number
numbers = [2, 2, 2, 4, 5, 6, 9, 10]
uniques = []
for number in numbers:
    if number not in uniques:
        numbers.append()
print(uniques)

#Tuple is Immutable 
# You can't add or remove 
numbers = (1, 2, 3)
print(numbers[0])

#Unpacking
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x,y,z = coordinates #shorcut from duplicates coordinates
print(x) # 1
print(y) # 2
print(z) # 3

#Dictionaries
customers = {
    "name" : "Kevin Kent Marquez",
    "Age" : 19,
    "is_verified" : True
}
print(customers["name"])
print(customers.get("names")) #None
print(customers.get("names","January 24")) #instead of none
customers["name"] = "Ken"
print(customers["names"])
customers["Birthdate"] = "Feb 21"
print(customers["Birthdate"]) # add new key  value pair

#Example
phone = input("Phone:" )
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)

#Emoji Converter
message = input("Enter: ")
words = message.split(' ')

emojis = {
    ":)" : "😀",7
    ":(" : "‎😔"
}
output = ' '
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#Functions
#Always add two line indented in Function
#if Function Doesn't call fucntion can't print
#Define Function first before call
def greet_user():
    print("Hello there!)
    print("Welcome To Python")


print("Start")
greet_user()
print("Finish")

#Parameters
#inside of parentheses you can add
# parameters / placeholder 
# for receiving information
def greet_user(name):
    print(f'Hi {name}')
    print('Welcome to Python')
    
    
print("Start")
greet_user("Keven")
greet_user("Python")
print("Finish")
#Arguments 
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome to Python')
    
    
print("Start")
greet_user("Keven", "Marquez")
print("Finish")

#keyword arguments
#Dito kahit hindi order
#mauuna yung na call na first_name
#para Readable yung Code
#positional Argument before The keyword
#argument
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome to Python')
    
    
print("Start")
greet_user(last_name="Marquez", first_name="Keven")
cal_cost(total=50, shipping=40, discount=0.50)
print("Finish")

#Return Statement
def square(number):
    return number * number #That is the square of number
#Best Optio     
print(square(5))
#2nd Option
result = square(5)
print(result)

#Creating Reusable Function
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
    ":)" : "‎😀",
    ":(" : "😔"
    }
    output = ""
    for word in words:
          output += emojis.get(word, word) + " "
    return output


message = input(">: ")
print(emoji_converter(message))

#Exceptions 
#Handling Error
try:
    age = int(input("Enter: "))
    print(age)
except ValueError:
    print("invalid Value")
#Another Example
try:
    age = int(input("Enter: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError: # Zero can not divide
    print("Ca Define")  #We Use Except Division Error
except ValueError:
    print("invalid Value")

#Classes
class Point:
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
point2.y = 20
print(point1.x)
point1.draw() #Print Draw itself

point2 = point() #Point 2 is different from point 1
point2.x = 1
print(point2.x)

#Constructor
class Point:
    def init(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')
point1 = Point(10, 20)
point.x = 11 # you can change value
print(point.x)

#Example Class Constructor
class Person:
    def init(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi I Am, {self.name}") 
        #when Add this remove line print


john = Person("Kevin")
print(john.name) # this will be remove after formating
john.talk

bob = Person("Joy")
bob.talk()

#inheritance
class Mamal:
    def walk.(self):
        print("Walk")


class Dog(Mamal):
    pass #to avoid empty
    def bark(self):
        print("Bark") #add New Class method


class Cat(Mamal):
    def be_annoying(self):
        print("Annoying")


dog = Dog()
dog.walk()

cat1 = Cat()
cat1.be_annoying
cat1.walk

#Modules in Python
import converters #Whole Modules
from converters import kg_to_lbs #Specific modules

kg_to_lbs(53)

converters. #to access
print(converters.kg_to_lbs(70))

#Examlple
#Name in Utils
def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

#In other modules
from Utils import find_max()

numbers = [10 , 20, 50, 200, 400]
maximum = find_max(numbers) #to avoid dupe
print(max) #result 10

#Generate Random Module
import Random

for i in range(3):
    print(random.randint(10, 20))
    print(random.random(10, 20))

#Example 2
import Random

members["Kevin", "Joy", "Mark", "Ash"]
leader = random.choice(members)
print(leader)

total = 0
inputs = []

while True:
    user_input = input("Enter a number (or 'stop' to quit): ") # Corrected to use input() function
    if user_input.lower() == "stop":
        print("\nYou typed 'stop'. The program is ending!")
        break

    try:
        number = int(user_input)
        inputs.append(number)
        if number == 0:
            total = 0
            print("You entered 0 — total has been RESET to 0.\n")
        elif number % 2 == 0:
            total += number
            print(f"{number} is EVEN → Added. Running total:{total}\n")
        else:
            total -= number
            print(f"{number} is ODD → Subtracted. Running total: {total}\n")
    except ValueError:
        print("That's not a valid number. Please try again.\n")

print("\n--- Summary of all numbers you entered ---")

if len(inputs) == 0:
    print("You didn't enter any numbers.")
else:
    for num in inputs:
        if num == 0:
            print(f" {num} → Reset the total")
        elif num % 2 == 0:
            print(f" {num} → Even (was added)")
        else: # Added an else block for odd numbers in the summary
            print(f" {num} → Odd (was subtracted)")

print(f"\nFinal Total: {total}")
print("Thanks for using the program!")

#2nd 
my_list = []

for i in range(1, 10):
    my_list.append(i)

print("Original list:", my_list)
print("Length of list:", len(my_list))

y = 1
x = 0
while x < len(my_list):
    if my_list.count(my_list[x]) > 1:
        del my_list[x]
    else:
        y = y + 1
        x += 1

print("\nThe list with unique elements only.")
print(my_list)

#3rd

class Toggle:
   def __init__(self):
      self.active = False
   
   def switch(self):
      self.active = not self.active
      if self.active:
         print("Status: ACTIVE")
      else:
         print("Status: INACTIVE")

t = Toggle()
t.switch()
t.switch()
t.switch()
t.switch()


#4th

class TimesTable:
    def generate(self):
        number = int(input("Enter a number: "))
        limit = int(input("Enter the limit: "))

        for i in range(1, limit + 1):
            print(str(number) + " x " + str(i) + " = " + str(number *i))

tt = TimesTable()
tt.generate()

#5th

class GradeBook:
    def get_grade(self):
        score = int(input("Enter your score: "))
        if score >= 90:
            print("Your grade is: A")
        elif score >= 80:
            print("Your grade is: B")
        elif score >= 70:
            print("Your grade is: C")
        elif score >= 60:
            print("Your grade is: D")
        else:
            print("Your grade is: F")

gb = GradeBook()
gb.get_grade()

#6th

class Repeater:
    def repeat(self):
        word = input("Enter a word: ")
        count = int(input("How many times? "))
 
        for i in range(count):
            print(word)

rep = Repeater()
rep.repeat()

#7th

class MindReader:
   def play(self):
      secret = 42
      found = False
      while not found:
        guess = int(input("Guess the number: "))
        if guess < secret:
          print("Too low! Try higher.")
        elif guess > secret:
          print("Too high! Try lower.")
        else:
            found = True
            print("Amazing! You read my mind!")
      
mr = MindReader()
mr.play()

#8th

class WeatherCheck:
    def check_temp(self):
        temp = int(input("Enter the temperature in Celsius: "))
        if temp <= 0:
            print("It is freezing! Wear a coat.")
        else:
            print("The weather is fine.")

w = WeatherCheck()
w.check_temp()

#9th

class Profile:
    def introduce(self):
        name = input("What is your name? ")
        age = input("How old are you? ")
        color = input("What is your favorite color? ")
        print("Hi! My name is " + name + ", I am " + age + " years old, and I love the color" + color + ".")

p = Profile()
p.introduce()

reviewer = """
( “ “, ‘ ‘) - Single and Double Quotation called a string to
call out the variable.
( +,-,*,/) – Mathematical/ Arithmetic Operation use for
any mathematical problem to your code.
( + ) Sum – Used to add a two whole number.
(-) Difference – Used to subtract two whole number.
( * ) Product – Used to multiply two whole number.
( / ) Quotient – Used to divide two whole number.
( =
, += , - = ,/ =
,
* = ) – Assignment Operation use to
store and update variables values.
( { }, + ) – Curly Bracket and Plus Sign is use for adding
a string and variable.
( [ ] ) – List Function is used to save a list of string of
variable.
( < , >, >=, <=, = =, != ) – Comparison Operation/ Logical
Operation use to compare values and return True / False
for your logical pattern.
( : ) Colon – Used to closed the header of function
( ) Parenthesis – Used for input values or variables.
(input) Input Function – Used to communicate to a user
what to input on the open ended question
(int) Integer Function – Used to set of whole number on
a program.
(str ) String Function – Used to represent a set of
variable as text rather than a number.
(bool) Boolean Function – is a data type that represent a
two values of True or False.
( % ) Modulo Operator – return the remainder of a
division operation between two numbers, it is also to
represent a EVEN & ODD numbers.
print() Print Function – Used to send or show the output
of a variable.
( def ) or Define Function – Short for define used to
create or declare a function.
(return) Return Function – Used to send a result back to
the caller or def.
(continue) Continue Function – Used to skips the
current iteration and jumps to the next one.
( for ) Loop – Used for definite iteration or repeats a set
number of times.
(while) Loop – Used for indefinite iteration or repeats as
long as a specified condition remains True.
(range) Function – Used to set a number range on for
loop.
(.upper) Uppercase Function – Used to set the variables
into a uppercase letter.
(.lower) Lowercase Function – Used to set the variables
into a lowercase letter.
( count ) Count Function – Used to set a count of a
integers.
( if, elif, and else) Conditional Statements – Used for
decision making and controlling program flow.
( if ) Statement – If only one condition is true.
(elif) Statement – Used to check additional conditions or
another conditions.
(else) Statement – Used to catch all block of condition
that execute only if all preceding if and elif conditions
were false.
( <class> ) Function – Used to called out a type function
if it is class string or class boolean.
( class variable: ) Class Function – Used to called the
class variable on a program.
(variable_variable) Class Boolean – Used to call a
Boolean class.
(.append) Function – Is used to save an existing list.




"""


#___________Number Ones____________
def ones(x):
    if x == 0:
        return ""
    elif x == 1:
        return "One"
    elif x == 2:
        return "Two"
    elif x == 3:
        return "Three"
    elif x == 4:
        return "Four"
    elif x == 5:
        return "Five"
    elif x == 6:
        return "Six"
    elif x == 7:
        return "Seven"
    elif x == 8:
        return "Eight"
    elif x == 9:
        return "Nine"

#___________Number Tens____________
def tens(x):
    if x == 10:
        return "Ten"
    elif x == 11:
        return "Eleven"
    elif x == 12:
        return "Twelve"
    elif x == 13:
        return "Thirteen"
    elif x == 14:
        return "Fourteen"
    elif x == 15:
        return "Fifteen"
    elif x == 16:
        return "Sixteen"
    elif x == 17:
        return "Seventeen"
    elif x == 18:
        return "Eighteen"
    elif x == 19:
        return "Nineteen"
    elif x >= 20:
        if x // 10 == 2:
            return "Twenty"
        elif x // 10 == 3:
            return "Thirty"
        elif x // 10 == 4:
            return "Forty"
        elif x // 10 == 5:
            return "Fifty"
        elif x // 10 == 6:
            return "Sixty"
        elif x // 10 == 7:
            return "Seventy"
        elif x // 10 == 8:
            return "Eighty"
        elif x // 10 == 9:
            return "Ninety"

#___________Number Hundreds____________
def hundreds(x):
    return ones(x) + " Hundred"

#___________Number Thousands____________
def thousands(x):
    return ones(x) + " Thousand"


num = int(input("Enter a number: "))

if num == 0:
    print("Zero")

elif num < 10:
    print(ones(num))

elif num < 20:
    print(tens(num))

elif num < 100:
    print(tens(num) + " " + ones(num % 10))

elif num < 1000:
    if num % 100 == 0:
        print(hundreds(num // 100))
    elif num % 100 < 20:
        print(hundreds(num // 100) + " " + tens(num % 100))
    else:
        print(hundreds(num // 100) + " " + tens(num % 100) + " " + ones(num % 10))

elif num < 10000:
    if num % 1000 == 0:
        print(thousands(num // 1000))
    elif num % 1000 < 10:
        print(thousands(num // 1000) + " " + ones(num % 1000))
    elif num % 1000 < 20:
        print(thousands(num // 1000) + " " + tens(num % 1000))
    elif num % 1000 < 100:
        print(thousands(num // 1000) + " " + tens(num % 1000) + " " + ones(num % 10))
    elif num % 100 == 0:
        print(thousands(num // 1000) + " " + hundreds((num % 1000) // 100))
    elif num % 100 < 20:
        print(thousands(num // 1000) + " " + hundreds((num % 1000) // 100) + " " + tens(num % 100))
    else:
        print(thousands(num // 1000) + " " + hundreds((num % 1000) // 100) + " " + tens(num % 100) + " " + ones(num % 10))


total = 0
inputs = [] 

while True: # loop condition while = True
    user_input = input("Enter a number (or type 'stop' to end): ") # user enter a either number, 0 reset the total and stop to stop the program
    if user_input.lower() == "stop": # if user enter stop program will stop
        break

    try:
        number = int(user_input) # use in because its whole number
        if number == 0: # first if in try if number equal siya sa zero mag rereset siya in total is zero (0)
            total = 0
            inputs.append(number)
            print(f"{number} is ZERO → Total reset to 0. Running total: {total}") # mag aapend dito if zero nilagay na total is zero in total
        elif number % 2 == 0: # even if user type even numbers
            total += number
            inputs.append(number)
            print(f"{number} is EVEN → Added. Running total: {total}") # and then numbers that user entered will add in total of the numnbers
        else: # else if odd siya mag substract siya ng number sa total numbers bawas if odd numbers add numbers pa add naman and 0 pag ireset ang total
            total -= number
            inputs.append(number)
            print(f"{number} is ODD  → Subtracted. Running total: {total}")

    except ValueError:
        print("Invalid input. Please enter a number or 'stop'.") # invalid input if si user nag entered ng invalid na na type nya sa input will print invalid

print("The Program is ending!")  # program ending pag na type yung stop 
print("Summary of all numbers you entered") # pag na stop na program  will print the total numbers who entered the user

for input in inputs: # dito naman yung after nung program end 
    if input == 0: # i print dito if zero was total reset total
        print(f"{input} → Zero (total was reset)")
    elif input % 2 == 0: # even naman pag even was added  sa total
        print(f"{input} → Even (was added)")
    else: # odd naman pag na print is odd was substract 
        print(f"{input} → Odd (was subtracted)")

print(f"Final Total: {total}") # and finally yung total ng lahat ng na enter ni user  