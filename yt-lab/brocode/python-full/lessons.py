#Python lessons

#Intro

#print("I love pizza, it's my favorite food")

#Variables

#variable = a container for a value. Behaves as the value that it contains

#first_name = "Asaf"
#last_name = "Looper"
#full_name = first_name + " " + last_name
#print(type(name))
#print("Hello "+full_name+"!!")

#age = 26
#age += 1
#print("Your age is: "+str(age))
#print(type(age))

#height = 1.85
#weight = 75
#bmi = weight / height**2
#print("Your BMI is: "+str(bmi))
#print(type(height))

#human = False
#print(human)
#print("Are you a human: "+str(human))
#print(type(human))

#Multiple variables

#multiple assignment = allows us to assign multiple variables at the same time in one line of code

#name = "Bro"
#age = 21
#attractive = True
#print(name)
#print(age)
#print(attractive)

#name, age, attractive = "Bro", 21, True
#print(name, age, attractive)

#SpongeBob = Patrick = Sandy = Squidward = 30
#print(SpongeBob, Patrick, Sandy, Squidward)

#String methods

#name = "asaf"

#print(name)
#print(len(name))
#print(name.find("a"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("a"))
#print(name.replace("a", "e"))
#print(name*3)

#Lists

#names = ["Asaf", "Bro", "Patrick", "SpongeBob", "Sandy"]
#print(names)
#print(names[1])
#print(names[-1])
#print(names[0:3])

#Type casting = convert the data type of a value to another data type.

#x = 1 #int
#y = 2.0 #float
#z = "3" #str

#print("x is "+str(x))
#print("y is "+str(y))
#print("z is "+str(z*3))

#x = str(x)
#y = str(y)
#z = str(z)

#print(x)
#print(y)
#print(z)

#user imput

#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+" cm tall")

#math functions

#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(430))
#print(max(x,y,z))
#print(min(x,y,z))


# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

#name = "Bro Code"

#first_name = name[0:3]
#last_name = name[4:9]
#funky_name = name[0:9:3]
#reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8,12)
print(website2[slice])

# if statement = a block of code that will execute if a condition is true

age = int(input("What is your age?: "))

if age == 100:  
    print("You are a century old!")
elif age > 100:  
    print("You are immortal?")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")












