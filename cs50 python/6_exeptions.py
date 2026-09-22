# Excepttion is everything that can go wrong
# When something is exceptional in code that doesnt mean it's a good thing
# It's a problem that only I can solve [Syntax error]
# Syntax error is an exception that occurs when the code is not written correctly.
# Syntax error is a compile time error, it occurs when the code is being compiled.
# Runtime error is an exception that occurs when the code is being executed.
# Runtime error is an exception that occurs when the code is being executed.
# Logical error is an exception that occurs when the code is logically incorrect.
# Logical error is an exception that occurs when the code is logically incorrect.
# Exception handling is the process of handling exceptions in a way that does not crash the program.
# Exception handling is the process of handling exceptions in a way that does not crash the program.    
# Try and except block is used to handle exceptions in a way that does not crash the program.
# Try block is used to write the code that may raise an exception.
# Except block is used to write the code that will be executed if an exception is raised.
# Finally block is used to write the code that will be executed regardless of whether an exception is raised or not.
# Raise keyword is used to raise an exception manually.
# Custom exception is an exception that is defined by the user.
# Custom exception is an exception that is defined by the user.

if False:
    x = int(input("How many times did you make a joke today? " ))       # If the user enters a non-integer value, it will raise a ValueError exception. 
    print(f"You made {x} boring jokes today!")                          # ValueError is an exception that occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value.

# Invalid literal for int() with base 10: 'abc' is an example of a ValueError exception that occurs when the user enters a non-integer value.
# Literal is something that is not a variable, it is a value that is directly written in the code. For example, 10, 'hello', True are literals.
# We can print instructions to guide the user but still the user may not follow.
# We need to write our code with error handling in mind.

# If we want to catch a value error or any other kind of errors except syntax error, we can literallyuse try[keyword] and except[keyword] block.
# At this point are just trying.

if False:
    while True:
        try:        
            x = int(input("How many times did you make a joke today? " ))   # The code we are trying has to be under try block, if we write it outside the try block it will not work. If it's before try block the valueerror exception will not wor.
            print(f"You made {x} boring jokes today!")
            break  
        except ValueError:                                                  # This symbol is case sensitive, capital V and capital E, if we write valueerror or Valueerror it will not work.
            print("Please be a little unicorn and enter a friggin number this time numpty!")

# Figure out what kind of error could happen and try out to check.
# Documentation does not spell out what could go wrong, you have to figure it out by yourself.

if False:
    while True:
        try:        
            x = int(input("How many times did you make a joke today? " ))
            break  
        except ValueError:                                                  
            print("Please be a little unicorn and enter a friggin number this time numpty! (0 included)")
    print(f"You made {x} boring jokes today!")                              # Only  try the part of the code you suspect might raise an exception, not the whole code. If we put the print statement inside the try block, it will not work because if the user enters a non-integer value, it will raise a ValueError exception and the print statement will not be executed. By putting the print statement outside the try block, it will be executed regardless of whether an exception is raised or not.

# Exceptions are corner cases.
# Value error is an error introduced by the user and NameError is an error introduced by the programmer.
# For Example, if we write print(x) without defining x, it will raise a NameError exception because x is not defined. NameError is an exception that occurs when a local or global name is not found. It is raised when the variable is not defined.

if False:
    try:        
        x = int(input("How many times did you make a joke today? " ))       # The location of the value error.
    except ValueError:                                                  
        print("Please be a little unicorn and enter a friggin number this time numpty! (0 included)")
    print(f"You made {x} boring jokes today!")                              # Here print is not in the try block, so if the user enters a non-integer value, it will raise a ValueError exception and the print statement will be executed, but it will raise a NameError exception because x is not defined. To avoid this, we can define x before the try block.

# Scope of variables is important when we are handling exceptions. If we define a variable inside the try block, it will not be accessible outside the try block if an exception is raised. To avoid this, we can define the variable before the try block.
# Local variable is a variable that is defined inside a function and can only be accessed inside that function. Global variable is a variable that is defined outside a function and can be accessed anywhere in the code. If we define a variable inside the try block, it will be a local variable and if an exception is raised, it will not be accessible outside the try block. To avoid this, we can define the variable before the try block, so it will be a global variable and can be accessed anywhere in the code.
# Also here, int() function is getting a value error and hence the line in issue is situated inside the try block.
# According to David we can use else block. But it is under conditional.

if False:
    try:        
        x = int(input("How many times did you make a joke today? " ))       
    except ValueError:                                                  
        print("Please be a little unicorn and enter a friggin number this time numpty! (0 included)")
    else:
        print(f"You made {x} boring jokes today!")

# The dirrection is now a tree and else is a contrast to except block as opposed to try block[comparing with the conditional relationships between if, elif, else blocks].
# Try is the friend of else.

if False:
    while True:
        try:        
            x = int(input("How many times did you make a joke today? " ))       
        except ValueError:                                                  
            print("Please be a little unicorn and enter a friggin number this time numpty! (0 included)")
        else:
            break   
    print(f"You made {x} boring jokes today!")

# The else clause is associated with the try block and not with the except block.
# Also break is used to exit any loop function.
# Could we also use break in the try block? It is not recommended because if an exception is raised, it will not be executed and the loop will not be exited. It is better to use break in the else block because it will only be executed if no exception is raised.
# Let's make our custom function.

