# Let's remember the name and house of harry potter program
# let's gradually enhance this program by adding more and more features to it to see if we don't stumble upon any problems
# in that probable scenario hope we can introduce oop to deal with or writting even more sophisticated programs down the line
from unicodedata import name


if False:
    name = input('Name: ')
    house = input('House: ')
    print(f'{name} from {house}')
# let's remeber the custom function lessons, which gave us building blocks to expand our code as we proceed
# let's define main() which david affectionately calls world and instead of input() let's define our function as get_name()

if False:
    def main():
        name = get_name()
        house = get_house()
        print(f'{name} from {house}')

    def get_name():
        return input('Name: ')
        # returning means we are connecting the dots between the variables name s from both def main() and def get_name() blocks

    def get_house():
        return input('House: ')
    # it's a good habit in case we want to use it as modules
    if __name__ == "__main__":
        main()

# we can return only one function using sub def blablabla. But we can also return return them through variables and return = x, y . It's better to use name, house as it's more readable
# we could use dictionary, but it will get complicated
if False:
    def main():
        # we can totally unpack the way we are returning the variables [sequences of values that are coming back]
        name, house = get_student()
        print(f'{name} is from {house}')

    def get_student():
        name = input('Name: ')
        house = input('House: ')
        return name, house
        # we are returning two values here so how do we get these returned values?
    # it's a good habit in case we want to use it as modules
    if __name__ == "__main__":
        main()
# what we have just done is used a tuple
# tuple is another type of data, which is comprised of a collection of values, it's similar in spirit to a lise so to speak
# but it's immmutable, for example we can change the values of index (0, ..., n) from a list but touple is simpler than that
# we don't need to use a collection of value as a list, but we can definitely return it as a touple
# We are usually returning one value which is a touple, we can also use parentheses around a touple

# we can totally retrieve the returned touple as student whcih acts like a list[because we can use indexes to specify arguments] but an immutable one
if False:
    def main():
        student = get_student()
        print(f'{student[0]} is from {student[1]}')
    def get_student():
        name = input('Name: ')
        house = input('House: ')
        return (name, house)
    if __name__ == "__main__":
        main()

# When do we use touple instead of lists? When we want to program more defensively
# If we don't wnat to change anything in the dataset why would we use one that allows it, so touple.
# Let's code in a way so that if name == padma, it should automatically be ravenclaw
if False:
    def main():
        student = get_student()
        if student[0] == 'Padma':
            student[1] = 'Ravenclaw'
            # It should give type error as touple objects don't allow item assignment, nondestructive
            # for that we need a list
        # we don't need any else condition
        print(f'{student[0]} is from {student[1]}')
    def get_student():
        name = input('Name: ').lower().capitalize()
        house = input('House: ').lower().capitalize()
        #return name, house
        #return (name, house)
        return [name, house]
        # just adding square braces instead of firsts make it a mutable or reassignable least
    if __name__ == "__main__":
        main()

# Let's revember dictionary, a collection of keys and values. So they have better semantics
if False:
    def main():
        student = get_student()
        print(f"{student['name']} is from {student['house']}")
    def get_student():
        student = {}
        # It's an empty dictionary where we will assign values using input() function
        # it is same as appending into an empty list
        student['name'] = input('Name: ').lower().capitalize()
        student['house'] = input('House: ').lower().capitalize()
        return student
        # just adding square braces instead of firsts make it a mutable or reassignable least
    if __name__ == "__main__":
        main()

# simpler version
if False:
    def main():
        student = get_student()
        print(f"{student['name']} is from {student['house']}")
    def get_student():
        name = input('Name: ').lower().capitalize()
        house = input('House: ').lower().capitalize()
        return {'name': name, 'house': house}
        # just adding square braces instead of firsts make it a mutable or reassignable least
    if __name__ == "__main__":
        main()

# Let's solve that padma issue this way
if False:
    def main():
        student = get_student()
        if student['name'] == 'Padma':
            student['house'] = 'Ravenclaw'
        # we don't need any else condition
        print(f"{student['name']} is from {student['house']}")
    def get_student():
        name = input('Name: ').lower().capitalize()
        house = input('House: ').lower().capitalize()
        return {'name': name, 'house': house}
    if __name__ == "__main__":
        main()
# So dictionaries like lists are mutable

# There are also many more kind of datas assinable to students like patronous, hair color and whatnot
# So far lists, dictionaries and touples are probided by python developers, some general purpose tools
# But they also gave us another type of general purpose tool that would allow us to create a dataset of our own and actually give them name
# They are called classes
# A class is kind of like a blueprint for pieces of data, objects so to speak
# A class is like a mold that we can define, give them a name and when we use the mold we get types of data that are designed exaxctly like we want
# This falls under the object oriented programming

