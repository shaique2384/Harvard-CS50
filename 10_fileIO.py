# Up untill now all the programs we have written that just stores all the information it stores in the memory, that is inside variables.
# Downside of that is anything that we typed it inside that program is lost, for example the side effects in th terminal
# With file utility we can store our programs inside a file that we can save and read from later
# So File I/O within the context of programming is all about writing a code that can read from i.e, load information from or write to that is save information to files themselves.
# Lets see if we can transition them from only using memory, variables and likes to actually writing codes that save files for us and therefore data persistently
# Using list we are able to store more than one piece of information in the past compares to variables
# But the lists also dies when we close the program bcause it also stays in the memory
# Let's write a program that only collects people's names

if False:
    names = []                                                  # This means give me an empty list

    for _ in range(3):
        name = input("What's your name? ")
        names.append(name)                                      # It is names.apppend to our list, it means append the name inputs in our empty list, like the coll object in max
    print(f"hello, {name}")
    # Now lets write at top names plural with an empty list, very similar to max msp
    # Now lets iterate through range(3) the name variable which also have an input functionality

# We can make it even consise without creating complexity, and a very short line. Readable

if False:
    names = []                                                  # This means give me an empty list
    for _ in range(3):
        names.append(input("What's your name? "))               # Exactly like that cycling project, where there was this empty message at top!
    # Now let's sort them alphabetically so that it makes sense to gathering them altogether then sorting them and printing them
    # To sort lists in python there is a function called sorted(). It is used in for name in names: loops
    print(names)
    print(sorted(names))                                        # Sorted just sort strings alphabetically
    for name in sorted(names):                                  # We are actually going backwords, we are collecting our input names in a vessel or list called [] empty list. names is modified because of appending inputes while iterating _ through range(3) which means 3 repeatation of the funvtion input and storing as well as updating in the names empty list
        print(f"helo, {name}")                                  # So here we are taking the list and doing what we've done before that is printing while iterating thoough names while printing the fstr with each name variable. This time we have just created empty set stored data and sorted alphabetically

# By the way all names are lost, we haven't effectively utilized the coll object yet
# How to save this information somehow instead, that's how file I/O comes in
# How can we save them ina file

if False:
    name = input("What's your name? ")
    # There is a function in python which is called open whose purpose in life is to do exactly that. To use it programmatically so that we the programmers can actually read from or write to it
    # So open is like a programmer's equivalent of double clicking on an icon from pc. 
    # It let's us specify what to read from or write to, follow the documentation https://docs.python.org/3/library/functions.html#open 
    # Usage is relatively straight forward, requirs the name of the file we want to open it and how we want to open it
    ''' open("names.txt", "w") '''                                          # It is a call to open the file name.txt and w for writing priviledges
    # Open returns a file handle, a special value that lets me to access that file. Let's assign it to file so open on the left of assignment symbol =
    '''file = open("names.txt", "w")'''
    file = open("names.txt", "a")                                           # A gives us write and add hence "a"
    file.write(name)                                                        # Let's link write() function to the variable file and put name variable inside file. It is a function that comes with function open
    file.close()                                                            # It will just eeffectively close and save the file
# Open names.txt by terminaling code name.txt
# The problem is the file doesn't save previous data everytime I write
# We are not appending, and w is a little dangerous, it rewrites
# Let's remove the text by terminaling rm names.txt and confirm by y
# let's now change w to a in the open function line to append
# Problem is our text is totally rumbled up, so let's use f string insteaf

if False:
    name = input("What's your name? ")
    file = open("names.txt", "a")
    file.write(f"{name}\n")
    file.close()

if False:
    # Thing is we don't have to use close() everytime if we use another aproach which is more pythonic
    # We are introducing another keyword quiet simply called "with" that allows us to specify that in this context I want the program to automatically close afterwords while we are using the open function
    name = input("What's your name? ")
    with open("names.txt", "a") as file:                                            # instead of asigning we are using conditional alike, with .... as file: which kind of means like we are opening some blablas with the condition as a file. That means act like open, write and close-save just like a file.
        file.write(f"{name}\n")                                                     # It has turned into a block and inside this block all the programs will be called in the context of with .... as file: That is the power of with
