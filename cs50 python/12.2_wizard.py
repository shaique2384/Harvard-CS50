# We are here from 12.1_student.py to understand inheritence in OOP
import dis

class Wizard:
    # So far we have self.name as common attribute but we can also definitly have other constructor variables like patronous and so on
    def __init__(self, name):
        # Let's keep name only and raise value errors if not name
        if not name:
            raise ValueError('HEI! GIVE US THE NAME!')
        self.name = name
        # Let's put a # before everything related to name in other classes to make them inactive.
        # name arg of __init__() in both student and professor classes got offline because we havent told python that both students and professors are wizards themselves.
        # To make student and teacher descend or inherit from super class Wizard we need to pass in Wizard as the argument of class Student(): header.
        # It means they are inheriting all the attributes from the wizard class.
        # We need to do another thing before name arg in the constructor block of descendent class comes online.
        # We have to say explicitly that we need the attributes of constructor lock of class Wizard althoug we have separate constructor blocks of the desnendent classes.
        # Function super() under their constractor block (super means supar or parent) accesses the __init(arg) method and its self.arg attribute of the existing super class Wizard when added with a .__init__(arg).

    def __str__(self):
        return f"My name is {self.name} and I am not a muggle!"

    ...

# Let's start by initializing a class Student with name and student attributes
class Student(Wizard):
    def __init__(self, name, house):
        #if not name:
            #raise ValueError('HEI! GIVE US THE NAME!')
        #self.name = name
        super().__init__(name)
        # It seems like __init__() is a method of super() function.
        # It's typical used to call a cooperative superclass method and works for class methods too.
        # Let's do the same down on the class Professor block
        self.house = house
        # By default we can simply just create a student object inside the main assigning it with Student(arg1, arg2)
        # Let's keep a placeholeder for other functionality

    def __str__(self):    
        return f'I am from {self.house} house, {super().__str__()}!'
    
    ...

    

# Let's now create a class called professor
class Professor(Wizard):
    def __init__(self, name, subject):
        #if not name:
            #raise ValueError('HEI! GIVE US THE NAME!') 
        # We have to copy paste that means we can improve the design and for this case we can enjoy some inheritance.
        # Also they don't have to exist in parallel but can come with hierarchy between them.
        # Let's now define class Wizard which comes with common attributes shared by professors and students at the top of our code
        #self.name = name
        # This is a smaller caviate, a reundancy, identical name for both classes
        super().__init__(name)
        # super() is a function that accesses the super class and .__init_() specifies the exact attribute that we want it to access
        self.subject = subject

    def __str__(self):    
        return f'I teach {self.subject}, {super().__str__()}!'

    ...

# We made with Gervais
if False:
    name = input('Name: ').lower().capitalize()
    ans = input('you a student or a professor?').lower()
    if ans == 'student':
        house = input('House: ').lower().capitalize()
        student = Student(name, house)
        print(f'Students from {house} are so rude! You just said "{student}"')
    else:
        subject = input('Subject: ').lower().capitalize()
        professor = Professor(name, subject)
        print(f'Professors who teach {subject} are so rude! You just said "{professor}"')

def main():
    # Let's come back to Malan
    student = Student('Harry', 'Griffindor')
    professor = Professor('Severus', 'Defense Against the Dark Arts')

    # If we want more generically just a wizard who is neither student nor professor with one str arg only
    wizard = Wizard('Albus')
    str_list = [student.name, student.house, professor.name, professor.subject, wizard.name]
    #for _ in str_list:
        #print(_)

    

# We can have multiple layer of super class like super super class
# When we subclass a superclass with inputing the superclass name in the class header we actually inherit all the attributes
# We can also override some attributes 
# There are also ways to have multiple parents on the same level
# Class also have exception with errors as well as other exceptions but they are all hierarchical in nature
# let's go to docs.python.org/3/library/exceptions.html and fetch this,
    '''
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
'''

# All the exceprtions there are also hierarchical in nature, remember the voice leading rules and our vector ml model in this hierarchical fashion.
# The exceptions themselves actually descend from or inherit from superclasses already.
# For example ValueError has a superclass called exception which ultimately inherits from BaseException.
# Well it turns out all the other errors have some functionalities in common like the intersection of a venn diagram exists in BaseException.
# At one point of the development of python the developers decided to keep things nested like instead of copy pasting same attributes over and over again.
# It's a more robust and energy conserved way of organinizing.
# With the try method of capturing error we can have all the other common functionalities of exceptions get checked as well.
# If we wanna create our own exception probably it's not a good idea to reinvent same thing, it's better to inherit from existing relevanr classes, let's check the exception python files

    import random
    str = random.choice(str_list)
    print(str)
#dis.dis(main)

# Clasees have features that we are taking for granted for weeks now for example operator overloading
# We can take very common symbols like plus or minus or other such syntax on the keyboard and we can implement our own interpretation thereof.
# Plus does not have to equal addition even in default python plus also means concatenation.
# This is called overloading i.e, oveloaded by the authors of python so that we can use the same symbol way but with a different data types to solve slightly different problems.
# Let's create a new final file called vault so let's terminal code 13_vault.py
