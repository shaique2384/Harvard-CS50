# Libraries are gnerally files of codes that other people r you have written and can use in another program. They are used to save time and effort by reusing code that has already been written and tested.
# To use a library, you need to import it into your program. You can do this using the import statement. For example, if you want to use the math library, you can import it like this:
# This is anability of sharing codes across codes, these are called modulese. A module is a file that contains Python code. A library is a collection of modules. When you import a library, you are importing all the modules in that library.
# Modules encourage sharability and reusability of code. They allow you to organize your code into logical sections and make it easier to maintain and debug. By using modules, you can also avoid naming conflicts and keep your code clean and organized.
# To import a module, you can use the import statement followed by the name of the module
# For example, if you want to use the math module, you can import it like this:
# We don't have to keep copying and pasting code from one program to another, we can just import the module and use the functions and variables defined in that module. This makes our code more efficient and easier to maintain.
# You can also import specific functions or variables from a module using the from keyword. For example
# This will import only the sqrt function from the math module, and you can use it directly without having to prefix it with math.
# You can also give a module an alias using the as keyword. This can be useful if
# It's Like creating an object in max msp, you can give it a name and then use that name to refer to the object. In the same way, you can give a module an alias and then use that alias to refer to the module. For example:
# This will import the math module and give it the alias m. You can then use m
# to refer to the math module in your code. For example, you can use m.sqrt(16) to calculate the square root of 16 using the math module.
# We can put it into a library that we can load into any program we want. This is a great way to reuse code and save time. For example, if we have a function that calculates the area of a circle, we can put it in a library and then import that library into any program that needs to calculate the area of a circle. This way, we don't have to rewrite the function every time we need it, we can just import the library and use the function.
# To create a library, you can simply create a new Python file and define your functions.
# Python comes with a random library that contains functions for generating random numbers.
# Modules gives us functions that we don't have access to by default like print and import. These are work functions but sometimes functions are tucked away in the modules so you have to be more deliberate about loading them carefully. You can also create your own modules and libraries to share your code with others or to reuse it in different projects. This is a great way to save time and effort by reusing code that has already been written and tested.
# To create a module, you can simply create a new Python file and define your functions in that file. For example, you could create a file called my_module.py and define a function called greet in that file like this:
# Then, you can import that module into another Python file and use the greet function like this:
# This will import the my_module and call the greet function, which will print "Hello,
# When we install python there is also a file that random.py . That is to say how to flip a coin or get a random number from 1 to 10 in python. Well you  need a bit of randomness in your code, you can use the random library. To use the random library, you need to import it into your program. 
# We could figure out mathmatically how to write funtions like that by ourselves it's a lot easier to stand on the shoulders of others who have already solved that problem and we can focus on the problems that we want to solve.
# docs.python.org/3/library/random.html is where the documentation for that specific module lives and we can see a list of modules that are available in the random library and how to use them. For example, if we want to generate a random number between 1 and 10, we can use the randint function from the random library like this:
# The import keyword lets us import the contents of, the functions from some modules into python. This is a powerful feature that allows us to reuse code that has already been written and tested, and it also allows us to access a wide range of functions and tools that are available in the Python ecosystem. By importing modules, we can save time and effort by not having to write everything from scratch, and we can also take advantage of the work that others have done to solve common problems.
# Let's import random.choice(seq) to randomly select an item from a list. For example, if we have a list of colors, we can use random.choice to randomly select a color from that list like this:

if False:
    import random
    colors = ['red', 'blue', 'green', 'yellow']                 # This is AI program from copilot
    random_color = random.choice(colors)

    print(random_color)

# Let's generate a program that simulates flipping a coin. 50% Probability of everything. We can use the random library to generate a random number between 0 and 1, and then use that number to determine whether the coin flip is heads or tails. For example:
if False:
    import random

    flippen_coin = random.choice(["heads", "tails"])                                                 # The choice function from random takes in a list or list like dataset into the parentheses. According to documentation the list takes a sequence. Choice chooses one of the problems randomly with equal probability.
    print(flippen_coin)

# if we can flip the coin infinite amount of time it will be 50 50!
# Downside of random is we have to type it everytime we use it.
# An alternative is the use of KW from, it allows us to be a little more specific. For example let's tweak the same function,
# It loads the function named choice into our name space, into the scope of the file we are working in.
# I know longer have to specify which choice function I mean, I can just say choice. So it loads it into my local namespace, my local vocabulary if you will, so now I can just choice. 

