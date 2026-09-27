# Let's here simply implement a program that just has a cat meowing three times.
if False:
    MEOWS=3
    # But we can easily break the endeavor by reassigining to the capitalized variable name like this,
    MEOWS=4
    # This is to avoid mix upps and accidental reassignments in the code, remember the deepcopy solution for note and pitch objects in music21 tonerow example.
    # Now it turns out there are other sorts of constant variable systems that python can manifest for that we need to start a brand new code block after this one.
    for _ in range(MEOWS):
        # We just hard coded 3 into the range() function but imagin dozens and dozens of lines it's hard to see or rememmber that somehow we hard coded a magic value like 3.
        # So it tends to be a best practice to assign the number 3 to a capitalized variable name at the top so that it acts as a constant, for cases like this.
        print('meaw')

# Let's initiate a class called cat;
if False:
    class Cat:
        # Recall that inside classes we can have not only instance variables inside the constructor block but also class blocks just below the class Cat: header itself.
        # It's accessible to all of the methods underneath it.
        # We must capitalize it to express that it should, should and should not be changed no matter what.
        MEOWS=3
        # It's a python constant but also a class variable.

        def meow(self):
            # We must put Cat.MEOWS to access the class variable.
            # cls.CONSTANT is a way to access class variable anywhere inside the class block
            for _ in range(Cat.MEOWS):
                print('meow')

    cat=Cat()
    # Little cat here and big cat over there lol
    cat.meow()
    # Still it's not like that the regulation to treat it as a costant is not enforced by the language, but it is expected that the programmer should honor that regulation.

# Python is a dynamically typed language, means it's not strongly typed. When we want an int the python still categorizes a str input by default and takes it in. It makes the debugging tricky compared to c and java who enforce these regulations on the syntax level.
# [type hints] docs.python.org/3/library/typing.html
# Good news! There is a ptogram called mypy for checking these if all the lines of our code are adhering to these type hints.
# Let's install it through pip and it has it's own documentation in mypy.readthedocs.io
# To represent it's utility let's proceed with a different aproach to solve the meows problem using def function() without using main(),
if False:
    def M(x:int):
        # colon is for type hint, not an assignment but just a hint that it is an integer
        #for _ in range(x):
            #(x,'meow',end=' ')
        print(x,'meow',sep='',end=' ')
        # It's still printing 4meow althow I have hinted x:int

    #n=int(input('Type any number: '))
    # Let's change the above to devoid of int() function and collide with the type hint.
    #n=input('Type any number: ')
    # The community prefers that python should be flexible like this.
    # Let's go and utilize mypy program who understands type hints by terminaling mypy instead of python our lesson script file.
    # Although the python file.py worked without errors the mypy on the other hand showed this,
    '''
    3_meows.py:50: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
    Found 1 error in 1 file (checked 1 source file)
    '''
    # It showed :50 because the line with error was at that line where we passed in the variable into M() function
    # We can also hint in the variable level by doing the same thing with the variable assignment.
    n:int=input('Type any number: ')
    # mypy shows this now
    '''
    3_meows.py:58: error: Name "n" already defined on line 48  [no-redef]
    3_meows.py:65: error: Argument 1 to "M" has incompatible type "str"; expected "int"  [arg-type]
    Found 2 errors in 1 file (checked 1 source file)
    '''
    M(n)
    # mypy is not a program that a user would rather you and I would use.
    # We can also exercise hint adding to variables as well, let's go before the final line 

# If we create this habit of annonating the variables always we can utilize mypy to solve the issues and still utilize the openness of python flow.
# Also remember when the brain overclocking happened couple of times while exploring music21 the the usual suspects were hidden in plain sight very tiny isuues but beside the bulk of abstract mind taxing logic flow they caused significant overwhelms. 
# So in a nutshell we are getting best of the all worlds. Another benefit of this felixibility is that those imposed regulation by the language are expensive in terms of performance.

# Let's think about a problem where meow() function returns meow some number of times. Sometimes it's better to have return values rather than printing. For this let's consider we by mistake have return iterated.
if False:
    '''
    meow(n:int)->None:
        # To let people know we change the above to this def meow(n:int)->None:
        for _ in range(n):
            #return 'meow'
            # it's reassigning in the outside (n-1) number of times
            print('meow') 
            # We are getiing an extra None because meows=print and print(meows) is giving nothing

    number:int=int(input('Number: '))
    meows:str=meow(number)
    '''
    # Right side actually doing the print() function but as it has no return value, it still returns None by default.
    # Adding type hints ->None we make mypy show the following mistake;
    '''
    3_meows.py:84: error: "meow" does not return a value (it only ever returns None)  [func-returns-value]
    3_meows.py:84: error: Incompatible types in assignment (expression has type "None", variable has type "str")  [assignment]
    Found 2 errors in 1 file (checked 1 source file)
    '''
    #print(meows)


# There is another way of activating mypy
if False:
    def meow(n:int)->str:
        # Recommended way
        #return 'meow\n'*n
        # My intentionally stupid way
        meow=''
        for _ in range(n):
            meow+='meow\n'
        return meow

    number:int=int(input('Number: '))
    meows:str=meow(number)
    print(meows, end='')
    # It should have no issues.

