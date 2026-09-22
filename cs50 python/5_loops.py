# Loops are this ability to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.
# A cycle of sorts
# For loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. They are often used when you know in advance how many times you want to execute a block of code.
# We will create a python program that meaws like a cat 3 times

if False:
    print("Meow")
    print("Meow")
    print("Meow")

# If we want to meaw 50 times or n times it's gonna get ugly and we will have to write print("Meow") 50 times or n times. This is where loops come in handy.
# Let's use "while"!
# A while loop is used to execute a block of code as long as a specified condition is true. It is often used when you don't know in advance how many times you want to execute a block of code.
# We will create a python program that meaws like a cat 50 times using a while loop
# While is a construct that allows me to ask a question again and and again, to get a boolean answer, and to execute a block of code as long as the answer is true.
# Every time I meaw I ask a question: "Have I meawed 50 times?" If the answer is no, I meaw again and ask the question again. If the answer is yes, I stop meawing.
# We will use a variable to keep track of how many times we have meawed. Let's call this variable "meow_count". We will initialize it to 0 and then increment it by 1 every time we meaw.
# We will also use a variable to keep track of how many times we want to meaw. Let's call this variable "meow_limit". We will initialize it to 50 and then compare it to "meow_count" to determine when to stop meawing.

if False:
    i = 5           # i is just an integer, it has nothing to do with our print function. 
    while i != 0:   # This is the condition segment of the while loop. 
        print("Meow")
        i -= 1      # [Assignment function]. This is the same as i = i - 1. It decrements the value of i by 1 every time python check back(iterate through) the while condition (That's why its called loop). 
                    # without this it will keep coming back to check "while" condition and it will always be true because i will always be 5, so it will meaw forever. This is called an infinite loop and it's usually not what we want.
                    # If that happens press Ctrl + C to stop the program. This is a common way to stop an infinite loop in Python.

if False:
    i = 5
    while i != 0:
        print("Meow")
        i = i - 1   # This is the same as i -= 1. It decrements the value of i by 1 every time python check back(iterate through) the while condition.
                    # It does not make sense, it's just rather a pythonian way to say that i - 1 is the i.
if False:
    meow_count = 0
    meow_limit = 50
    while meow_count < meow_limit:
        print("Meow")
        meow_count += 1     # This is the same as meow_count = meow_count + 1. It increments the value of meow_count by 1 every time python check back(iterate through) the while condition.

if False:
    meaw_count = 9
    meaw_limit = 49
    while meaw_count < meaw_limit:
        print("Mau")
        meaw_count += 4     # This is also the math variable of delta, which is the change in value of the variable. In this case, we are incrementing the value of meaw_count by 4 every time python check back(iterate through) the while condition. This means that we will meaw 10 times (9, 13, 17, 21, 25, 29, 33, 37, 41, 45) before we stop meawing because meaw_count will be equal to or greater than meaw_limit.   
                            # meaw_count is a variable defined earlier. Its different than print("Meow"), we just created a condition like cyclic max msp project, a device exclusive to our outcome. It just deals with the looping mechanism of while condition. We can change the name of the variable to anything we want, as long as we use the same name consistently throughout the code. The name of the variable does not affect the functionality of the code, it is just a label that we use to refer to a value in our program.

if False:
    i = 1
    while i <= 3:
            print("RAWRRR!")
            i += 1          # i -= 1 would be an infinite loop because i will always be less than or equal to 3, so we need to increment i by 1 every time we check the while condition to eventually make it false and stop the loop.

# We are just using the universal logics of mathmatics and this new language called python to create a loop that will meaw 3 times. We start with i = 1, and we check the condition i <= 3. If the condition is true, we print "RAWRRR!" and then we increment i by 1. This process repeats until i is greater than 3, at which point the condition becomes false and the loop stops.

if False:
    i = 0
    while i < 3:
            print("Blep")
            i += 1                      # it's a good habit to start now from zero to go upto but not through 3
                                        # more coherent with mathmatical notation and physics order equation staffs containing n.
                                        # not like java it does not have ++ or -- operators, so we have to use += and -= to increment and decrement the value of i. This is just a syntax choice in Python, it does not affect the functionality of the code. In Java, you can use i++ to increment i by 1, but in Python you have to use i += 1. This is just a design choice in the Python language.

