# This lesson is about the etcetra of the course comprising of all the beyonds we could do on top of the basics that we have done so far.
# Never shy away to check the open library of python docs.python.org, docs.python.org/3/(library|reference|howto)/ and when you do that you will see there are some tidbits we did not touch on yet.
# They were mostly things that might have felt too much too soon. Let's work on set.
# Very similar to sets of maths, we can use it in our everyday code. Let's look at docs.python.org/3/library/stdtypes.html#set
# Let's solve a problem by automatically getting rid of the duplicates.
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]
# Let's first create a list where we will accumulate the houses uniquely.
if False:
    houses=[]
    for student in students:
        if student['house'] in houses:
            pass
        else:
            houses.append(student['house'])
    print(houses)
    # Above was my solution ;) smart ehh? loops and whatnots and now let's try Malan's method,
    #houses=[]
    # Let's change the above assignment above wherein list() is represented by [], let's instead assign to houses a built in set() function
houses=set()
# Below is David's old method;
'''
for student in students:
    if student['house'] not in houses:
        houses.append(student['house'])
        # Same same different so far.
# But he adds str sorting alphabetically
for house in sorted(houses):
#then he stops and changes it to this;
'''
for student in students:
    houses.add(student['house'])
    '''
    # We don't need any more conditionals as similar to real world set a set in python stores unique elements.
    # Also, we need to add to a set as opposed to append to a list following the documentation.   
    # There is another Jarvis suggested method, first lets write the loop statement;
    #for student in students
    # Now let's take the iterator and put it in front of it;
    #student for student in students
    # It won't work yet, now we need to put it inside curly braces to imitate the set.add(iterator);
    #{student for student in students}
    # we can do same with square braces to represent a list;
    #[student for student in students]
    # Now it only represents an encloser containing our dataset, we need to assign it to housesByJarvis
    #housesByJarvis=[student for student in students]
    # Above won't work because TypeError: unshapable type: 'dict'. We can only iterate with an element not another i.e, dict for this case. So let's assign student['house']
    '''
housesByJarvis={student['house'] for student in students}
# If we put them under the square braces they will not do the unique elements and sorting properties of sets.
if False:
    for house in sorted(houses):
        sh=sorted(houses)
        if house!=sh[-1]:    
            print(house,end=', ')
        else:
            print(house,end='. ')

#print(', '.join(housesByJarvis)+'.')
'''
it's not imune to randomness bdw;
You are directly on the right track! What you are seeing is Python's Hash Seed Randomization, which deliberately introduces randomness into memory every time Python runs.

Why this happens
How Sets Store Data in RAM: Python sets use a lookup system called a hash table. When you put a string like "Gryffindor" into a set, Python runs it through a hashing function to decide which specific memory bucket to drop it into.

Hash Seed Randomization: For security reasons (specifically to prevent hash-collision denial-of-service attacks), Python generates a new random hash seed every single time a Python process starts.

The Result: Even though your code doesn't change, running python etcetra.py launches a fresh process with a new random seed. "Gryffindor", "Ravenclaw", and "Slytherin" get hashed to different memory locations each time, changing the order they come out when you iterate over the set.

How to fix it in your code
If you are currently printing or iterating directly over a set, you are at the mercy of that random hash order.

To guarantee alphabetical sorting every single time, pass the set into sorted()
'''
housesByJarvis=sorted(housesByJarvis)
print(', '.join(housesByJarvis)+'.')
if False:
    ...
    if 'Gryffindor' in housesByJarvis:
        print(list(housesByJarvis).index('Gryffindor'))
    for i, house in enumerate(housesByJarvis):
        if house=='Gryffindor':
            print(i)



# Let's work on this notion called global variables, which we haven't touched on yet as opposed to local variables.
# It sits on top of all the functions in a script. It looks like an aspect of the module|library area but they are not.
# To demonstrate that let's terminal code 2_bank.py 