# Let's introduce this new keyword for classes literally called class
# Trust me it is not about students lol, class is a general purpose term in a lot of languages 
# It allows us to define this custom container class for different kind of data
if False:
    class Student:
        # We will get to it later for the implimentation but for now let's use three dots lol. ... is a valid placeholder
        ...
        # here we just created a class Student which we defined with properties on def get_student() block when we assigned Student() function to student variable

    # Let's now go to our custom function get_student() and change it to use the class instead of the dictionary
    def main():
        student = get_student()
        # Inside print functio we are going to pass in student.name instead of student['name']
        # We now have a proper data type that was not provided by python developers but we created it ourselves, so we can use it to create a dataset of our own
        print(f"{student.name} is from {student.house}")

    def get_student():
        # This is where we are defining an object for the class Student
        student = Student()
        # we are assigning a new function which matches the term we wrote after class at the top
        # Now let's asswign name to our class like a dictionary student['name']
        # But the syntax is a little different than the dictionary, the key is called the attributes or properties and we use it with after a dot
        # It is like a methode ut without parentheses and it is in the LHS
        student.name = input('Name: ').lower().capitalize()
        student.house = input('House: ').lower().capitalize()
        # Now exactly as before let's return student
        return student
    if __name__ == "__main__":
        main()
# Class is like a mold and object is like the pluster that we put inside
# Class is the definition of a new data type and object is the incarnation of or more technically instanciation of that data type
# Another definition of object would be instances of classes
# These custom data types are mutable but we can also make them immutable by using the __init__() method and the @property decorator.
# It will happen next in our ... placeholder

# Gemini example
if False:
    # The Blueprint (Class)
    class Car:
        def __init__(self, brand, color):
            self.brand = brand  # Attribute
            self.color = color  # Attribute

    # The Concrete Objects (Instances)
    car1 = Car("Tesla", "Red")    # instance 1
    car2 = Car("Toyota", "Blue")  # instance 2

    print(car1.brand)  # Outputs: Tesla
    print(car2.color)  # Outputs: Blue

if False:
    class Student:
        # In the context of classes there are also a number of methods that are built into the class, they are called dunder methods because they have double underscores before and after their names
        # The __init__() method is a special method that is automatically called when a new instance of the class is created, it is used to initialize the attributes of the class
        # The self parameter is a reference to the current instance of the class, it is used to access the attributes and methods of the class, it is similar to the this keyword in other programming languages
        # init means initialize, it is a constructor method that is called when a new instance of the class is created, it is used to initialize the attributes of the class    
        # We dont just init this object generically by passing in only self but we also want it to be able to take in name, house as well.
        def __init__(self, name, house):
            # If we want to initialize the contents of a class we define this method. 
            # This is the Student() function defining phase of the class.
            # The fascinating part here is that the 'self' can be anything.
            # Self is being instantiated or initialized here as an example, prototype or generic object of the class Student. 
            # It is a placeholder for the actual object that will be created when we call the Student() function.
            self.name = name
            self.house = house
            # This is like a mold, the manifestaion of the object oriented programming.
            # It's like adding keys to dictionaries but in this case we are adding variables to objects.
    def main():
        student = get_student()
        print(f"{student.name} is from {student.house}")
        # Attributes are the properties of the class, they are like the keys in a dictionary but they are not strings, they are identifiers
        # They are like the keys in a dictionary but they are not strings, they are identifiers
        # They are also called the instance variables because they are variables that are associated with a particular instance of the class
        # .name and .house are basically just variables called name and house inside of an object whose type is Student, so they are instance variables
    def get_student():
        # The attribute values can be any data type, including other objects, lists, dictionaries, or even functions. This allows for complex data structures and relationships between different pieces of data.
        # It turns out with classes unlike dicts we can actually standardize all the more what those attributes can be and what kind of values we can set them to
        # let's manually just assign inputs into local variables
        name = input('Name: ').lower().capitalize()
        house = input('House: ').lower().capitalize()
        # Now instead of creating a student object fom my student class and then manually putting the attributes inside of it let's call the Student() function
        # This Student() function is identical to the class name with the capital letter included let's pass in name and house into it and assign it to student variable
        # the Student() function insput just takes in previously defined variable as if they are the newly set attributes to the whatever function assigned to in the LHS of the assignment operator
        student = Student(name, house)
        # Student(name, house) is called the constructor call where we are assigning name, house to student the way name, house are assligned to the self in the def __init__() method of the Student class.
        # This line of code constructed or instantiated a student object for us and we can now use it in the main() function to print out the name and house of the student.
        # How is it going to use the student class? It is going to use the Class Student as a template, as a mold of sorts so that every student is structured the same way.
        # Because we can pass inarguments to this Student() function we are gonna be able to customize the contents of that object.
        # It's like creating housing based on templates but having different paintings and plantations.
        # Here each student is going to have same attribute distribution but name, house local variable assignment will give us the variation in this case.
        # It's ultimately going to give me an opportunity to error check and validate the inputs before they are assigned to the attributes of the object.
        # Now we have motre control to the correctness of my data and let's now go to the class block.
        return student

    if __name__ == "__main__":
        main()