# Oval for start, stop; rectangle for assignment or funtion and diamond for condition. 

# FOR LOOPS
# For loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. They are often used when you know in advance how many times you want to execute a block of code. The syntax of a for loop in Python is:
# We will use list as data types. We've seen str, int, float, bool, and now we will see list. A list is a collection of items that are ordered and changeable. We can use a for loop to iterate over the items in a list.
# We will create a list of cat sounds and then use a for loop to print each sound.
# Way of storing multiple values in a single variable.
# For loops are often used to iterate over a list of items, but they can also be used to iterate over a string, a tuple, a dictionary, a set, or any other iterable object. The for loop will execute the block of code for each item in the iterable object.

if False:
    for i in [0,1,2,3,4,5] :            # Much simpler than while loop. Square brackets represent a list.
        print("Meow")                   # It will just iterate through the items in the list, for every i belonging to the list run the print function.

# Use functions in range or it will be ugly. Range is a built-in function that generates a sequence of numbers. The syntax of the range function is:
# range(start, stop, step). By default the values are from 0 to upto the number specified but not through it, and the step is 1. So if we just use range(6), it will generate a sequence of numbers from 0 to 5 (inclusive). The stop parameter is 6, so the sequence will include numbers up to but not including 6.
# start is the number that the sequence starts from (inclusive). If start is not specified, it defaults to 0.
# stop is the number that the sequence ends at (exclusive). This means that the sequence will include numbers up to but not including stop.
# step is the difference between each number in the sequence. If step is not specified, it  defaults to 1. This means that the sequence will include every number from start to stop, incrementing by 1 each time. 

if False:
    for _ in range(0, 5, 2):            # This will generate a sequence of numbers from 0 to 5 (inclusive). The stop parameter is 6, so the sequence will include numbers up to but not including 6.
        print("Meow")                   # This will print "Meow" for each number in the sequence generated by the range function. The variable _ is a common convention in Python to indicate that we are not using the variable, and it is just a placeholder for the current number in the sequence. In this case, we are not using the variable _ in the print function, we are just printing "Meow" for each number in the sequence generated by the range function.

if False:
    for i in range(6):                  # This will generate a sequence of numbers from 0 to 5 (inclusive). The stop parameter is 6, so the sequence will include numbers up to but not including 6.
        print("Meow")                   # Even thogh I am defining a variable i, I am not using it in the print function. I am just using it to iterate through the range of numbers from 0 to 5. The variable i is just a placeholder for the current number in the sequence, but we are not using it in the print function. We are just printing "Meow" for each number in the sequence. This is a common pattern when we want to repeat a block of code a certain number of times, but we don't care about the specific values of the variable that we are iterating over.

# If we don't wanna use a variable like integer i, we can use an underscore _ as a placeholder. This is a convention in Python to indicate that the variable is not going to be used.
if False:
    for _ in range(6):                  # This will generate a sequence of numbers from 0 to 5 (inclusive). The stop parameter is 6, so the sequence will include numbers up to but not including 6.   
        print("GiGiGaGa")               # We are using an underscore _ as a placeholder for the variable that we are iterating over, because we don't care about the specific values of the variable. We just want to repeat the block of code a certain number of times, and the underscore is a way to indicate that we are not using the variable. This is a common pattern when we want to repeat a block of code a certain number of times, but we don't care about the specific values of the variable that we are iterating over.

