# DEF
# You can build your own functions
# How to make these functions exist? using def which means define
# The lines underneat def hello(): indented python will treat as the meaning of this new function
# The parenthesis with nothing inside means its not gonna take any inputs
# : means stay tuned for the indentation
# All of the indented code should line up
# Def funcions return in the backend, but we can also use the return keyword to explicitly return a value

if False:
    def hello():
        print("hello")

    name=input("What's your name?  ")
    hello()
    print(name)

if False:
    # Lets mod it more so that it takes input
    # Lets add to inside the parameter, like who do you say hello to?
    # to is like a variable, which makes the defination understand its a port for input values
    def hello(to):
        print("hello,", to)

    name=input("What's your name?  ")
    hello(name)

if True:
    # We can add default values for our new function
    # If there is no input it will print the default value
    def hello(to="world"):
        print("hello,", to)

    hello()
    name=input("What's your name?  ")
    hello(name)

if False:
    # Other way around will not work
    # This way we have to define earlier
    # But direction in messed up
    
    hello()
    name=input("What's your name?  ")
    hello(name)

    def hello(to="world"):
        print("hello,", to)

if False:
    # To keep the freedom of direction we need to define the main part of the code
    # Still nothing, no one is telling python to actually use or call name
    # Call name at the end
    # Let's me organize my code anyway I want
    def main():
        hello()
        name=input("What's your name?  ")
        hello(name)

    def hello(to="world"):
        print("hello,", to)

    main()

if False:
    # Lets make a mistake
    # Lets sabotage to, the variable branch from def hello()
    # name error, name was not define
    # scope refers to a variable only exists in the context in which you defined it i.e, it is defined in main() function
    def main():
        name=input("What's your name?  ")
        hello()

    def hello():
        print("hello,", name)

    main()

if False:
    # main() specifies the parent branch
    # in the context of def hello(to): to shows how a variable can be used in the main context, it's a variable of a variable
    def main():
        name=input("What's your name?  ")
        hello(name)

    def hello(to):
        print("hello,", to)

    main()

# What if I dont want my function to render a side effect per se but hand me a value, a return value
# int function, float function returns a value
# We can use a final keyworkd here to literally return ato return a value to explicitely yourslef
# Lets try one other version in 2_calculator.py