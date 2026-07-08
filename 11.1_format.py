# Let's reformat user's name, not email addresses
# There might be differences in typing names based on referencing or simply typing names one after another
if False:
    name = input("What's your name? "). strip()
    '''print(f'Hello, {name}.')'''
    # David Malan and Malan, David situation will create issues here
    # If the user has already submitted a form online and we have the data which needs to be done cleaned up by effing me
    # let's split the variable name with comma and space if there is this comma backward name situation
    # we can also use ',' and strip() the first variable
    if "," in name:
        last, first = name.split(',')
        name =f'{first.strip()} {last}'
    print(f'Hello, {name}.')
# here we are taking inputs everytime, it can be like this we are reading from a csv file in that case we have to iterate through the lines of one file and write, save into a corrected file
# we can do the same thing using re library

if False:
    import re

    name = input("What's your name? "). strip()
    # the regular expression can also assign to a variable other than just giving boolean signal
    # parentheses in the pattern gives a return value inside the pattern parameter of re.search(), meaning inside the pattern definining procedure there are some returning happening
    # we can use parentheses to not only group things but also to capture them i.e, (?:...) non-capturing version, says we don't want to capture or return thise we are just grouping things
    '''matches = re.search(r'^(.+), ?(.+)$', name)'''
    # using * in stead of ? covers more corner cases
    matches = re.search(r'^(.+), *(.+)$', name)
    # we are just capturing the first and last variables with the (.+)
    # let's still create some boolean. When there is no comma-reverse situation in the input the matches is nothing as nothing matched by the re.search() function. If matches is not nothing,
    if matches:
        '''last, first = matches.groups()'''
        # groups() makes the matches return all the captured arguments grouped. This is the apparatus that makes the boolean machine re.search() to return the value corresponding to the grouped symbols with (...)
        # another way is using group(1), group(2). There is smth else that comes out from the matches.group(0)
        last = matches.group(1)
        first = matches.group(2)
        name = f'{first.capitalize()} {last.capitalize()}'
    print(f'Hello, {name}')

# we can also do this, more concise,
if False:
    import re

    name = input("What's your name? "). strip()
    if matches := re.search(r'^(.+), *(.+)$', name):
        # it's a new feature of python and we use the walrus sign := if and only if it's an assignment and we are asking an if or elif question
        name = matches.group(2) + " " + matches.group(1)
    print(f'Hello, {name}')

# let's try extracting this time and let's terminal code 11.2_twitter.py