if False:
    from random import choice

    flippen_coin = choice(["heads", "tails"])                                                 # The choice function from random takes in a list or list like dataset into the parentheses. According to documentation the list takes a sequence. Choice chooses one of the problems randomly with equal probability.
    print(flippen_coin)

# But it is such a short program or equivalently may be I'm using the choice function in so many places calling random.choice is adding that many extra words, so bleep! looooong code!
# From lets us keep the choice function under the scope of the random file or module . This is useful because we may introduce our own cutom function named choice and we don't want it coliide with the choice function of random module.
# Python let's us scope the functions to each of the modules so to speak
# let's work with "random.radint(a,b)" it means get back a random intenger between a and b inclusive each with a 1/(b-a+1) probability.
# Let's pick a random number between 1 and 10

if False:
    import random

    number = random.randint(1, 10)
    print(number)                               # 10% probability each


if False:
    from random import randint

    a = int(input("What is the starting number? "))
    b = int(input("What is the ending number? "))
    for _ in range(b-a+1):
        print(randint(a,b))

# another function is "random.shuffle(x)" it takes a list of values and shuffle them

if False:
    import random

    cards = ["jack", "queen", "king"]               # It shuffles the arguments in place. Usually array like data structures are passed by reference, so the shuffle function is gonna change the order of the cards in the original list. It doesn't return a new list, it just shuffles the original list. So we don't need to assign it to a new variable, we can just call random.shuffle(cards) and it will shuffle the cards in place.
    random.shuffle(cards)
    # print(cards)
    for card in cards:
        print(card)

# Code by ramin raja

if False:
    import random 

    card = ["jack","queen","king","apple"]

    print(card)
    def shuffle(x):
        size = len(x)
        new_list = []
        done = []
        while True:
            if len(done) == size:
                return new_list
            else:
                l = random.randint(0,size-1)
                if l not in done:
                    new_list.append(x[l])
                    done.append(l)
    print(shuffle(card))

# Python caomes with a statistics library. It let's us do things of statical nature
# Let's work on average function

if False:
    import statistics

    print(statistics.mean([100, 90]))

# command-line arguments, like other languages a feature in python that allows us to provide input not when prompted inside the program but rather allows to provide arguments that is input to the program just when we are executing at the command-line
# Let's understand through example, let's open a module called sys
# It contains all the funcions that are specific to system files
# The documentation shows "sys.argv" it's called argument vectors, a fancy way describing a list of all words humans typed in during prompting the program before they hit enter all of those are seemingly magically provided to you via python in a variable called sys.argv 
# This variable is gonna be a list of the words that you typed in correct order 
# By weighing this list then you can figure out what words humans have typed in during the program and and may be use that to influence the behavior of your own program
# For example we will not use any input. Anything we type in after python 7_libraries.py will taken as input

if False:
    import sys

    print("Calling from file: ", sys.argv[0], sep='')             # Print hello, my name is followed by whatever is in the sys.argv i.e, whatever we type in in the terminal along with python 7_libraries.py

    # What is the very first element i.e, argv[0], it is exactly what we type after python. We typed "7_libraries.py" the name of our program

    import sys

    print("hello, my name is", sys.argv[2], sys.argv[2])             # Print hello, my name is followed by whatever is in the sys.argv i.e, whatever we type in in the terminal along with python 7_libraries.py

# If we don't type two words after the name of the file we will get an index error "list index out of range"

if False:
    import sys

    try:
        print("hello, my name is", sys.argv[1], sys.argv[2])
    except IndexError:
        print("Nothing was typed in after the name of the file, please type in your name after the name of the file when you run the program")

# We don't need loops because we are trying the program to print name using the input at the command line. We want to get rid of IndexError by this instance.
# I don't need to use try blocks instead I can get a bit more defensive. Let's use a conditional here.

if False:
    import sys

    # Check for errors
    if len(sys.argv) < 3:
        print("Too few arguments.")
    elif len(sys.argv) > 3:
        print("Too many arguments.")

    # Print name tags
    else:
        print("hello, my name is", sys.argv[1], sys.argv[2])