if False:
    print("Meaw" * 3)                   # This is a string multiplication operation. It will repeat the string "Meaew" 3 times, resulting in "MeaewMeaewMeaew". This is a convenient way to repeat a string a certain number of times without having to use a loop.
    print("Meaw" + "Meaw" + "Meaw")     # This will concatenate the string "Meaew" 3 times, resulting in "MeaewMeaewMeaew". This is another way to repeat a string a certain number of times, but it is less convenient than using the string multiplication operator because we have to write the string multiple times and use the + operator to concatenate them together.
                                        # But there's no space between the words, it's like using + between same strings in the print function so we can add a space at the end of the string to make it look better.
    print("Meaw " * 3)                  # This will repeat the string "Meaew " 3 times, resulting in "Meaew Meaew Meaew ". This is a convenient way to repeat a string a certain number of times without having to use a loop, and it also adds a space between the words for better readability.
    print("Meaw\n" * 3)                 # Has an extra newline character at the end of the string, so it will print "Meaew" 3 times on separate lines. This is a convenient way to repeat a string a certain number of times without having to use a loop, and it also adds a newline character at the end of the string to print each repetition on a new line for better readability.
                                        # There is also an extra line at the end, because \n is with every strings. we can use end='' to remove the extra line at the end of the string.
    print("Meaw\n" * 5, end="")         # This will print "Meaew" 3 times on separate lines without an extra line at the end. The end='' argument in the print function specifies that the string should not end with a newline character, which is the default behavior of the print function. By setting end='' we are telling the print function to end the string with an empty string instead of a newline character, which removes the extra line at the end of the output.

if False:
    times = int(input("How many times do you want the cat to meaw? "))
    if times < 0:
        times = int(input("Please enter a countable number.")) # It means ask for input then make it integer and assign again to "times" variable. This is a way to ensure that the user enters a valid input, in this case a non-negative number, before we proceed with the rest of the program. If the user enters a negative number, we will prompt them to enter a non-negative number until they do so. This is a common way to handle invalid input in Python programs.
        print("Meaw\n" * times, end="")
    elif times == 0:
        print("The cat is silent.") 
    else:
        print("Meaw\n" * times, end="")

# We can also use loop here, we can induce an infinite loop like while true: and then break out of the loop when we get a valid input. This is another way to handle invalid input in Python programs, but it is generally not recommended because it can lead to an infinite loop if the user continues to enter invalid input. It is usually better to use a while loop with a condition that checks for valid input, as we did in the previous example, to ensure that the program does not get stuck in an infinite loop.
if False:
    while True:                             # The answer to the true question is always true, so this loop will run indefinitely until we break out of it. This is a common pattern when we want to keep asking the user for input until they provide a valid input. It's different than if true.
        times = int(input("How many times do you want the cat to meaw? "))
        if times < 0:
            print("Please enter a countable number.")
            continue                        # Continue will keep the loop going.
        else:
            break                           # Break will break you out of the most recently begun loop.
    print("Meaw\n" * times, end="")

if False:
    while True:                             # The answer to the true question is always true, so this loop will run indefinitely until we break out of it. This is a common pattern when we want to keep asking the user for input until they provide a valid input. It's different than if true.
        times = int(input("How many times do you want the cat to meaw? "))
        if times > 0:                       # By default the if True infinite loop will keep going, continue is by default. So specifying only the condition for break works and gives us even more concise code.
            break                           # Break will break you out of the most recently begun loop.
    for _ in range(times):
        print("Meaw")

# More refined.
if False:
    while True:                                     
        times = int(input("How many times do you want the cat to meaw? "))
        if times > 0:                       
            break
        else:
            print("Please enter a countable number.", end=" ")  
    for _ in range(times):
        print("Meaw")

if False:
    def main():
        number = get_positive_integer()
        meaw(number)
    
    def get_positive_integer():
        while True:
            try:
                times = int(input("How many times do you want the cat to meaw? "))
                if times > 0:
                    return times              # return means that we are returning the value of times to the main function, so that we can use it in the meaw function. This is a way to pass the value of times from the get_positive_integer function to the main function, and then to the meaw function. This is a common pattern in Python programs, where we define a function to get input from the user, and then we return that input to the main function so that we can use it in other functions. So it is already breaking out of the infinte while true loop when we get a valid input, we just need to return the value of times to the main function so that we can use it in the meaw function. This is a more refined way to handle invalid input in Python programs, as it allows us to keep our code organized and modular by defining separate functions for different tasks.
                else:
                    print("Please enter a countable number.", end=" ")
            except ValueError:                # This is for the case when the user enters something that cannot be converted to an integer, like a string or a float. The try-except block will catch the ValueError that occurs when trying to convert the input to an integer and will prompt the user to enter a valid input instead of crashing the program.
                print("Invalid input. Please enter a positive integer.", end=" ")
    
    def meaw(times):
        for _ in range(times):
            print("Meaw")

    main()