if False:
    def main():
        gormet = get_int_for_boring_jokes_count()                                      # gormet just popped up in my head out of nowhere, it actually comes from Gourmet which means a person who enjoys fine food and drink, but here it is just a variable name that I chose randomly. It has no meaning in this context.
        print(f"You made {gormet} boring jokes today!")

    def get_int_for_boring_jokes_count():                                              # Now we have a function get_int() that will "try" to do the following. 
        while True:
            try:        
                x = int(input("How many times did you make a joke today? " ))       
            except ValueError:                                                  
                print("Please be a little unicorn and enter a friggin number this time, numpty! (0 included)", "\n", sep="", end="I'M ASKING AGAIN! ")
            else:
                break   
        return x                                              # When you are inventing your own function the purpose of whose life is not just to print something as a side effect but to hand back a value that has been inputed we have to return the value of the variable explicitly.

    main()

# Can we improve upon it?

if False:
    def main():
        gormet = get_int_for_boring_jokes_count()                                      
        print(f"You made {gormet} boring jokes today!")

    def get_int_for_boring_jokes_count():                                              
            while True:
                try:        
                    x = int(input("How many times did you make a joke today? " ))       
                except ValueError:                                                  
                    print("Please be a little unicorn and enter a friggin number this time, numpty! (0 included)", "\n", sep="", end="I'M ASKING AGAIN! ")
                else:
                    return x                                                               # return is break as well as return.
                                                    
    main()

# We can also use break and return in the try block.

if False:
    def main():
        gormet = get_int_for_boring_jokes_count()                                      
        print(f"You made {gormet} boring jokes today!")

    def get_int_for_boring_jokes_count():                                              
            while True:
                try:        
                    x = int(input("How many times did you make a joke today? " ))
                    return x       
                except ValueError:                                                  
                    print("Please be a little unicorn and enter a friggin number this time, numpty! (0 included)", "\n", sep="", end="I'M ASKING AGAIN! ")
                                                                                                                                  
    main()

# We can just return the value of x and that would be the function of our custom function get_int_for_boring_jokes_count() and we can also use break in the try block but it is not recommended because if an exception is raised, it will not be executed and the loop will not be exited. It is better to use return in the try block because it will only be executed if no exception is raised.

if False:
    def main():
        x = get_int_for_boring_jokes_count()                                      
        print(f"You made {x} boring jokes today!")

    def get_int_for_boring_jokes_count():                                              
            while True:
                try:        
                    return int(input("How many times did you make a joke today? " )) 
                except ValueError:                                                  
                    print("Please be a little unicorn and enter a friggin number this time, numpty! (0 included)", "\n", sep="", end="I'M ASKING AGAIN! ")                                                                                                                                  
    main()

# Now let's talk about pass statement. Pass statement is used when we want to write a block of code that does nothing. It is a null statement that is used as a placeholder for future code. It is used when we want to write a block of code that does nothing but we want to avoid syntax error. For example, if we want to write an empty function, we can use pass statement.
# We can also use pass statement in the except block when we want to ignore the exception and do nothing. For example, if we want to ignore the ValueError exception, we can use pass statement in the except block. But it is not recommended because it will hide the error and make it difficult to debug the code. It is better to handle the exception properly instead of ignoring it.

if False:
    def main():
        x = get_int_for_boring_jokes_count()                                      
        print(f"You made {x} boring jokes today!")

    def get_int_for_boring_jokes_count():                                              
            while True:
                try:        
                    return int(input("How many times did you make a joke today? [Enter a number] " )) 
                except ValueError:                                                  
                    pass                                                                                                                                  
    main()

# Indentation in python is deliberate logically. Anytime you write a line of code and indent the next line then it means the next line is somehow associated to the previous line. In the above code, the except block is associated with the try block and the pass statement is associated with the except block. It means that if a ValueError exception is raised, it will be caught by the except block and the pass statement will be executed, which means that nothing will happen and the loop will continue to execute until a valid input is entered.
# It's like the group and subgroups of tracks in reaper. The try block is the main track and the except block is the subgroup of the try block and the pass statement is the subgroup of the except block. If an exception is raised in the try block, it will be caught by the except block and the pass statement will be executed, which means that nothing will happen and the loop will continue to execute until a valid input is entered.
# For pass the user is not gonna know about it, that is the whole point of pass statement, it is used to hide the error and make the code look cleaner. It is not recommended to use pass statement in the except block because it will hide the error and make it difficult to debug the code. It is better to handle the exception properly instead of ignoring it.
# Other languages focus more on if, elif else etc over and over again, but in python it's more like try it but make sure you are handling the error properly.
# One final tightening up, let's not type x over and over over again. The caller is main() and the callee is get_int_for_boring_jokes_count() and the value that is being returned by the callee is being assigned to x in the caller. So we can just return the value of x directly without assigning it to a variable in the caller. The caller does not have to know all the nooks and corners of the callee variables.
# To call a function means is to use it, the caller is the function that is using it. The callee is simply the function being called.
# Let's try to use the braces inside our get_int_for_boring_jokes_count().
# We can just move the string input "How many times did you make a joke today? [Enter a number] " into the variable of the def main() block and use any variable inside the def callee braces. It is not recommended to use global variables because it can lead to unexpected behavior and make the code difficult to debug. It is better to pass the string input as an argument to the get_int_for_boring_jokes_count() function.

if True:
    def main():
        x = get_int_for_boring_jokes_count("How many times did you make a joke today? [Enter a number] ")                                      
        print(f"You made {x} boring jokes today!")

    def get_int_for_boring_jokes_count(prompt):                                              
            while True:
                try:        
                    return int(input(prompt)) 
                except ValueError:                                                  
                    pass                                                                                                                                  
    main()

# This way we don't have to come back to the callee function details and we can just use the main function.
# Thus we can use more reusable modular code.
#
# We can also raise exceptions ourselves using the raise keyword. For example, if we want to raise a ValueError exception when the user enters a negative number, we can use the raise keyword in the get_int_for_boring_jokes_count() function.