# Now we are gonna write a code that reads an existing file, for us names.txt. Instead of opening as "a" , [open to write and add] we are going to use "r", [open to read]
if False:
    with open("names.txt", "r") as file:                                            # The return value of open is being withed hahaha as file
        # Let's define a variable called lines, an assign file.readlines() to it
        lines = file.readlines()                                                    # Readlines return a list of strings
    # Now our variable lines have been assigned to a list of strings by the readlines() function over our file
    # Let's iterate through the elements using for loops,
    '''print(lines)'''                                                              # readlines function adds an extra "\n" after already existing '\n's in our file names.txt. So the list looks like this, ['Hermione\n', 'Draco\n', 'Harry\n', 'Ron\\\n'], the "\n"s exist already in our file
    for line in lines:
        '''print("hello,", line, end="")'''                                         # so cut off extra "\n" added by our print funcion 
        # Let's predict what will happen. I think it will have "\n" str at the end by default as it is a print function
        # we can also use rstrip on line to strip out any extra detail in the lines list elements and we will get normal new lines frop the print function
        print("hello,", line.rstrip())                                              # The rstrip() method is a built-in Python string function that returns a copy of the string with trailing characters removed from the right side of the assignment. braces in the rstrip() mean that it returns a value
# We don't have to create an extra variable for file.readlines() because file itself is a list dataset. So we can iterate through file using line or anything that we are going to add inside the fucntion using the same function.rstrip(). It kinda reads rather like english

if False:
    with open("names.txt", "r") as file:
        for line in file:
            print("hello,", line.rstrip())

    # We already have files in the read mode
    "my name is shaique" # This string is also like a note, weird huh?
    '''
    for _ in file:
        print("hello,", _.rstrip())
    '''
# Let's sort it out, we need to talk
if False:
    with open("names.txt", "r") as file:
        for line in sorted(file):
            print("hello,", line.rstrip())
# Above is what david did later
# To make David happy let's use the idea of empty list first ;)
if False:
    names=[]
    # The above is like let, given, etc from our childhood math
    # this time we are not using the w, a or r mode, we are plainly opening the file 
    with open("names.txt") as file:
        # file is already a list so we can iterate through files then update our empty list into our file, which will be strored while running the program
        # I know we already did the easier part, this is just to review the concepts of empty lists and append functions.
        for line in file:
            names.append(line.rstrip())
            # Here our names list is filled up with data from opened file list. How? By each iteration of our line in the opened file list we are rstrip ing each lines and appending into the line empty list
            # So append is specific method for empty lists. We can use it in max msp patch
        
    # Now we have our list names updated inside the program but will not be saved in the memory as files.
    # Let's iterate and sorted it, [sorted(iterable, /, *, key=Note, reverse=False) ; Reverse takes boolean value here]
    if len(names) <= 4:
        for name in sorted(names, reverse=True):
            '''print("hello,", name)'''
            # We can also use f"str
            '''
            if name == "Harry":
                print(f"hello, {name}")
            '''
            print(f"hello, {name}")
            # This method allows us to have more control over specifics as we have store it in the coll object names=[] here; exactly like our if False: blocks for each example for the control over these large python files which are just my note taking chapters
    else:
            print("Too many names")
            SystemExit

# What if we want to track of other information as well, supposed that we want to store the name of students' house
# Let's not add house names manually, let's add a convention and terminal code names.csv . csv stands for comma separated value and it is a very common convention to store multiple pieces of information that are related in the same file
# Let's add house name manually and instead of new lines let's add comma and we just installed rainbow.
# This is a kind of two dimentional file like the dictionary, row by row we have students but we are also getting columns with comma
# These csv files are used in microsoft xl export and imprting text formates spreadsheet style
# Let's copy our new data into students.csv, let's change our code to read both kind of datas and we have access to both kind datas instead of just lines

if False:
    with open("students.csv") as file:                          # FILE IS A VARIABLE
        for line in file:                                       # file here represents a list dataset of lines from our file that we have opened                                   
            # here in our loop we are just going to get access of the whole line of text, how to specify
            # We can not use key and value, let's use a split function using that comma
            # split lets us split using any string symbol
            row=line.rstrip().split(",")
            # This is what we are doing in each iteration, we are r stripping the lines and splitting using the comma symbol but what are we getting? [any "str" symbol that we put inside the braces of split is going to split the line with into set of characters into elements of a list which is row at this point]
            # if we didn't use splt() here we would get a list of characters from each lines where row[0] would have been H and row[1] would have been e
            # But how do we collect each arguments? The thing is split is going to give us another list of elements separated by the comma in each line   
            print(f"hello, {row[0]}! You are in {row[1]} house!")
            '''
            print(row)
            for letter in row:
                print(letter)
                print(f"hello, {letter[0]}! You are in {letter[1]} house!")
        '''
