# Another type of argument is integer, int
# % modulus, it gives remainder
# python has interactive mode, dont have to run cli everytime rather you can run it on cli
# You can add randomly in cli
# lets make a calculator

if False:
    print(1+1)

if False:
    # lets make a calculator
    x=input("What's x? ")
    y=input("What's y? ")
    z=x+y
    print(z)
    # wont work cause numbers are input as str 

if False:
    # int function converts str to intezers
    x=input("What's x? ")
    y=input("What's y? ")
    z=int(x)+int(y)
    print(z)

if False:
    # nesting function is like simplification in mathematics
    x=int(input("What's x? "))
    y=int(input("What's y? "))
    print(x+y)

if False:
    # nesting ultra! Too Complicated, balance is broken. 
    # You are making me think too much, waste of time, more susceptible to error, not readable.
    # That can be a good quality as well ;)
    print(int(input("What's x? "))+int(input("What's y? ")))

# In oppose to int, float is a number with decimal point, exists in the set of real numbers, R

if False:
    # Float lets us add decimal points, or floating point values
    # Round is a built in function 
    # round(number[, ndigits])
    # no aesterisks so not infinit numbers can be passed through, [] means optional, ndigits lets us specify roundof difit number
    x=float(input("What's x? "))
    y=float(input("What's y? "))
    print(round(x+y))

if False:
    # Another built in function to add commas in large numbers using f srtings
    x=float(input("What's x? "))
    y=float(input("What's y? "))
    z=round(x+y)
    print(f"{z:,}")

if False:
    # Division
    # In python int can be as big as it goes
    # In python floating pont value is limites
    # For rounding ndigits dont use [], these are to mean optional, just use comma after the argument inside the round() function
    x=float(input("What's x? "))
    y=float(input("What's y? "))
    z=round(x/y, 2)
    print(z)

if False:
    # For ndigits you can also use formatt function with z:.2f
    x=float(input("What's x? "))
    y=float(input("What's y? "))
    z=x/y
    print(f"{z:.2f}")

# Coming from 3_def_function.py
# Implementing return utility of def function
if False:
    def main():
        x=int(input("What is x? "))
        print("x square is", square(x))
    
    # We will call generically n any old number
    # We then have to return n*n to main()
    def square(n):
        return n*n
    main()

# Additional vocabulary pow(n, n) function
# Again implementing return utility of def function
if True:
    def main():
        x=int(input("What is x? "))
        print("x square is", square(x))
    
    # In pow(n,n), a built in python function 
    # The first digit is the input second one is the exponential
    def square(n):
        return pow(n,2)
    main()
    