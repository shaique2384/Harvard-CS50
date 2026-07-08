# PARITY, about pairs
# We can use the modulus operator to determine if a number is even or odd
# The modulus operator gives us the remainder after division
# % is the modulus function
# Is this number even or odd, its a building block

if False:
    x=int(input("What's x? "))
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

if False:
    def main():
        x=int(input("What's x? "))
        # Let's think of a magical function is_even
        if is_even(x):
            print("Even")
        else:
            print("Odd")
    def is_even(n):
        if n % 2 == 0:
            return True # We are returning boolean expression true or false, like a trigger
        else:
            return False
    main()

# Everything we pass on python is an object unlike java and c++



if False:
    trigger = bool(input("Give me a number "))
    if trigger:
        print("Kaboom!")
    else:
        print("Phew!")

if False:
    def main():
        x=int(input("What's x? "))
        # Let's think of a magical function is_even
        if is_even(x):
            print("Even")
        else:
            print("Odd")
    def is_even(n):
        return True if n % 2 == 0 else False 
        # We can use the ternary operator to return true or false based on the condition, its a one line if else statement
    main()

if False:
    def main():
        x = int(input("What is x? "))
        if is_even(x):
            print("Even")
        else:
            print("Odd")

    def is_even(n):
        return n % 2 == 0 
    # We can just return the boolean expression directly, no need for if else statement
    # The expression n % 2 == 0 will evaluate to True if n is even and False if n is odd, so we can return it directly without needing to use an if statement to check the condition.
    # Even more concise, we can use the ternary operator to return true or false based on the condition, its a one line if else statement
    main()