if False:
    def main():
        number = get_positive_integer()
        meaw(number)
    
    def get_positive_integer():
        while True:
            times = int(input("How many times do you want the cat to meaw? "))
            if times > 0:
                return times
    
    def meaw(times):
        for _ in range(times):
            print("Meaw")

    main()

# LISTS
# A list is a collection of items that are ordered and changeable. We can use a for loop to iterate over the items in a list. We can also use a while loop to iterate over the items in a list, but for loops are generally more concise and easier to read when iterating over a list.
# We can create a list of cat sounds and then use a for loop to print each sound.
# In python or any programming language it is useful to have a large amount of data sets to work with, and lists are a way to store multiple values in a single variable. We can use lists to store a collection of items, such as cat sounds, and then we can use loops to iterate over the items in the list and perform some action on each item, such as printing it out. This is a common pattern in programming, where we use data structures like lists to store and organize our data, and then we use loops to process that data in some way.

if False:
    students = ["Hermione", "Harry", "Ron"]    # This is a list of strings. This is not a loop yet. The square brackets represent a list, and the items in the list are separated by commas. We can access each item in the list using its index, which starts at 0. So students[0] will give us "Hermione", students[1] will give us "Harry", and students[2] will give us "Ron". We can also use a for loop to iterate over the items in the list and print them out.
    print(students)
    print(students[0])                       # This will print "Hermione", which is the first item in the list. The index of the first item in the list is 0, so we use students[0] to access it.
    print(students[1])                       # This will print "Harry", which is the second item in the list. The index of the second item in the list is 1, so we use students[1] to access it.
    print(students[2])                       # This will print "Ron", which is the third item in the list. The index of the third item in the list is 2, so we use students[2] to access it.

#For list we don't have to initiate or assign the variable iterating over the list, we can just use a for loop to iterate over the items in the list and print them out. The variable that we use in the for loop will take on the value of each item in the list as we iterate through it, so we can use any variable name we want as long as it is consistent throughout the loop. The important thing is that the variable takes on the value of each item in the list as we iterate through it, so that we can perform some action on each item, such as printing it out.
if False:
    students = ["Hermione", "Harry", "Ron"]
    for _ in students:                      # This will iterate over each item in the list and print it out. The variable student will take on the value of each item in the list as we iterate through it, so the first time through the loop student will be "Hermione", the second time it will be "Harry", and the third time it will be "Ron". This is a common pattern when we want to process each item in a list, we can use a for loop to iterate over the items and perform some action on each item, such as printing it out.
        print(_)                            # _ will make the code too cryptic because we are using the variable in the for loop function, so it is better to use a more descriptive variable name like student. The variable name does not affect the functionality of the code, but it can affect the readability of the code. Using a descriptive variable name can make it easier for other people (or yourself in the future) to understand what the code is doing.

# Why bother, pythpn is more readable than other programming languages, so we can use a more descriptive variable name like student to make the code even more readable and easier to understand. This is a common practice in Python programming, where we prioritize readability and clarity in our code by using descriptive variable names and avoiding cryptic or ambiguous variable names.
if False:
    students = ["Hermione", "Harry", "Ron"]
    for student in students:                 # This will iterate(to perform a repeated action on every individual item within a set, collection, or list) over each item in the list and print it out. The variable student will take on the value of each item in the list as we iterate through it, so the first time through the loop student will be "Hermione", the second time it will be "Harry", and the third time it will be "Ron". This is a common pattern when we want to process each item in a list, we can use a for loop to iterate over the items and perform some action on each item, such as printing it out.
        print(student)                       # This will print each item in the list on a separate line. The variable student is a common convention in Python to indicate that we are iterating over a list of students, but we can use any variable name we want as long as it is consistent throughout the loop. The important thing is that the variable takes on the value of each item in the list as we iterate through it, so that we can perform some action on each item, such as printing it out.

