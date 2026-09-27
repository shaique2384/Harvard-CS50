# We came back from 3_meows.py
# Let's remember a program which prompted users for their name and we could split the user's name into two separate variables[unpacking from a datastructure and put it into a variable].
# I just made a custom author formatting using APA 6.
if False:
    names=input('Please input author\'s full name.').split(' ')
    last=names[-1]
    first=names[:-1]
    firsts_abb=[f'{name[0]}.'.upper() for name in first]
    # Works only for lists types of datasets
    if not first:
        print('Please kindly, input full name')   
    elif len(first)==1:
        # names[:-1] slices the list from the beginning up to (but excluding) the last element
        print(f'According to APA 6 your name would appear as <{last}, {firsts_abb[0]}>.')    
    else:
        firsts=' '.join(firsts_abb)
        print(f'According to APA 6 your name would appear as <{last}, {firsts}>.')

#Jarvis Method:
if False:
    raw_input = input('Yo! WTF is your name? ').strip()

    # Split into words
    names = raw_input.split()
    # Return a list of the substrings in the string, using sep as the separator string.

    if not names:
        print("No name entered!")
    elif len(names) == 1:
        print(f"According to APA 6 your name would appear as <{names[0]}>.")
    else:
        last = names[-1]
        first_names = names[:-1]
        
        # Abbreviate each first/middle name using a list comprehension
        firsts_abb = [f"{name[0].upper()}." for name in first_names]
        
        # Join with space (works for 1 or many first names)
        formatted_firsts = " ".join(firsts_abb)
        
        print(f"According to APA 6 your name would appear as <{last}, {formatted_firsts}>.")

# Now David's upacking specials
if False:
    first,_=input('What\'s your name? ').split(' ')
    # We don't need the second name to greet so we just _ because we have to provide at least some variable to store the value [an attempt to abstract storing in local ram in real time] to accomplish the unpacking.
    print(f'hello, {first}')
    # There are other features that python offers when it comes to defining and using funstions and it is slightly more intermediate functionality if you will that's useful because we can start to write even more elegant and powerful code once we get comfortable with syntax like this.
    # Let's not simply greet let's alose involve some coinage again using fantasy world entities like galleons, sickles and knuts[There is a mathematical relationship between those according to their mathmatical relationship].

# My code for qizarding currency
if False:
    def main():
        balance=total(100,50,25)
        print(balance)
        
    def total(galleons=0, sickles=0, knuts=0):
        if knuts>=29:
            sickles+=int(knuts/29)
            knuts=knuts%29
        if sickles>=17:
            galleons+=int(sickles/17)
            sickles=sickles%17
        return f'you have {galleons} galleons, {sickles} sickles, {knuts} knuts'

    if __name__=='__main__':
        main()
        # Works totally!
        # you have 102 galleons, 16 sickles, 25 knuts

# Now David's turn,
if False:
    def total(galleons:int, sickles:int, knuts:int)->int: 
        '''
        The formula to get total sickles.

        :param: galleons x 17 = sickles; sickles x 29 = knuts
        '''
        return (galleons*17+sickles)*29+knuts

    coins=[100,50,25]
    # if not list then it will assign the values in commas one after another.
    print(total(coins[0], coins[1], coins[2]), 'knuts')
    # Works totally! The math still checks out.
    # 50775 knuts
    # But we haven't done any unpacking yet, let's first assign our total as a list into coins. 

# Let's create a custom function which takes in a list of given currencies.
if False:
    def total(box:list)->int:
        '''
        The formula to get total sickles from a list of currencies of the wizarding world.

        :param: Box must have 3 elements as currencies as galleons, sickles, knuts following order
        :relationships: galleons x 17 = sickles; sickles x 29 = knuts
        :returns: Total currency in knuts
        :rtype: int
        '''
        #galleons,sickles,knuts=box[0],box[1],box[2]
        return (box[0]*17+box[1])*29+box[2]    

    def un_total(knuts:int)->dict:
        '''
        The formula to get perfectly organized galleons, sickles and knuts from a bucket of knuts.

        :param: Takes in knuts
        :relationships: galleons x 17 = sickles; sickles x 29 = knuts
        :returns: A dictionary with keywords as the string literal of the currencies.
        :rtype: dict
        '''
        sickles,knuts=int(knuts/29),int(knuts%29)
        galleons,sickles=int(sickles/29),int(sickles%29)
        return {'galleons':galleons,'sickles':sickles,'knuts':knuts}

    coins=[100,50,25]
    print(total(coins), 'knuts')
    # Well it turns out I'm much ahead than cs50 they are still talking about if they can assign coin list into the galleons in the first version.
    print(f'{un_total(total(coins))} is our dict.')
    ut=un_total(total(coins))
    print(f'That means you have {ut['galleons']} galleons, {ut['sickles']} sickles and {ut['knuts']} knuts')


