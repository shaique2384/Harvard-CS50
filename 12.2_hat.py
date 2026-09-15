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
        
# No matter what the class will end up being, this the exact syntax to instantiate the object hat, like n = note.Note()
hat = Hat()
# Let's assume Hat() is much simpler than Student() and it has some sorting capabilities
# Let's assume hat has only one function .sort()
hat.sort('Harry')
# Let's now initiatlize the class
