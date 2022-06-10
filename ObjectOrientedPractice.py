# This is to practice object oriented programming in Python
# Source of practice video is: https://www.youtube.com/watch?v=JeznW_7DlB0
# June 10, 2022

def hello():
    print("Hello")

print(type(hello))  # This returns the type 'function'

string = "hello"
print(string.upper()) # Method upper acting on object of type string

# Now to create our own class
class Dog:  # Blueprint for any type of dog
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        self.age = self.age * 13    # Just did this to see if I can change age in method
        return self.age

    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1

    def set_age(self, age):
        self.age = age

d = Dog("Matt", 5)
print(d.name)
print(d.get_name()) # Both this and the previous command can get the name, but in different ways
print(d.get_age())
d.set_age(40)
print(d.get_age())
d.bark()
print(d.add_one(20))
print(type(d))

# Ultimately, we create classes or use OOP since we can use this blueprint for a large number of specific instances, rather than creating each variable in a list or whatnot, which becomes a pain in the ass

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []     # Notice that we created the attribute students for our list of students and it is empty. This is common and perfectly fine.
        
    def add_student(self, student): # Student parameter is the Student object that we created earlier
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Matt", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("CS101", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students) # This returns "[<__main__.Student object at 0x00000153A27B3C10>, <__main__.Student object at 0x00000153A27B3BB0>]". Let us try to be more specific.
print(course.students[0].name)
print(course.get_average_grade())

print(course.add_student(s3)) # Notice that since our max capacity is 2, we cannot add s3



# Now we get into inheritance 

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Bark")

# Now notice for these two methods they are very similar, both take in name and age. But instead of initializing init for each, why can't they just inherit those two parameters from an upper class?
# Let us try that

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

# Now what can we make Dog and Cat look like?

class Cat(Pet):
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bark")

# Now Cat and Dog inherit from the Pet class the name and age. 

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.show()    # Notice how even though we don't put Bill into the Pet class, we can still use the show function. That is because Cat inherits the Pet class along with its functions.

# What about if we want our child classes (Cat and Dog)  to be able to take in specific parameters? Like what if we wanted the color of our cat?
# Would this mean we would have to rewrite our Pet class? No, we could just rewrite our Cat class.

class Cat(Pet):
    def __init__(self, name, age, color):   # Notice that we initialize by taking in the previous parameters, but we add color as well.
        super().__init__(name, age)
        self.color = color # Also notice that we don't reinitialize the name and age parameters. Doing so is not necessary.

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} colored.")

c = Cat("Bill", 34, "Brown")
c.show()



# Now we will try class specific instances instead of object specific instances
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        

p1 = Person("Tim")
p2 = Person("Jill")

# number_of_people is class specific, meaning that right now, regardless of p1 or p2, the number_of_people is still 0.
# We can change that through this way:

Person.number_of_people = 8
print(p2.number_of_people)

# By adding "Person.number_of_people += 1" in our __init__ function, this increments the number of people by each person we initialize

# But what about if we wanted to do this through a class method? They are a bit different than regular methods

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod    # This is not specific to an instance, rather it acts on the class itself
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())



# Now we have static methods
class Math:
    @staticmethod # This mean that this method does not change anything
    def add5(x):
        return x + 5

print(Math.add5(5))

# The point of this is to not have to create an instance and all of that (and organization of our code). We can just call the function