# Good new is that there is a way we can pass in list unpacked into or first type of total parameter.
if False:
    def total(galleons=0,sickles=0,knuts=0):
        return (galleons*17+sickles)*29+knuts

    coins=[100,50,25]
    #print(total(coins),'Knuts')
    # We can unpack lists just like we previously unpacked str class's split function into multiple tings.
    # Very much like the unpack of max or pd files we can unpack lists using an aesterisk sign before the variable containing it. 
    # It will automatically return elements with commas in between.
    print(total(*coins),'Knuts')
    print(*coins)
    # We can not use unpack in str to variable assignment.

# Does not work with sets where order is not preserved but works with dicts;
if False:
    def total(galleons=0,sickles=0,knuts=0):
        '''
        Takes in all wizarding currencies and returns knuts for laundry. Unpacking lists following order or dicts with keywords similar but unpreserved order works as well.

        '''
        return (galleons*17+sickles)*29+knuts

    #print(total(galleons=100,knuts=25,sickles=50), 'Knuts')
    # Still the matchs chekcs out because it is no longer positional.
    # With the help of keywords into our custom func we can totally ignore the order.
    # Wait a minut! Names and values, names and values, names and values AAAAA, I remember we can totally unpack a dictionary with any order!
    bucket={'galleons':100,'knuts':25,'sickles':50}

    #print(total(*bucket),'Knuts')
    # Well certainly this doesnt work because it gave us 50775galleons knuts :'( 
    '''
    galleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsknutssickles Knuts
    '''
    #print(*bucket) 
    # This prints this <galleons knuts sickles> but we can definitly index with the keys when unpacked.
    #print(total(bucket['galleons'], bucket['sickles'], bucket['knuts']), 'knuts')
    # But imagine the program is a little longer, we would face proper ugliness this way.
    # We were short because of David's theatricality, we need 2 aesterisks for unpacking dicts
    print(total(**bucket),'Knuts')
    #print(**bucket)
    # Above won't work because <TypeError: print() got an unexpected keyword argument 'galleons'>
    # So wrapp around strings around it, doesn't work either because it can pass in as typed keywords with = sign but can not assign to a variable, the characters have commas in between that is why can't be used as code lines to assign to keywords as brand new local variables.
    # So **bucket == (galleons=100,knuts=25,sickles=50)

# The functions can also have felexible input value properties while aesterisks as prefix like *args, **kwargs. Let's now define a function called f() that will utilize just that.
if False:
    def f(*args, **kwargs):
        # *args means it takes in a variatic number of positional[positional means that goes typically from left to right] arguments but wthout any limit as yet.
        # **kwargs means a variable number of 'keyword' arguments. These convensions frequent in python's own documentation.
        # Now let's use inside it a diagnostic method to print out the input positional args and kwargs, as if inside out.
        print('Positional:',args)
        print('keywords:',kwargs)
        ...

    f(100,50,25,5,galleons=100,knuts=25,sickles=50,pennies=4)
    # We can see it prints out any number[including 0] of args or kwargs as touples or dicts.
    '''
    Positional: (100, 50, 25, 5)
    keywords: {'galleons': 100, 'knuts': 25, 'sickles': 50, 'pennies': 4}
    '''
    # We can symply use this method to pack into touple or dicts flexible number of elements.
    #f(int(input('Number: ')))
    kList=[]
    for _ in range(2):
        pass
        '''
        kw=input('Name: ')
        v=int(input('Value: '))
        kList.append(f'{kw}={v}')'''
    #does not work :'( ask jarvis later, after finishing the course)
    #f(*kList)
    # For *args input of our f() let's remember our very first courses on print function, we had print from python documentation (*objects, blabla and bla) and we can definitly infer that the aesterisk that day meant print can take in variable number of objects as inputs.

# According to that notion we could define a function exactly like print;
if False:
    def prinj(*objects,sep=' ',end='\n'):
        for object in objects:
            # Do some assmbly to machine code shenanigans on the object as chars in C or that ansi regulation so that cli can yell at you if you don't provide a string with ''s.
            ...

    # That is why in past we could do just this without any frawn in the cli,
    print()
    # It automatially gives a new line, annoying.
    # This way if used, regulations of flexibility can pass in from one def func() block to another with mechanisms involved .
    # This above is one of many ways we can enjoy the functionality of aesterisks in python.

# It turns out there are other ways we can utilize python toolkit related to the types of programming models that python supports.
# Before we have done procedural programming whereby we look top to bottom of a dataset for a specific expression, functions or procedures.
# But later we discovered that python is much more object oriented, and the lot of those variables, types were infact all objects situated in certain classes which were basically blueprints where we could encapsulate data or functions.
# We also encountered a notion which python also to some extent supports-the third paradigm of programming, called the functional the functional programming.
# In these cases functions are evermore powerful that they tend not to have side effects, no changing of state globally but rather they are completely self contained and might take as inputes and return values.
# We saw examples of that when we started sorting things, our sort functions and lambda functions.
# It turns out python has more ways to utilize the essence of functional programming and let's now talk about map.
# Let's terminal now, code 5_yell.py and we will meet there! ADIOS AMIGOS!