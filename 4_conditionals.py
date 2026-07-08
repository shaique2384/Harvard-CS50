# CONDITIONALS: COMPARE
# Asking mathmatical questions and get answers logically
# > Gtreater than; >= Greater than or equal to; < Less than; <= Less than or equal to; == equality where one is assignment the other equality; != not equal to

if False:
    # We need a keyword, if to answere questions
    x=int(input("What's x? "))
    y=int(input("What's y? "))
    # We will unleash a booean expression named after Mathmatician Bool
    # Simply a question that has a yes - no answere or true - false answere
    # Line 11 should only be executed "if" line 4's question is in fact true
    if x<y:
        print("x is less than y")
    if x>y:
        print("x is greater than y")
    if x==y:
        print("x equals to y")
    # There is a control of flow from top to bottom
    # So order matters, it's an algorythm

if False:
    # We need another keyword, elif to stop repeating mutually inclusive answeres
    x=int(input("What's x? "))
    y=int(input("What's y? "))

    if x<y:
        print("x is less than y")
    elif x>y:
        print("x is greater than y")
    elif x==y:
        print("x is equal to y")
    # There is still a control of flow from top to bottom
    # If first is true we go directly to side effect

if False:
    # We need another keyword, elif to stop repeating mutually inclusive answeres
    x=int(input("What's x? "))
    y=int(input("What's y? "))

    if x<y:
        print("x is less than y")
    elif x>y:
        print("x is greater than y")
    else:
        print("x is equal to y")
    # If first two scenarios are false the last scenario can't be false
    # That's why we use else

if False:
    # Let's introduce or
    x=int(input("What's x? "))
    y=int(input("What's y? "))
    
    # "Or" and "and" are set maths languages
    if x<y or x>y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

if False:
    # Simplest
    x=int(input("What's x? "))
    y=int(input("What's y? "))

    if x!=y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

if True:
    # Simplest opposit order
    x=int(input("What's x? "))
    y=int(input("What's y? "))

    if x==y:
        print("x is equal to y")
    else:
        print("x is not equal to y")

# For python indentation and collons are necessary else it won't work