# Here we have a program that purses the contents of a comma separated value file into lists and we can identify with each iterated with indexes inside square braces
# If we want to automate the modification of the files we need to write code blocks to write as well somewhere convenient for the design
# Let's clean up our above code, when we have a variable that's a list like row we don't have to through all of these variables into a list we can actually unpack that whole sequence at once
# if we know we have two values separated by commas in each iterable row we can use name, house = lines.rstrip().split(",")
# It's a good pythonic shortcut technique to assign variables like keywords for the elements by keywords outside the list.
# So are we creating a dictionary by that process?
if False:
    with open('students.csv') as file:
        for line in sorted(file):
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house} house")
# let's sort this time the f"str" appending into an empty list wizards using iteration
if False:
    infos=[]
    with open('students.csv') as file:
        for line in sorted(file):
            name, house = line.rstrip().split(",")
            infos.append(f"{name} is in {house} house")
    for info in sorted(infos):
        print(info)
# But can we sort by students' names? probably gotta use dictionary? Let's create a dictionary that stores name, house
if False:
    students=[]
    with open("students.csv") as file:
        for line in file:                                           # This gives us lines in each iteration over the elements of file
            name, house= line.rstrip().split(",")                   # This is where we create lists on every iteration [name, house] and we are using the utility of comma inside the csv file
            student={}                                              # We are bringing another variable which is student, singular of students empty sets. Compare, we haven't appended anything yet. We are assigning an empty dictionary here by assignment symbol
            student["name"] = name                                  # In the student hypothetical dictionary we are coining keyword "name" and assigning name variable to its value! By definition the value of any keyword == dictionary["keyword"]. This assigning of variables into the keyword is same as assigning str arguments to value in each iteration where we are separating the data in each line using split(). So the codes are themselves self explanatory.
            student["house"] = house                                # Same for house, but don't we need to append to the dictionary?
            students.append(student)
    for student in students:
            print(f"{student['name']} is in {student['house']} house")

if False:
    students=[]
    with open("students.csv") as file:
        for line in file:
            name, house= line.rstrip().split(",")
            # we can also define the dictionary by assigning variables and perceive its design more easily
            student={"name": name, "house": house}                                  # same old assignment
            students.append(student)
    # How can we sort now? because we can't do this sorted(students) like before because the iterable elements in students are not sentences anymore, they are dictionaries
    # How to sort dictionaries inside of a list? We can tell the sorted function not just to reverse things but also sort dictionaries using keys!
    # This now is a feature of python, it let us pass in functions like arguments into other functions using def. We don't have to create main() for this because the purpose of this custom function is to return a parameter.
    '''
    A= {"fire":"A", "fire":"B", "fire":"C", "fire":"D"}'''                          # Doesn't work, we gotta use same context of dataset for this instance, students and student. And the keyword must exist there
    
    def get_name(student):
        return student["name"]                                                      # student["name"] is a value returned by get_name into the key parameter of the sorted function. If we consider the only purpose of the student variable in def get_name(student) is to show that anything in the curly bracket of the function if has keywords, will return value. That act is the meaning of putting this def function as the key parameter of the sorted function. Here we need to specify the iterator name which we are going to use later in the for loop where we sort the list, and the list must exist with keyword "name". It's like a puzzle
    # We just defined a function with def and showed what student is going to do, it is going to return the value of keyword "name" for iterated student. It is cinnected to the key input of sorted function which is sorting students list that is done before def and after append(student) command. It's like sidechaining a compressor in a daw
    # This is like a switch
    def get_house(A):
        return A["house"]
    # So when we pass in a function like get name or get house to the sorted function like the value of the key, that function is automatically called by the sorted function for you on each of the dictionaries in the list and it uses the return value[the value of the name key in each dictionary] of get_name() or get_house() to decide what strings to actually use to compare in order to decide which is alphabetically correct. We don't pass in the functions in the key parameter by the parentheses by the end. The sorted performs the alphabetization vased on the return value but it is not calling it so we don't add the () parentheses at the end
    # o jokhon students ke sorted korar jonno key call kortese o hochhe prottkta dictionary te torch light fele khuje khuje ber kortese name gula jate kora ultimately oibhabe sajaite pare. So sorted(students, key=def_name) hochhe emon ekta list[] jekhane element dictionary gula tader name key er value gula die alphabetically re organised hoye gese.
    for student in sorted(students *10, key=get_name, reverse=False):              # We can make each iteration 10 times then go to the next element, remember sketchup? lol
                print(f"{student['name']} is in {student['house']} house")
