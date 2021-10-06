import os 
os.system("cls" if os.name == "nt" else "clear")

def printtype(data):
    for i in data:
        print(i, type(i))

test =[123, "Barry", [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x,{
    "name": "henry", "age": 38
}]

# printtype(test)

# Definig Classes

class Person:
    name = "Barry"
    age = 44

person1 = Person()
person2 = Person()

print(person1.name)
print(person2.name)


Person.job = "teacher"

print(person1.job)
print(person2.job)

#  Class Attributes ve instance attributes

Person.name ="Rafe"
person1.name ="Henry"
print(person1.name)
print(person2.name)