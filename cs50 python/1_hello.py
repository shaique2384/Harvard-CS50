# FUNCTIONS; ARGUMENTS[STRINGS]; VARIABLES; PARAMETERS

if False:
    # Computer understands 0s and 1s
    # Program that lets computer understand the command in a more comprehensive way
    # Python is a program like that, program, an interprter installed in a server or pc and 
    # we can run that interpreter which passes through the inputs, reading 
    # from top to bottom left to right and translates into those 0s and 1s the computer can understand 
    print("Hello, World!")

if False:
    # Ask user for their name
    # Variables are functions with returning values
    # They connect the input with the output, here we are connecting the name input with the print output
    # = is an assignment operator. Its not equality operator, it assigns the value on the right to the variable on the left.
    name = input("What's your name? ")
    print("Hello,")
    print(name)

if False:
    # Concatenation: joining two strings together
    # + operator joins two strings together, as if it is a big argument
    name = input("What's your name? ")
    print("Hello,"+name)

if False:
    # Print takes multiple arguments separated by commas. 2, 3, 4 arguments etc
    name = input("What's your name? ")
    print("Hello,",name)
    # Comma automatically adds a space between the arguments
    # So its better to use comma than concatenation

if False:
    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=false)
    # end parameter of print function
    # By default, print function ends with a new line character \n
    # We can change that behaviour by changing the end parameter; e.g., end=''
    # We can also add end='???', anything that would overrride '\n'
    name = input("What's your \"name?\" ")
    print("Hello, ", end='?!')
    print(name)

if False:
    # A relatively new feature of python where we can formate strings in a special way is called f str
    # Yet another way to solve the same problem
    name = input("What's your \"name?\" ")
    print(f"Hello, {name}")
    

if False:
    # Strings datatype themselves comes with a lot of built in functionality  
    # We can manipulate user inputs and clean it up using these 
    # strip and capitalize are method functions which does exactly this, removes whitespace from the left and right of the str
    name = input("What's your \"name?\" ")
    name = name.strip() # Equal sign assigns from right to left; not in the middle
    name = name.capitalize() # Capitalization
    name = name.title() # Capitalize like title of a book
    print(f"Hello, {name}")

if False:
    # We can stack functions left to right with periods to assign to a variable
    name = input("What's your \"name?\" ").strip().capitalize().title()
    print(f"Hello, {name}")

if True:
    # String is important because the same thing we can do with floats
    # Split breaks the variable into first, last literally
    name = input("What's your \"name?\" ").strip().capitalize().title()
    first, last = name.split()
    print(f"Hello, {last}, {first}")