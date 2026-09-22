if False:
    # Let's implement the notion of sorting hat, which in the story assigns houses to the students
    import random
    class Hat:
        def __init__(self):
            # self would be the only argument here
            self.houses = ['Griffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']

        # Let's define sort() first
        def sort(self, name):
            # We are adding name arg on top if self because we want our class method sort() to take in name og the student
            # We can also make it take in an object, who knows    
            # Let's put the list in the instance constructor block
            #n = random.randrange(0,4)
            #print(name, 'is in', self.houses[n])
            # We can also use rand.choice() function which takes in a list to choose
            #house = random.choice(self.houses), we can also put it in the print input, a question of aesthetics
            print(name, 'is in', random.choice(self.houses))
            ##return f'{name} is in, {random.choice(self.houses)}'

    # No matter what the class will end up being, this the exact syntax to instantiate the object hat, like n = note.Note()
    hat = Hat()
    # Let's assume Hat() is much simpler than Student() and it has some sorting capabilities
    # Let's assume hat has only one function .sort()
    hat.sort('Harry')
    ##print(hat.sort('Harry'))
    # Let's now initiatlize the class

    # When should we use class methods? When we want to have a method that is not an instance method, but it is a method that is related to the class itself. 
    # For example, if we want to have a method that returns the number of houses in the Hat class, we can use a class method.
    # When should we use class to represent something in our code?
    # When we want to represent something that has a state and behavior, we can use a class. 
    # When we want to represent some real world entity like a note object or somr fantasy world entity like the sorting hat
    # We could use all these with a dictionary but class comes with a lot more functionality.
    # In this code class is like ablueprint but in harry potter we had only one sorting hat.
    # In our code we can have multiple hats,
    hat1 = Hat()
    hat2 = Hat()

if False:
    # But in harry potter there is only one singleton
    # So far we are just using instant methods, but we can also use class methods.
    # These are methods that are related to the class itself and not to any particular instance of the class.
    # It's totally possible to have a class method that is not related to any instance of the class, but it is related to the class itself.
    # Class will be like a container for data and functionality that are somehow conceptually related, for this case things related to a sorting hat.
    # If I'm not gonna instantiate multiple houses I dont really need the __init__() method which meant to initialize specific objects from that blueprint.
    # So let's remove self but keep houses list as variable.
    # We can keep the houses variable indented to our class Hat: header as it turns out in addition to class methods we can also have class variables.
    import random
    class Hat:
        # Class variables exists in the class itself and there is just one copy of that variable for all of the objects thereof
        # They all share if you will, the same variable, for this case we have a list of houses names as strs.
        # So it exists outside the self instances in the trunk of the tree, so to speak, and all the instances of the class can access it.
        houses = ['Griffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']

        # And with sort it also doesn't make sense to have it sorting within a specific hat() object or instance of the class, and I want only one global sorting hat.
        # We can use a class method to sort students into houses, and we can call it without instantiating the class.
        # we use cls instead of self to funrther strengthen our point.
        # Oops using class will definitly conflict with the class header.
        # We can now easily call cls.houses to access the class variable houses as opposed to self variables i.e, one copy only.
        @classmethod
        # Also note that there is no @instancemethod like above. 
        # Any defined method under class <title>: header is an instance method by default.
        def sort(cls, name):
            # ^It's like putting attributes to the cls or self with a input name and getting the return value as designed with name and variables in the context of a Class or an object respectively.
            # Also note that we are calling the variable not from the function locally, we are calling them from the globally available class variable.
            print(name, 'is in', random.choice(cls.houses))

    # I don't have to instantiate any hat() objects here like before we can simply call the class method sort() on top our class Hat, as it is a global class method 
    # We simply capitalize the hat object into Hat class like our very first class lesson.
    # Also we are not using objects because we are usingany object specific operation, for instances, pun intended ;)
    Hat.sort('Harry')

# We could simply do this below, but the above is just touching the oop to design the world
import random
houses = ['Griffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']

def sort(name):
    print(name, 'is in', random.choice(houses))

sort('Shaique')

# But as our code gets longer as we start collaborating with other people and if problems that we want to solve get a bit more sophisiticated our code can get messy quickly
# And we are gonna find that we have a huge number of functions in one file and some of them are related while others are not, organising them with more flexibility will have values.
# And in the world of harry potter we can have a class for students(lol, pun intended), a class for professors, sorting hat and so on.
# Class comes handy when we want to focus on individual ideas. 
# OOP is just a way of encapsulating related data that is variables related functionality inside of things that can have names, are called classes
# Libraries were another soilution to same problem, and sometimes which one should we use overlaps and we will develop instinct and preference to chose over time.
# Let's now terminal code 12.1_student.py and simplify the code there a bit more 