if False:
    students = ["Hermione", "Harry", "Ron"]
    for s in students:                          # Looks more physics like
        print(s)   

if False:
    students = ["Hermione", "Harry", "Ron"]
    for i in range(len(students)):              # For i in students will not give numbers. The range function expects an integer as an argument, but students is a list, so it will raise a TypeError. If we want to iterate over the indices of the list, we can use the range function with the length of the list as an argument, like this: for i in range(len(students)). This will give us the indices of the list, which we can then use to access the items in the list using students[i]. However, it is generally more concise and easier to read to iterate directly over the items in the list using a for loop, like we did in the previous example, rather than iterating over the indices and then accessing the items using those indices.
        # print(i, students[i])                 # This will print each item in the list on a separate line. The variable i is a common convention in Python to indicate that we are iterating over a list of items, but we can use any variable name we want as long as it is consistent throughout the loop. The important thing is that the variable takes on the value of each index in the list as we iterate through it, so that we can access the corresponding item in the list using students[i] and perform some action on it, such as printing it out. However, it is generally more concise and easier to read to iterate directly over the items in the list using a for loop, like we did in the previous example, rather than iterating over the indices and then accessing the items using those indices.
        # print(i, students[1])                 # It's a loop that's why it finishes print function under for loop and repeats for the length times, so it will print "Harry" 3 times because students[1] is "Harry". This is a common mistake when using loops, where we accidentally put a print statement inside the loop that we intended to be outside the loop, which can lead to unexpected behavior. In this case, we are printing students[1] inside the loop, which means that it will be printed for each iteration of the loop, resulting in "Harry" being printed multiple times. To fix this, we should move the print statement outside the loop so that it only gets executed once after the loop has finished iterating over all the items in the list. For every i in the range of the length of the students list, we are printing the index i and the corresponding student at that index. This will give us a numbered list of students, which can be useful for certain applications where we need to keep track of the indices of the items in the list. However, if we just want to print the items in the list without their indices, it is generally more concise and easier to read to iterate directly over the items in the list using a for loop, like we did in the previous example, rather than iterating over the indices and then accessing the items using those indices.
        print(i + 1, students[i])

# Here we just extracted the index out of every items in the list, same thing I have done in max mps using index object. I remember max msp.
# According to adam what i loops really do is it takes the variable and says im the first item in the list, then it executes the function under it. As it is a loop it goes back to its very old list and says im the second items. It keeps doing it untill it runs out of items in the list. It's like going to the gym and doing reps with an ancient counting device.
# Range gives us the number that we input iside it, and len of a list gives us the number of items in the list that's why it works.

# In python there are data structures called dictionaries, which are collections of key-value pairs. We can use a for loop to iterate over the items in a dictionary, and we can access the keys and values using the items() method of the dictionary. This is another common pattern in Python programming, where we use data structures like dictionaries to store and organize our data, and then we use loops to process that data in some way. However, we will cover dictionaries in more detail in a later section, so we will not go into it here.
# Something associated with something else, mil koron excercise.
# It's 2 dimentional. For example let's use lists to show name and houses in hogearts.

if False:
    students = ["Hermione", "Harry", "Ron", "Draco"]
    houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

    for i in range(len(students)):
        print(students[i], houses[i])  

# We can also do this using dictionaries, which are collections of key-value pairs. We can use a for loop to iterate over the items in a dictionary, and we can access the keys and values using the items() method of the dictionary. This is another common pattern in Python programming, where we use data structures like dictionaries to store and organize our data, and then we use loops to process that data in some way. However, we will cover dictionaries in more detail in a later section, so we will not go into it here.
# We will use curly brackets here. It's different than f strings, which we will cover in a later section. Curly brackets are used to define a dictionary, which is a collection of key-value pairs. We can use a for loop to iterate over the items in a dictionary, and we can access the keys and values using the items() method of the dictionary. This is another common pattern in Python programming, where we use data structures like dictionaries to store and organize our data, and then we use loops to process that data in some way. However, we will cover dictionaries in more detail in a later section, so we will not go into it here.

    students_houses = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor", "Draco": "Slytherin"}