# Let's talk about docstrings now.
# peps.python.org/pep-0257/ documents how one should document their custom function.
# Let's utilize the docstring notation to describe our custom function and add comments just below the def line using tripple quotation mark.
# Let's explore the standardized way to structure the comment and it should turn the comments into titles and paragraphs.
# This is not pythonic, it is a form of restructured text, a mark don type language used for documentation, for websites, for blogs and many more.
# This will not trigger type hints but with this a third party tool can analyze my code for me and generate documentation for me[.pdf, .web etc].
if False:
    # Let's import cowsay
    import cowsay
    def meow(n:int)->str:
        '''
        Meow n times.
        
        :param n: Number of times to meow
        :type n: int
        :raise TypeError: If n is not an int
        :return: A string of n meows, one per line
        :rtype: str
        '''
        return 'meow\n'*n

    number:int=int(input('Number: '))
    meows:str=meow(number)
    # If we hover our mouse over meow() python automatically shows the documentation iside '''<>''' and this functionality can be utilized to extract the documentation for any processes. 
    cowsay.meow(meows)

# Let's now utilize cli for input taking
if False:
    import cowsay
    import sys

    def meow(n:int)->str:
        '''
        Meow n times.
                
        :param n: Number of times to meow
        :type n: int
        :raise TypeError: If n is not an int
        :return: A string of n meows, one per line
        :rtype: str
        '''
        return 'meow\n'*n

    # If the user doesn't provide argv the function meows only once.
    # sys.argv can be used to to streamline existing cli commands to work for the program
    if len(sys.argv)==1:
        number=1
    elif len(sys.argv)==3 and sys.argv[1]=='-n':
        number=int(sys.argv[2])
    elif len(sys.argv)==3 and (sys.argv[1]).lower()=='--number':
        number=int(sys.argv[2])
        # Already our code is getting complicated and this is why as always there exists a library called argparse.
    else:
        cowsay.cow('usage: meows.py')
        # 'usage: meows.py' is an approval statement to say cli style, 'yo! this is the way to do this'
        # again -n means number of times, $ python 3_meows.py -n 3.
        # Now terminal shows this error message;
        '''
        number:int=int(sys.argv[1])
                ~~~^^^^^^^^^^^^^
        ValueError: invalid literal for int() with base 10: '-n'
        '''
        # Let's create an elif above else to demonstrate that.
        number:int=int(sys.argv[1])

    meows:str=meow(number)
    cowsay.meow(meows)
    # Note that this is a meow() function inside cowsay module

# Now let's imagin our program is getting a bit more complicated, I don't wanna suport only -n but also many more.
# We used in our first elif single dashes for abbreviated words like -n for number and we can also use double dashes to utilize numbers.
# A lot of new projects will evolve while doing music21 lessons, plugdata lessons and tensorflow lessons, don't hesitate to waste time there.
# docs.python.org/3/library/argparse.html shows us all these analysis of these cli aeguments[argv stands for argument vector] so that we can focus on creating all these interesting parts of the program instead of scratching head over cli related regulations.

# Let us import argparse
if False:
    import cowsay
    import argparse
    # To parse means is to read it and pick smth apart to analyze it.

    parser=argparse.ArgumentParser()
    # Object for parsing command line strings into Python objects.
    # This is to know about the specific cli argv s that I want to support in my program
    #cowsay.trex(parser)
    # Let's utilize a method add_argument('-n') of parser by which we can add an argument to the parser
    parser.add_argument('-n')
    #* Use any library shortcuts and also learn the foundation codes and write it once yourself.
    # Let's use parse_args() is going to automatially look for sys.argv s for me and I don't need to import sys, it will do that automatically for me.
    args=parser.parse_args()
    # The RHS results in the parser having parsed all of the argv
    # RHS is an object as variable args inside of which are all of the values of those argvs including -n, no matter what order they appeared in[although definitely we can enforce sort()]
    #cowsay.cow(args)
    # It shows  Namespace(n='3')
    # We can also iterate over the range(int(args.n)) where n is an attribute of the instance args which gives us the number after our recent add_argument() of Namespace() which has Namespace(n='3'). So it will render str(3)
    m=''
    for _ in range(int(args.n)):
        m+='meow '
    cowsay.cow(m)
    # It's easier than our previous method although we have to add 3 extra lines of codes. On top of that it does not have any solution for len(sys.argv)==1, yet.
    # A documentation to operate is necessary and when the user uses a special arguments like -h or --help they can see what went wrong. So let's terminal python 3_meows.py --help. We should get this message;
    '''
    usage: 3_meows.py [-h] [-n N]

    options:
    -h, --help  show this help message and exit
    -n N
    '''
    # This is a standard syntax in computing and we have seen it python's documentation before. The square braces means these argvs are optional and the info indicates that the program has the option to take in -n N as argv.

# But this is not going to help my users when I release this into the world so instead we can pass in description inside argparse.ArgumentParser() assigning to it's description keyword the description of what is going to happen.
if False:
    import argparse

    parser=argparse.ArgumentParser(description='Meow like a cat')
    # Now let's add help explanation to add_argument('-n') assigning to the help keyword.
    parser.add_argument('-n', default=1, type=int, help='number of times to meow')
    args=parser.parse_args()

    for _ in range(args.n):
        print('m')
    # Now let's call meows.py -h and see what shows up this time. VOILA!
    '''
    usage: 3_meows.py [-h] [-n N]

    Meow like a cat

    options:
    -h, --help  show this help message and exit
    -n N        number of times to meow
    '''
    # Here in '-n N' the capital N means It is advised to type in a number after -n to see the effects.
    # It would be nice tho, if my program still didn't break when I run it without any argv s.
    # For that we can specify a default value 1 for -n with the default keyword inside the add_argument() method and we can further specify that it is an int or it will will break our range() function Xb and then I don't need to do the conversion manually inside range() either[by the way, order doesn't matter!].
    # These are the value of a library, this let's us do everything for us[for me, Im still need to see how everything is happening inside the class .py files].
# It is important to note that if we input for example, dog after -n we will get an error message :'()
# Let's excercise unpacking in the new way and terminal code 4_unpack.py
