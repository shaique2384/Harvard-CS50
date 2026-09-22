# This is a script to learn global variables
# Let's start with a global variable called balance
balance=0

# [Introduction] let's define a main() function to print out a balance whenever it get's a cli call 
def main():
    print('Balance:', balance)
    balance=deposit(100)
    balance=withdraw(20)
    print('Balance:', balance)
    # Now let's define the custom functions.
    # If we hit run after custom function construction we should encounter 'UnboundLocalError: local variable 'balance' regerenced before assignment'
    # The problem was by convention we can read from global variable but can't wri

# Thus we have a terribly short program, what's the catch David?
# - Well look at the top, we have a variable that not just main but any other function can utilize. 
# Calling the whole thing inside cli works. But let's not stop here, let's add depositing and withdrawing, the most basic function of a bank. 
# Let's type in inside our main block whatever functions we will later develop precisely.

def deposit(curr:int)->int:
    ...
    '''takes in int as currency and adds to the global balance'''
    balance+=curr
    # Each time the code runs the balance is reassigned to zero at the top, so use another local variable called session balance 
    return balance

def withdraw(curr:int)->int:
    ...
    '''takes in int as currency and subtracts from the global balance'''
    balance-=curr
    # Same as deposit()
    return balance



# [Conclusion] the usual, __name__ calling if =='__main__'
if __name__=='__main__':
    main()
