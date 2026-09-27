# This is a script to learn global variables
# Let's start with a global variable called balance
balance=0

# [Introduction] let's define a main() function to print out a balance whenever it get's a cli call 
def main():
    print('Balance:', balance)
    # An interesting corner case, if we assign to similarly named local variable to a global one it will not be prefered to the global one if mentioned explicitly with global adjective inside a custom function.
    # That means a global function is unmutable in other blocks once mentioned with global in ant of the blocks.<turns out it is not true in the main block>. It will create bugs so not recommended to that.
    deposit(100)
    withdraw(20)
    # Both of them are reading from and writing to the global variable.
    print('Balance:', balance)
    # Now let's define the custom functions.
    # If we hit run after custom function construction we should encounter 'UnboundLocalError: local variable 'balance' regerenced before assignment'
    # The problem was by convention we can read from global variable but can't write to it.
    # So let's try putting balance inside of main() but this is super weird because we are expecting the custom functions to have balance inside it. Still doesn't work 'UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value'. It's not local to the custom functions as thery can not even read from it let alone weite to them.
    # We can solve this by adding global adjective to the global function to make it understand that it is a global variable and you can write to it as well.

# Thus we have a terribly short program, what's the catch David?
# - Well look at the top, we have a variable that not just main but any other function can utilize. 
# Calling the whole thing inside cli works. But let's not stop here, let's add depositing and withdrawing, the most basic function of a bank. 
# Let's type in inside our main block whatever functions we will later develop precisely.
def deposit(curr:int)->int:
    '''Takes in int as currency and adds to the global balance'''
    global balance
    #balance=0 # We can use it here after the global calling not before
    balance+=curr
    # Each time the code runs the balance is reassigned to zero at the top, so use another local variable called session balance 
    #return balance
    # That's a redundency, we don't have to return as we are modifying it.

def withdraw(curr:int)->int:
    '''Takes in int as currency and subtracts from the global balance'''
    global balance
    balance-=curr
    # Same as deposit()
    #return balance

# [Conclusion] the usual, __name__ calling if =='__main__'
if __name__=='__main__':
    main()