# If you are a coockie monster like david and forget to terminate a string literal with a closing quote, you will get a syntax error. 
# If you forget to put a closing parenthesis, you will also get a syntax error. 
# If you forget to import a library that you are using in your code, you will get a name error. 
# If you try to access an index that is out of range in a list, you will get an index error. 
# If you try to divide by zero, you will get a zero division error. 
# If you try to use a variable that has not been defined, you will get a name error. 
# If you try to use a function that has not been defined, you will get a name error. 
# If you try to use a module that has not been imported, you will get a name error. 
# If you try to use a function from a module that has not been imported, you will get a name error. 
# If you try to use a function from a module that has been imported but not loaded into the local namespace, you will get a name error. 
# If you try to use a function from a module that has been imported and loaded into the local namespace but is not defined in the module, you will get an attribute error. 
# If you try to use a function from a module that has been imported and loaded into the local namespace but is not callable, you will get a type error. 
# If you try to use a function from a module that has been imported and loaded into the local namespace but is not defined in the module and is not callable, you will get an attribute error. 
# If you try to use a function from a module that has been imported and loaded into the local namespace but is not defined in the module and is not callable and is not an attribute of the module, you will get an attribute error.

# How argv works is that each words point out specific location of the list, but if I add quote after name of the python file at the command line import sys will consider them as one word and it will be the first element of the list, so it will be sys.argv[0] and then the name of the file will be sys.argv[1] and then the name that I typed in will be sys.argv[2]. So if I type in "python 7_libraries.py "hello world" ramin" then sys.argv[0] will be "hello world", sys.argv[1] will be "7_libraries.py" and sys.argv[2] will be "ramin". So if I want to print hello, my name is followed by whatever is in the sys.argv i.e, whatever we type in in the terminal along with python 7_libraries.py then I can use sys.argv[2] to get the name that I typed in.

# If we get rid of the else then it will flag us with print side effects "Too few or too many arguments" as well as give us an IndexError for final print as well.
if False:
    import sys

    # Check for errors
    if len(sys.argv) < 3:
        print("Too few arguments.")
    elif len(sys.argv) > 3:
        print("Too many arguments.")

    # Print name tags
    print("hello, my name is", sys.argv[1], sys.argv[2])

# There is a solution for that by terminating the code prematurely at that point and not going upto the final print statement if we have too few or too many arguments. We can use the sys.exit() function to terminate the program immediately. For example:
# sys.exit() will terminate the program immediately and return a status code of 0 to the operating system, which indicates that the program has completed successfully. You can also provide a non-zero status code to indicate that the program has encountered an error. For example, sys.exit(1) will terminate the program and return a status code of 1 to the operating system, which indicates that the program has encountered an error. By using sys.exit(), you can ensure that your program does not continue to execute after encountering an error or invalid input, which can help prevent further issues and improve the overall robustness of your code.
# The arguments in the parenthesis will return a status code and show as a side effect like the printing function while terminating the program.

if False:
    import sys

    # Check for errors
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments.")

    # Print name tags
    print("hello, my name is", sys.argv[1], sys.argv[2])

# Now we have access to all of the functions in the sys module, we can use them to do things like exit the program or print the arguments that were passed in at the command line. By importing the sys module, we have access to a wide range of functions that can help us interact with the system and manage our program's behavior.
# This time I don't wanna limit the number of arguments to 3, I want to be able to print as many names as I want. So I can use a loop to iterate through the arguments and print them out. For example:
# We will use a for loop to iterate through the arguments in sys.argv and print them out. We will start the loop from index 1 to skip the name of the file, and we will print each argument followed by a space. This way, we can print as many names as we want without getting an index error.

if False:
    import sys

    # Check for errors
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.")

    # Print name tags
    for arg in sys.argv[1:]:                        # Slice is a subset of a data structure like a list. In python we can take a slice of a list by using the colon operator. sys.argv[1:] means take all the elements of the list starting from index 1 to the end of the list. This way, we can iterate through all the arguments that were passed in at the command line, regardless of how many there are. The numbers close to the right bracketof the list is exclusive, so sys.argv[1:5] means take the elements from index 1 to index 4, but not index 5. This way, we can print the first four arguments that were passed in at the command line, and if there are more than four arguments, we will ignore them. This is a way to limit the number of arguments that we print without getting an index error. But if we don't use any number with the closing bracket then it will take all the elements from index 1 to the end of the list, which is what we want in this case.
        print("hello, my name is", arg)                                  # By default it will print with end="\n" which means it will print each argument on a new line. If we want to print them all on the same line, we can use end=" " to specify that we want to print a space after each argument instead of a new line. For example, print(arg, end=" ") will print all the arguments on the same line separated by a space. This way, we can print as many names as we want without getting an index error and without having to worry about how many arguments were passed in at the command line.

if False:
    import sys

    # Check for errors
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.")

    # Print name tags
    for arg in sys.argv[1:-2]:                        # Adding -2 at the end bracket will cut 2 from the right extreme of the list.
        print("hello, my name is", arg) 