# This is gonna get ugly, to make it readable, we can add lines to make it readble this way, but it is still not very readable. We can use a for loop to iterate over the items in the dictionary and print them out in a more readable format, like this:

if True:
    students = {
        "Hermione": "Gryffindor", 
        "Harry": "Gryffindor", 
        "Ron": "Gryffindor", 
        "Draco": "Slytherin"
    }

# We can use indexes that are not restricted to numbers, we can use strings as indexes in a dictionary. In this case, the keys of the dictionary are the names of the students, and the values are the names of their houses. We can use a for loop to iterate over the items in the dictionary and print them out in a more readable format, like this:
if False:                                               # If false usually bypases keepng the code colorful and readable, but it is not a loop, so it will just execute the code once and then stop. This is a common pattern when we want to write some code that we don't want to execute yet, but we want to keep it in the code for later use. We can use if False to bypass the code and keep it in the code for later use, without having to comment it out or delete it.  
    print(students["Hermione"])                         # This will print "Gryffindor", which is the value associated with the key "Hermione" in the dictionary. We can access the value associated with a key in a dictionary using the syntax dictionary[key], where dictionary is the name of the dictionary and key is the key that we want to access. In this case, we are accessing the value associated with the key "Hermione" in the students dictionary, which gives us "Gryffindor". This is a common way to access values in a dictionary, and it allows us to retrieve information based on a specific key.
    print(students["Harry"])                            # This will print "Gryffindor", which is the value associated with the key "Harry" in the dictionary. We can access the value associated with a key in a dictionary using the syntax dictionary[key], where dictionary is the name of the dictionary and key is the key that we want to access. In this case, we are accessing the value associated with the key "Harry" in the students dictionary, which gives us "Gryffindor". This is a common way to access values in a dictionary, and it allows us to retrieve information based on a specific key.
    print(students["Ron"])                              # This will print "Gryffindor", which is the value associated with the key "Ron" in the dictionary. We can access the value associated with a key in a dictionary using the syntax dictionary[key], where dictionary is the name of the dictionary and key is the key that we want to access. In this case, we are accessing the value associated with the key "Ron" in the students dictionary, which gives us "Gryffindor". This is a common way to access values in a dictionary, and it allows us to retrieve information based on a specific key.
    print(students["Draco"])                            # This will print "Slytherin",   which is the value associated with the key "Draco" in the dictionary. We can access the value associated with a key in a dictionary using the syntax dictionary[key], where dictionary is the name of the dictionary and key is the key that we want to access. In this case, we are accessing the value associated with the key "Draco" in the students dictionary, which gives us "Slytherin". This is a common way to access values in a dictionary, and it allows us to retrieve information based on a specific key. 
    print(students)                                     # This will print the entire dictionary, which is a collection of key-value pairs. The output will be something like: {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor', 'Draco': 'Slytherin'}. This is a common way to print the contents of a dictionary, and it allows us to see all the key-value pairs in the dictionary at once.
    for student in students:                            # This will iterate over each key in the dictionary and print the key and its associated value. The variable student will take on the value of each key in the dictionary as we iterate through it, so the first time through the loop student will be "Hermione", the second time it will be "Harry", the third time it will be "Ron", and the fourth time it will be "Draco". This is a common pattern when we want to process each item in a dictionary, we can use a for loop to iterate over the keys and perform some action on each key and its associated value, such as printing them out.
        print(student, end="\n")                                  # This will print each key and its associated value on a separate line. The variable student is a common convention in Python to indicate that we are iterating over a dictionary of students, but we can use any variable name we want as long as it is consistent throughout the loop. The important thing is that the variable takes on the value of each key in the dictionary as we iterate through it, so that we can access the corresponding value in the dictionary using students[student] and perform some action on it, such as printing it out. However, it is generally more concise and easier to read to iterate directly over the items in the dictionary using the items() method, like this: for student, house in students.items(), rather than iterating over the keys and then accessing the values using those keys. This allows us to unpack the key-value pairs directly in the for loop, which can make our code more readable and easier to understand. 

 # Exactly like a list where the students only exists. Ususally students are the keys and houses are the values, but we can also have a dictionary where the keys are the houses and the values are the students, it just depends on how we want to organize our data. The important thing is that we can use a for loop to iterate over the items in the dictionary and perform some action on each key and its associated value, such as printing them out.
