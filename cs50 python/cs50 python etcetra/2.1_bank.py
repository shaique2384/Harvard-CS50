# We were trying to solve the bank problem, here is my method, did not work lol haha.
# I got this in cli 'UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value'.
if False:
    class Bank:
        balance=0

        def __init__(self,name):
            self.name=name

        def __str__(self):
            return f'{self.name} has {self.balance}'

        def deposit(self, curr:int)->int:
            balance+=curr

        def withdraw(self, curr:int)->int:
            balance-=curr

        @classmethod
        def show_balance(cls):
            return f'{cls.balance}' 

    account1=Bank('Shaique')
    account1.deposit(100)
    account1.withdraw(10)
    print(f'{account1} has {Bank.show_balance()}')

# Now let's try David's method, he creates a class called account.
if True:
    class Account:
        def __init__(self,name):
            # It takes at least one input and that must be self by convention.
            self._balance=0
            # By this the __init__() gives us the instance variable called balance initialized initialized for this account to 0.
            # He defines an unmutable(by reassignments in other blocks and decorators) variable with._balance to self as an object attribute independet of constructor inputs and assigns it to 0.
            self.name=name

        def __str__(self):
            return f'{self.name}'.capitalize()

        # now let's define a function called balance() which will be a property and will return the self._balance.
        @property
        def balance(self):
            # We must use a decorator @property above it.
            return self._balance
            # This is the ability to return self._balance anytime of the class object handling outside the block [Let's recall getter from the Xstudent.py lesson script].
            # If we used assignment of balance inside the __init__() argument then there would be no scope of a starting balance=0. If we did not use ._balance then it could be modifiable outside our class block and @property simply gives us a special ability to return a constructor attribute(or property) after modification inside the class block while staying immutable outside the class block [Although totally possible to reassign in other blocks using ._balance after instance construction which is why it is recommended ro avoid unless viewing the internal nesting of the class]
            # As in this case we do not have a setter, nobody can reassign balance without tweaking the class block.

        def deposit(self,n=0):
            self._balance+=n
            # We are following the order of the class block execution; __init__>setter ability securing with @property>(deposit|withdraw)

        def withdraw(self,n=0):
            self._balance-=n
    import cowsay
    acc=Account(input('Account Holder\'s name: '))
    print(f'Hi {acc}, in your balance you have BDT. {acc.balance}')
    acc.deposit(int(input('Deposit amount in number : ')))
    acc.withdraw(int(input('Withdraw amount in number : ')))
    cowsay.cow(f'{acc}, your current balance is BDT. {acc.balance}. \nThank you for doing business with us.')
    # IT FRIGGIN WORKS! We enjoyed the power of instance variable using class as it is intended to model any real or imaginary entity.

# For a reasonably small script global keyword(usually frowned upon in the python commuity, for unclear nesting) works just fine but it is cleaner and more stable to use class to solve the same problem.
# Another notion to mention is that these global variables are always local to a module.
# Some languages allow us to create a variable that can never be changed no matter how, these are called constants[not possible to reassign, or usually can not be reassigned without great effort], it allows us to program defensively.
# In python we are kind of in an honor system here, we have convensions to indicate that smth should be treated as though it's a constant but it's not actually enforced by the language.
# Let's terminal code 3_meaws.py

