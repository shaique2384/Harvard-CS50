# match 
# We can use the match statement to match a value against a pattern
# It's like a switch statement in other languages, but more powerful    
# We can use it to match a value against a pattern, and execute code based on the match
# We can use it to match a value against a pattern, and execute code based on the match
# We can use it to match a value against a pattern, and execute code based on the 
# match statement is a new feature in python 3.10, so we need to use python 3.10 or higher to use it
# house code will prompt the user for a name and will assignn them to a house

from os import name


if False:
    name = input("What's your name? ")

    if name == "Harry":
        print("Gryffindor") 
    elif name == "Hermione":
        print("Gryffindor") 
    elif name == "Ron":
        print("Gryffindor") 
    elif name == "Draco":
        print("Slytherin")  
    else:
        print("Who?")


if False:
    name = input("What's your name? ")

    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Gryffindor")  
    elif name == "Draco":
        print("Slytherin")  
    else:
        print("Who?")
    # if more names are added to the same house we can use "or" to check for multiple names in the same house
    # the line will get unrealistically long if we have more names in the same house

if True:
    name = input("What's your name? ")

    match name:
        case "Harry":
            print("Gryffindor") 
        case "Hermione":
            print("Gryffindor") 
        case "Ron":
            print("Gryffindor") 
        case "Draco":
            print("Slytherin")  
        case _:
            print("Who?")
    # match statement is a new feature in python 3.10, so we need to use python 3.10 or higher to use it
    # the match statement is more powerful than if statements because it can match patterns and not just values


if True:
    name = input("What's your name? ")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")  
        case "Draco":
            print("Slytherin")  
        case _:
            print("Who?")
    # we can use the "|" operator to match multiple values in the same case, it's like "or" in if statements but more concise and easier to read
    # the match statement is more powerful than if statements because it can match patterns and not just values
    # SAME AS IF STATEMENT BUT MORE CONCISE AND EASIER TO READ