if False:
    for student in students:
        print(student, students[student], sep=", ")     # This will print each key and its associated value on a separate line. The variable student is a common convention in Python to indicate that we are iterating over a dictionary of students, but we can use any variable name we want as long as it is consistent throughout the loop. The important thing is that the variable takes on the value of each key in the dictionary as we iterate through it, so that we can access the corresponding value in the dictionary using students[student] and perform some action on it, such as printing it out. However, it is generally more concise and easier to read to iterate directly over the items in the dictionary using the items() method, like this: for student, house in students.items(), rather than iterating over the keys and then accessing the values using those keys. This allows us to unpack the key-value pairs directly in the for loop, which can make our code more readable and easier to understand.

if False:
    for student in students:
        print(student, students[student], sep=":- \n    (", end="). \n")

# Dict is a same database as list but it iterates over keys instead of numbers.
# What if we have more information in the database like their patronus. It's like a database or table.
## Each of the dictionaries are "stuent".
if False:
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}                              # None is a special value in Python that represents the absence of a value or a null value. In this case, we are using None to indicate that Draco does not have a patronus, which is consistent with the Harry Potter series where Draco's patronus is never revealed. This is a common way to represent missing or unknown values in Python, and it allows us to handle cases where we don't have information for certain attributes without causing errors in our code.
    ]

# First members of the pairs, look alike to ratio operation, are keys, indices that are not numeric. 
# We are making 2d dictionaries with name, house, and patronus as keys and their corresponding values for each student. We can use a for loop to iterate over the list of dictionaries and access the information for each student in a structured way, like this:
# This will print the name, house, and patronus of each student on a separate line. The variable student is a common convention in Python to indicate that we are iterating over a list of dictionaries representing students, but we can use any variable name we want as long as it is consistent throughout the loop. The important thing is that the variable takes on the value of each dictionary in the list as we iterate through it, so that we can access the corresponding values in the dictionary using student["name"], student["house"], and student["patronus"] and perform some action on them, such as printing them out. This is a common pattern when we want to process each item in a list of dictionaries, we can use a for loop to iterate over the items and perform some action on each item, such as printing it out in a structured format.
# This dictionary of ours has all same keys so that we can iterate each time with the for loop with same keys in the final print function. That's the design, the prerogative of the programmer.
if False:
    print("#")
    print("#")
    print("#")

if False:
    for _ in range(3):
        print("#")

# The nice thing about function is not just they allow us to not just write codes that we can use and resuse they allow us to create abstraction.
# An abstraction is a way to simplify of a potentially more complicated idea.
# For print function we are not only thinking about hellow we are also thinking about what it does.

if False:
    def main():                         # We are just defining new custom functions using def keyword, and we can call the function by its name followed by parentheses. The main function is a common convention in Python to indicate that this is the main entry point of the program, but we can use any function name we want as long as it is consistent throughout the code. The important thing is that we define a function that performs some action, and then we can call that function to execute the code inside it. In this case, we are defining a function called main that will call another function called print_column with an argument of 3, which will print a column of 3 "#" characters when we run the program.
        print_column(3)

    def print_column(height):           # Generically the parameter is height, but we can use any variable name we want as long as it is consistent throughout the function. The important thing is that the parameter takes on the value that we pass to the function when we call it, so that we can use that value in the body of the function to perform some action, such as printing a column of a certain height.
        for _ in range(height):
            print("#")                  # Definition of print_column() where we know we are gonna use for range loop by comparing inside the definition, the input parameter of range() in this particular scenario.

    main()                              # We kinda complicated the code, it doesn't do anything here yet.

