# In this file we will implement the idea of a vault at gringots keeping on theme wherein there's a bank in the world of harry Potter.
# Within this bank families and individuals have vaults containing all sorts of money in the wizarding world.
# The money that exists in the world of Harry Potter are coins called galleons, sickles and knuts in descending order of values.
# So iin each of those vaults there will be coind gold, silver and bronze essentially each in those denominations tucked away(hidden).
# Let's implement the idea of vault so that I can store for instance for Harry potter, Ron Weasely how much coinage is in each of their family's vault or account.
# Let's go ahead and vault up high by creating a class called vault;
class Vault:
    # We could use dict, list or touples but we will see with it one final flourish with operators
    # For the input of constructor function we shall use the type of coins on top of self; [They are storing these currencies in their object or instance type called vaults, a real world entity]
    # When we pass in gallion=0 into the __init__() function we are setting the default value as 0.
    def __init__(self,name,galleons=0,sickles=0,knuts=0):
        # I will not use unnecessary whitespaces in the code anymore.
        # pass serves as a syntactically valid "no-op" (no operation). In Python, using pass inside a class's constructor (__init__) tells Python to do nothing when a new instance of that class is created.
        #pass
        self.name=name.capitalize()
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts
        # We could add some error checking especially if we don't pass in a number, we could turn it into properties to do even more validation but let's keep it simple and as always let's focus only on new ideas so we are gonna trust that relevants arguments will be passed in properly.

    def __str__(self):
        return f'{self.name} Vault Balance: {self.galleons} Galleons, {self.sickles} Sickels, {self.knuts} Knuts'

    def __add__(self, other):
        # Now whenever in the main we have operator overloading happening in this case + operator, it's automatically going to look for __add__() method and pass in the operand and operator arguments into it.
        # Let's create local variables related to the attributes of the self and the other self
        galleons=self.galleons+other.galleons
        sickles=self.sickles+other.sickles
        knuts=self.knuts+other.knuts
        # But in the end we need to return a brand new bigger vault that contains all of those contents together.
        # If we ultimately want to assign that bigger vault to the left total obejct in the main, we better indeed return a value from this add method which must also be another vault.
        return Vault('Total', galleons, sickles, knuts)
        # This way plus can be used for joining two lists into a list on top of addition and concatenation.
        # It is not possible to arbitrarily assigning operators to random symbols, it has to be a subset of the long list of python defined operator overloading on top of the exact operators.
        # Examples of other composite methods like these,
        '''
        object.__add__(self, other)
        object.__sub__(self, other)
        object.__mul__(self, other)
        object.__matmul__(self, other)
        object.__truediv__(self, other)
        object.__floordiv__(self, other)
        object.__mod__(self, other)
        object.__divmod__(self, other)
        object.__pow__(self, other[, modulo])
        object.__lshift__(self, other)
        object.__rshift__(self, other)
        object.__and__(self, other)
        object.__xor__(self, other)
        object.__or__(self, other)
        These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |).
        Add r and i before theme like __radd__() or __iadd__() for reflected (swapped) operands and augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=)
        '''
        #total.name='something'
        #return total
        #return f'{total=}'

        ...
    

def main():
    # For now our goal is simply to print whatever in the vault of someone, printing the receipts of vault balance so to speak.
    potter=Vault('potter',100,50,25)
    print(potter)
    '''This should only give the location of the object in our ram;
    <__main__.Vault object at 0x00000276738581A0>;
    <__main__.Vault object at 0x000001E5C1E081A0> #see? Different ram location for 2 different cli calls.'''

    # So let's go back to class and define __str__() method. Note we can't use self as a str argument or variable inside an f string, we have to use name variable for that.
    # Let's now bring in his friend Ron's family vault as well who has lower balance.
    weasely=Vault('weasely',25,50,100)
    print(weasely) 
    if False:
        # This way __init__() and __str__() methods will be invoked twice for each of those vault objects.
        # Let's think about how to combine the contents of two vaults in our code. Let's first combine Galleons for both i.e, total galleons in the vault
        galleons=potter.galleons+weasely.galleons
        #print(f'Total Vault Galleons: {galleons}')
        # But let's create a total instead
        sickles=potter.sickles+weasely.sickles
        knuts=potter.knuts+weasely.knuts
        total=Vault('Total',galleons,sickles,knuts)
        print(total)

    # Wouldn't it be nice if we simply add objects potter and weasely and got rid of all the unnecessary math in the main()? Like this?
    total=potter+weasely
    print(total)
    #total.name=...
    # it's called operator overloading. It is exactly what __str__() does
    # In python and class there is a way to do this, go to docs.python.org/3/reference/datamodel.html#special-method-names
    # The third special method is called object.__add__(self, other) which works on any objects generically even notes.
    # self is the object that is residing left to the + sign and other to the right. Other is the other self other than self.
    # They denote operand on the right and operator on the right while operator plus in between.
    # In our code we will implement the support for this, without the support python will show a TypeError because python doesn't know what we want to do here so let's scroll back to class and add another special method called __add__(self,other)

# All the examples we have seen so far over the weeks for example int, str, list, dict etc all of them were classes themselves and now we get to define and create our classes and objects. This was the final course material for cs50 python!

if __name__=='__main__':
    main()