# it's a bit arbitrary, the developers kheal
# remember one thing, goal is not to know everything about python, because we have better systems like wikipedia for that. The reason why we don't memorise anymore mindlessly. It is to wrap head around the main bulk so that everything else we can control and we can create vision. Same for AI, because understanding gives conceptualization and that gives control and contribution as humans.
# Let's have fun.
# The main difference between list and dictionaries are that one is these are specified by numbers as index the other one keywords as index. Now exploit the utility anyway we want to experience emergence properties i.e, lists inside dictionary, vice versa or each inside themselves. Loop and iterations are command flows themselves
# We can do the same thing as def function using lambda

if False:
    students=[]
    with open("students.csv") as file:
        for line in file:
            name, house= line.rstrip().split(",")
            student={"name": name, "house": house}
            students.append(student)
    for student in sorted(students, key= lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']} house")

# lambda student: student["name"] means we are inputing student and outputing student["name"] into a function. That is exactly lambda. It's like the such that syntax of mathmatics
# so key is assigned to by an anonymous function lambda which is the act of taking each dictionary that is student or any iterator like A and returning the value of the dictionary student or A specified by the keyword "name"
# We can use anonymous functions as much as we want but in contexts like this, when we want to pass a function into another function and it does not need a name we can add lambdas as many as we want
# lambda can have multiple parameters, (students, key = lambda students, x, y: student["name"])

# made a program for collatz conjecture
if False:
    x=int(input("give me a number "))

    while True:
    
        if x%2==0:
            
            file=open("collatz_conjecture_table.csv", "a")
            file.write(f"{x} ")
            x=int(x/2)
            
            
        elif x%2!=0:
        
            if x==1:
                print("found 1")
                break
            else:                
                file=open("collatz_conjecture_table.csv", "a")
                file.write(f", {x} \n")
                x=3*x + 1                                        
        else:
            print(f"we got foreign condition with {x} and ended the loop")

# The utility is that it does not need a name. We totally bypassed naming the get_name() and writing it in key parameter input

# Some fuckups
if False:
    students=[]
    with open("names2.csv") as file:
        for line in file:
            name, area, location= line.rstrip().split(",")
            # we can also define the dictionary by assigning variables and perceive its design more easily
            student={"name": name, "area": area, "location": location}                                  # same old assignment
            students.append(student)
    print(students)
    for student in students:
        if len(student)==2:
            print(f"{student['name']} lives in {student['location']}")
        if len(student)==3:
            print(f"{student['name']} lives at {student['area']} in {student['location']}")
            

if False:
    students=[]
    with open("names2.csv") as file:
        for line in file:
            name, home= line.rstrip().split(",")
            student={"name": name, "home": home}
            students.append(student)
    for student in sorted(students, key= lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']} home")
 
# As our names2.csv have 3 values separated by comma, we encountered a value error
# To solve this let's say we add quotes in harry's home address but we still have comma in the process of dictionary creation for keyword assigning
# Malan's law, "If we are facing a problem, chances are somebody else has already faced the problem"
# Let's find library made in the context of csv files
# I know it's fun to solve problems for exercise but in real life, if it is for fun, it is better to solve problems that nobody solved

if False:
    import csv
    students=[]
    with open("names2.csv") as file:
        reader = csv.reader(file)                       # Csv just comes with a funtion called reader whose purpose in life is to read a csv file for you. He will figure out where are the commas, where are the quots, the potential corner cases and deal it for you
        # We can override certain defaults, wheather it is a comma or a pipe or anything else but by default it is gonna work
        # let's iterate over the reader instead of the file. Remember reader is our new variable now
        for row in reader:
            students.append({'name': row[0], 'home': row[1]})
            # Reader gives us row, so it is not doing str split() using symbol comma, it is rather creating lists automatically on each row using the commas in the csv file. This way comma inside quotation marks get overriden. And in this line we are just taking list "row" elements with index [0] to [1] and making a dictionary with it by assigning it as values to our suggested keywords 'name' and 'home'. In list we index using numbers and in dictionary we index using keywords.

    for student in sorted(students, key= lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")
# So we solved a contradiction between english and CSV format where one represents comma in the language English and the other separates string arguments

if False:
    import csv
    students=[]
    with open("names2.csv") as file:
        reader = csv.reader(file)                       # Csv just comes with a funtion called reader whose purpose in life is to read a csv file for you. He will figure out where are the commas, where are the quots, the potential corner cases and deal it for you
        # We can override certain defaults, wheather it is a comma or a pipe or anything else but by default it is gonna work
        # let's iterate over the reader instead of the file. Remember reader is our new variable now
        for row in reader:
            students.append({'name': row[0], 'home': row[1], 'zelensky': row[2]})
            # Reader gives us row, so it is not doing str split() using symbol comma, it is rather creating lists automatically on each row using the commas in the csv file. This way comma inside quotation marks get overriden. And in this line we are just taking list "row" elements with index [0] to [1] and making a dictionary with it by assigning it as values to our suggested keywords 'name' and 'home'. In list we index using numbers and in dictionary we index using keywords.

    for student in sorted(students, key= lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")
# It will show error text on terminal <IndexError: list index out of range> even if one of the lists have 3 elements,

if False:
    import csv
    students=[]
    with open("names2.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({'name': row[0], 'home': row[1]})
    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student ['name']} is from {student['home']}")

# In the for loop we can do the same unpacking as before

if False:
    import csv
    students=[]
    with open("names2.csv") as file:
        reader = csv.reader(file)
        for name, home in reader:
            students.append({'name': name, 'home': home})
    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student ['name']} is from {student['home']}")

# The module csv reader is taking care of the comma separated data, not the individual comma symbols in the data from each line lists
# Is it possible to read and write to a file at the sane orogram?
# Years ago the mental model of files was a casette tapes are sequencial. We can not jump up and down. Like the netflix scrubber, we can not jump up and down like random access memory
# We can also seek the file in a different point but that's not the scope of the class
# There is a segway to reading csv, we can store the names in the column in the csv file itself, these are like spreadsheets.
# At the top line of names2.csv let's add name, home like a table
# Let's use a dictionary reader, instead of csv.reader(file) to csv.DictReader(file)

if False:
    import csv
    students = []
    with open("names2.csv") as file:
        reader= csv.DictReader(file)
        # A reder returns lists, a DictReader reaturns a dictionary on every iteration of row in reader lol
        for row in reader:
            # Instead of reader giving us values of indexes like row[0] we get the keyword as indexes like row["name"]. So by default reader thinks there are 0,1,2,3,..... at the 0th row
            students.append({'name': row['name'], 'home': row['home']})
        print(students)
    for student in sorted(students, key=lambda student: student["home"]):
            print(f"{student ['name']} is from {student['home']}")

if False:
    import csv
    students = []
    with open("names2.csv") as file:
        reader= csv.DictReader(file)
        for row in reader:
            students.append(row)
    for student in sorted(students, key=lambda student: student["home"]):
            print(f"{student ['name']} is from {student['home']}")

# Shifting columns doesn't matter, the DictReader will still read the data correctly because it is using the keywords as indexes instead of numbers
# We can easily add more columns in the csv file and we can read them as well, we just need to add the keywords in the dictionary creation line

if False:
    import csv
    students = []
    with open("names2.csv") as file:
        reader= csv.DictReader(file)
        for row in reader:
            students.append(row)
    for student in sorted(students, key=lambda student: student["home"]):
            print(f"{student ['name']}, from {student['home']}, is assigned to {student['house']} house")

# The code will break if we think the first column is the name but it is not, so we need to add a header row in the csv file. The DictReader will use the first row as the header row and use it as the keys for the dictionaries it creates. So we need to add a header row in the csv file with the names of the columns.
# Let's learn how to write to a csv file using the csv module. We can use the csv.writer() function to create a writer object that we can use to write to a csv file. We can use the writerow() method of the writer object to write a row to the csv file. We can also use the writerows() method to write multiple rows at once. Let's see how we can do this.

if False:
    import csv
    name = input('What\'s your name? ')
    home = input('Where do you live? ')
    house = input('What house are you in? ')
    with open('names2.csv', 'a', newline='') as file:
        writer = csv.writer(file)                                   # Here writer is a variable, and writer() is a function that takes a file object and returns a writer object that we can use to write to the csv file. We can use the writerow() method of the writer object to write a row to the csv file. We can also use the writerows() method to write multiple rows at once. Let's see how we can do this.
        writer.writerow([name, home, house])                        # We are getting lists of values from the user and writing them to the csv file. We are using the writerow() method of the writer object to write a row to the csv file. We are passing a list of values to the writerow() method, and it will write them to the csv file as a row. We can also use the writerows() method to write multiple rows at once. Let's see how we can do this.
        # If There is a header row in the csv file, we can use the writerow() method to write a row to the csv file. We can also use the writerows() method to write multiple rows at once. Let's see how we can do this.
        # If there is comma in the data the csv module will automatically handle it by enclosing the data in quotes. We don't have to worry about it. The csv module will take care of it for us.

# Let's use dictionary this time, we can use the csv.DictWriter() function to create a writer object that we can use to write to a csv file. We can use the writerow() method of the writer object to write a row to the csv file. We can also use the writerows() method to write multiple rows at once. Let's see how we can do this.
if False:
    import csv
    name = input('What\'s your name? ')
    home = input('Where do you live? ')
    house = input('What house are you in? ')
    with open('names2.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home", "house"])         # fieldname is a second argument that we can pass to the Dict
        writer.writerow({"name": name, "home": home, "house": house})

# CSV is not the only file and format to use, for example there are popular formats like JSON, XML, YAML, etc. But CSV is a very common format for tabular data and is widely used in data analysis and data science. It is also easy to read and write using the csv module in Python.
# Let's talk about binary files oposed to text files. Text files are human readable and can be opened in a text editor. Binary files are not human readable and can only be opened in a program that understands the format of the binary file. For example, an image file is a binary file and can only be opened in an image viewer or editor. A text file can be opened in a text editor like Notepad or Sublime Text. We can read and write binary files using the 'rb' and 'wb' modes in the open() function. Let's see how we can do this.
# Python has a library for almost everything, PIL, pillow, etc. for image processing, numpy for numerical computing, pandas for data analysis, etc. We can use these libraries to read and write binary files in their respective formats. For example, we can use the PIL library to read and write image files in various formats like JPEG, PNG, BMP, etc. We can use the numpy library to read and write binary files in the NumPy format. We can use the pandas library to read and write binary files in the HDF5 format. Let's see how we can do this.
# pillow.readtheddocs.io , it's a library for image processing in Python. It is a fork of the original PIL library and is actively maintained. We can use the pillow library to read and write image files in various formats like JPEG, PNG, BMP, etc. We can also use the pillow library to perform various image processing tasks like resizing, cropping, rotating, etc. Let's see how we can do this.
# We can add filters on instagram, we can also do animations
# I just thought about an voice leading analyzing tool, a program that will visually represent if the voice leading is correct according to tonality, or which category it falls into. Different syntax or caliberation using different period of music, like , tonal, atonal, jazz, romantic etc
# Let's make a program that creates an animated GIF. These things are everywhere in the forms of memes, animations stickers and the likes and

# In a GIF there are maltiple images that are displayed is a loop over and over again. We can use the pillow library to create an animated GIF by creating multiple images and saving them as a GIF file. Let's see how we can do this.
# Let's start with a couple of costumes, from another popular programming language, we can use the turtle library to create a turtle that can draw on the screen. We can use the turtle library to create multiple images and save them as a GIF file. Let's see how we can do this.
# Let's terminal code costume1.gif , it is just a static picture of a cat, no movement at all
# Now, let's terminal code costume2.gif , it is a little bit aligned differently different
# These cat images come from a popular programming language from MIT called Scratch, it is a visual programming language that is used to create animations and games. It is a very popular programming language for kids and beginners. We can use the images from Scratch to create an animated GIF using the pillow library in Python. Let's see how we can do this.
# Scratch allows you to very graphically to animate all these and more
# Let's terminal code 10.1_costumes.py and create our own program that takes as input two or even more image files and creates an animated GIF using the pillow library in Python. Let's see how we can do this.