# Let's tighten things  up
if False:
    
    class Student:
        def __init__(self, name, house):
            #if name == ''
            if not name:
                # if we just print('Missing name') the path will still go on
                # importing sys and doing sys.exit('Missing name') is an obnoxious solution, you are gonna quit the whole program? DUDE!
                # it's too late for return None. By the def get_student() block student is crated somewhere in the memory
                # We can not nope nope there is no object because the object is already created
                # There is another exception keyword called raise. It is the same mechanism how python raises error messages in the terminal
                # It's like something exceptional in a very bad way has happened, and we want to allow the programmers to try to catch that excreption as needed
                raise ValueError('Missing name')
                # We can treat these errors as functions and pass in explanation in str
                # Now let's go and try to return Student(name, house) in that code block
                # We just raised our own exceptions to signal these errors
            houses = ['Griffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
            if house not in houses:
                raise ValueError('Invalid house')
                # So here we now see a capability that we can do with classes that we can't with dictionaries.
                # If we add an attribute/key to a dictionary it's going in no matter what. Even if house = some random string int's going into the dictionary anyways
                # In class by this __init__() method we can now control what's going to be installed within these objects
            self.name = name
            self.house = house

    def main():
        student = get_student()
        print(f"{student.name} is from {student.house}")

    def get_student():
        name = input('name: ').lower().capitalize()
        house = input('house: ').lower().capitalize()
        # We don't want students to add whatever houses or empty names
        # The validation stays in the class block renders easy
        return Student(name, house)
        # The object will simply raise a ValueError in the terminal whenever the wxceptions occur.
        
    if __name__ == "__main__":
        main()
    # If we want to add First, Middle and Last name inputes we will just create attributes for each in the def __init__() block
    # We can have a list of arguments inside def __init__() parentheses.
    # The class can be put into modules.
    # by creating house=None we could make it optional
    # And for exceptions, there is a suit of exceptions and we can make exceptions of our own like AbidError

# Can we print the Student object?
if False:
    def main():
        student = get_student()
        # The print looking for a print will trigger the __str__() method of our obj and return the str
        print(student)
        # Just printing the object will give '<__main__.Student object at 0x0000016CA40D70E0>'
        # It is showing where in the computer's memory where it exists. It is a 16bit hex number lol
        # It's just a default way of describing where this object exists
        # We can override it with another class method called __str__(), it allows us to provide a string representation of our object.
        # Let's introduce this method after the init block
    
    
    def get_student():
        name = input('name: ').lower().capitalize()
        house = input('house: ').lower().capitalize()
        return Student(name, house)

    class Student:
            def __init__(self, name, house):
                if not name:
                    raise ValueError('Missing name')
                houses = ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
                if house not in houses:
                    raise ValueError('Invalid house')
                self.name = name
                self.house = house
    
            def __str__(self):
                # This one takes only one argument, the self. Pretty selfish method.
                # Let's return a student!
                #return 'a student! ^_^'
                # Now let's just simply return an f'str'
                # Remember 'return' returns only one str 
                return f"{self.name} is from {self.house}"
                # Here self is our beloved object ^_^
                # It's gonna fetch the variables from the __init__() method block which is at the top of the pyramid
    
    if __name__ == "__main__":
        main()

#  __repr__() is meant for developers
# now let's create our own method, real utility of the class objects
# Let's us now create their patronous

def main():
    student = get_student()
    print(student, student.charm(), sep='')

def get_student():
    name = input('name: ').lower().capitalize()
    house = input('house: ').lower().capitalize()
    # Classes not only have instance variables they can also have functions built in aka method
    # A function that is associated with a class is called a method
    # Now we are at the brink of creating functionality within our student object
    # Let's create a function called charm()
    patronus_emojis = {
                'Stag': '🦌',
                'Otter': '🦦',
                'Doe': '🦌',
                'Phoenix': '🕊️',
                'Jackrabbit': '🐇'
            }
    patronus = input(f'choose a patronus from {patronus_emojis}: ').lower().capitalize()
    return Student(name, house, patronus)

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError('Missing name')
        houses = ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
        if house not in houses:
            raise ValueError('Invalid house')
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house} says, \n \'EXPECTO PETRONUM\''

    # Classes not only have instance variables they can also have functions built in aka method
    # A function that is associated with a class is called a method
    # Now we are at the brink of creating functionality within our student object
    # Let's create our function charm()
    def charm(self):
        # As it's a method inside of a class, by convention it must take at least one argument, for instance self
        # We will implement charm in such a way so that the method returns an emoji that's appropriate for each student's patronus
        match self.patronus:
            case 'Stag':
                return '🦌'
            case 'Otter':
                return '🦦'
            case 'Phoenix': 
                return '🕊️'
            case 'Jackrabbit': 
                return '🐇'
            # we use _ for default or any
            case _:
                return '🪄'
            # Let's now go to main() block
        #return patronus_emojis.get(self.patronus, '✨')


if __name__ == "__main__":
    main()