# We are into a more sophicated problem,
# Let's print some chunk of the world of mario at a time.
# Fun part is now we can reimplement the print_column() function in new ways without having to change the main function, because the main function is calling the print_column() function, so as long as we keep the same function name and the same parameter, we can change the implementation of the print_column() function without affecting the main function. This is one of the main benefits of using functions in programming, as it allows us to create abstraction and modularity in our code, so that we can change the implementation of a function without affecting the rest of the code that uses that function. This makes our code more flexible and easier to maintain, as we can make changes to a specific function without having to worry about how it will affect the rest of the code.
# If the name function is not changed and the parameter is not changed, the function will be changed accordingly everywhere used. Good for modification, think about utilization in music composition.

if False:
    def main():                         # main() does not need to know that the underlying implementation of the print_column() has been changed.
        print_column(3)

    def print_column(height):           # This is more like an autonomous block of the code.
        print("#\n" * height, end="")   # Notun kham e purono chithi.              

    main() 

if False:
    def main():                         # Let's make 4 horizontal bricks of the super mario world with "?"s
        print_row(4)

    def print_row(width):              # This is more like an autonomous block of the code.
        print("?" * width, end="\n")   # String multiplication operator can be used to repeat a string a certain number of times, so we can use it to print a row of "?" characters with a width specified by the width parameter. The end="\n" argument in the print function specifies that the string should end with a newline character, which is the default behavior of the print function. By setting end="\n" we are telling the print function to end the string with a newline character, which will move the cursor to the next line after printing the row of "?" characters.              

    main()

# these were all one dimensional.
# Later in super mario brothers wher mario has to jump down into this world where there are a lot of these undersworld barriers.
# There is a square, which is 2  dimentional with a height and a width, so we can use nested loops to print a square of "?" characters with a height and width specified by the height and width parameters. This is a common pattern when we want to print a 2D shape using characters in Python, we can use nested loops to iterate over the rows and columns of the shape and print the appropriate characters for each position in the shape.
if False:
    def main():
        print_rectangle(3,4)

    def print_rectangle(height, width):            # Here for loop is to iterate virtically bottom-down.
        for _ in range(height):                 # Height parameter in action.
            print("#" * width, end="\n")        # Here width parameter is multiplying each string horizontally with same string "?" as bricks devoid of \n in the brick string.

    main()

if False:
    def main():
        print_rectangle(6, 4)

    def print_rectangle(x, y):
        for _ in range(y):
            print("-" * x, end="\n")

    main()

if False:
    def chini():
        print_square(20)
    def print_square(a):
        for _ in range(a):
            print("o " * a, end="\n")
    chini()

# it's like the print operation top to bottom, every pixel
# The def keyword works like sidenote, but custom functions must follow the tree of the ultimate main or "chini" function.


if False:
    def main():
        print_square(5)

    def print_square(size):
        for i in range(size):
            # For each brick in row
            for j in range(size):
                # Print brick
                print("o ", end="")
            print()                                 # it's like print("\n", end="") is the same as print() because the default value of end is "\n", so we can just use print() to print a newline character after each row of "o " characters. This will give us a square of "o " characters with the specified size, where each row of "o " characters is printed on a new line.

    main()

if False:
    def main():
        print_square(20)
    def print_square(size):
        for _ in range(size):
            print_row(size)
    def print_row(size):
        print("o " * size, end="\n")
    main()

if True:
    def main():
        print_square(20)
    def print_square(size):
        for i in range(size):
            print_row(size)
    def print_row(size):
        for j in range(size):
            print("o  ", end="")
        print()
    main()

# Loops let us do tasks cyclically, which is a fundamental aspect of programming. They allow us to repeat a block of code multiple times, which is essential for tasks that require iteration or repetition. Loops are a powerful tool in programming, and they are used in a wide variety of applications, from simple tasks like printing a message multiple times to more complex tasks like processing data or implementing algorithms. By using loops, we can write code that is more efficient and easier to read, as we can avoid having to write the same code multiple times and instead use a loop to repeat the code as needed.
