# Let's first bring our list of students from before.
if False:
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]


    # Let's assign to gryffindors, loacal variable, a list with longer lines so braces at different lines to create a list comprehension.
    if False:
        gryffindors=[
            student['name'] for student in students if student['house']=='Gryffindor'
        ]

        for gryffindor in sorted(gryffindors):
            print(gryffindor)

        # There is another functional feature called filter(function,iterable) and to utilize this let's define a function called is_gryffindor()
        def is_gryffindor(s):
            if s['house']=='Gryffindor':
                return True
            else:
                return False
            
    # We can do the same thing by returning the conditional iself, it means the same.
    def is_gryffindor2(s):
        return s['house']=='Gryffindor'

    # Remember students have multiple s s or student s, which is an iterable where is_gryffindor2 function can be applied in an iterated order and return a group of boolean values, like a conditional sign in pd files.
    # This is exactly what filter(function,iterable) does whereby it takes in the custom function and apply it to the iterator in an iterable fashion.
    # Unlike map(), filter() takes in a custom function as the first args which returns a boolean for each iterated[for our case should I return it's 'house' value or not] as the second args.
    # In a nutshell filter(function,iterable) is designed to ask quaestions to the function[is_gryffindor(s), s is the blue print for the iterator, not the iterable socket of the filter] giving the iterable[students list in our case] as clue and if it matches with the condition of the function inside which passing in the iterator[student of students into the s socket of the is_gryffindor(s)] the function replies replies yes[boolean] and then finally, filter function stores the iterator [as in our case a gryffindor2] in a list[in our case gryffindors2 another iterable].
    dict_gryffindors1=filter(is_gryffindor2,students)
    # There is another way;
    dict_gryffindors2=filter(lambda dog:dog['house']=='Gryffindor', students)
    # When we want filter to call a function for us we don't type in () as we don't input manually.
    if False:
        gryffindors2=[dict_gryffindor2['name'] for dict_gryffindor2 in dict_gryffindors2]
        # Let's what we did to our griffindors with each gryffindor before to our new gryffindors2 with each gryffindor2.
        for gryffindor2 in sorted(gryffindors2):
            print(gryffindor2)
        # Works pretty well.
    # David's way of doing this;

    for gryffindor2 in sorted(dict_gryffindors2, key=lambda jibon:jibon['name']):
        # A custom key function can be supplied to customize the sort order, and the reverse flag can be set to request the result in descending order.
        print('Gryffindor', gryffindor2['name'])

# Let's exercise another kind of toolkit called dictionary comprehensions, and already the syntax is starting to get weirder. Let's start the same problem old school way, let's start with a list of studrnts and empty lists.
students=['Hermione','Harry','Ron']

# Inside the variable gryffindors we want an iterable list(), so square bracesp[]; inside the square braces we want a dict() as an iterator with necessary values and keywords even from other datasets; this will happen for each iterator dict() with one or more key words or values from each of those outside iterators in the outside iterable [or eneumarate(outside iterable) in case we want to utilize the indices for the outside iterators].
gryffindors=[{'index':i+1,'name':student,'house':'Gryffindor'} for i,student in enumerate(students)]
# We are getting this in cli;
'''
[{'index': 1, 'name': 'Hermione', 'house': 'Gryffindor'}, {'index': 2, 'name': 'Harry', 'house': 'Gryffindor'}, {'index': 3, 'name': 'Ron', 'house': 'Gryffindor'}]
'''
#print(gryffindors)

# Let's make a simpler dictionary now;
dict_Gs={student:'Gryffindor' for student in students}
# This is called dictionary as opposed to a list comprehension.
#print(dict_Gs)

# Let's emember a time when we wanted to print ranking from a simple list of students;
for i in range(len(students)):
    print(i+1,students[i])
# On the other hand enumerate(iterable,start=0) gives us not only the iterable elements but also it's index, we don't have to provide keywords here like the problems in 4_unpack.py, we just need to follow the order.
for i,student in enumerate(students,1):
    print(i,student)

# Now it's time to use generators which is relevance in the functions which deals with a lot of data and might crash the local machine, it's like when we run out of memory just before sleep when we are counting sheeps lol. To explore that more let's terminal code 7_sleep.py

