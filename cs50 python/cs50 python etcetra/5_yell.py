# Just some program that allows users to pass in inputs and then it yells back at them the input messege.
# Let's just write that in in programming language, as it involves a custom function let's start with main and yell
if False:
    def main():
        yell('This is CS50')
        #wList=[input('Iput: ') for _ in range(3)]
        #yell3('This','is','Heaven')
        wList=[]
        while True:
            word=input('Input<type 4 for next steps>: ').strip()
            if word=='4':
                break
            else:
                wList.append(word)
        yell3(*wList)
        

    # Now let's implement the yell() function that takes in a phrase.

    def yell(phrase:str='RUN AGAIN AND WRITE AT LEAST SMTH!'):
        '''
        Print the user input applying uppercase()
        '''
        print(phrase.upper())

    # Now let's make another type of yell where we can pass in a list with multiple print objects to uppercas()
    def yell2(words:list):
        whispers=[word.upper() for word in words]
        #line=' '.join(whispers)
        # We could also use unpack
        #print(line, end='!\n')
        print(*whispers, end='!\n')
        # But still passing in list to a function is not user friendly cause it's not flexible outside the block. Let's create another function that takes in *args

    def yell3(*words:str):
        '''
        Takes in any number of arguments.
        '''
        #whispers=[word.upper() for word in args]
        # Instead of *args,args we can also use *words,words
        #whispers=[word.upper() for word in words]
        # We can also use map to do the same
        # Map takes two arguments, name of the function that that I want to map onto a sequence of values. 
        # For this case we want to apply str.upper[according to documents it's a method withoud () and we gonna use just that as we want to apply that to the next line, it's almost like the blueprint excapsulation analogy] method to every values passed into the function because of the *args.
        # We don't wanna call str.upper() now, rather we want to pass this function into hte map function so that map can according to it's design add those paretheses and call it on every passed in word *args.
        # So it's like passing in a def function() into another where map() takes in any function with multiple iterables. So we can this way totally avoid using loops to get a function iterated to make our codes more compact.
        whispers=map(str.upper,words)
        # Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted. 
        # If strict is true and one of the arguments is exhausted before the others, raise a ValueError.
        # Let's see outside this scrpt to see what Jarvis says the above means.
        print(*whispers, end='!\n')
        ...

    # Conclusion
    if __name__=='__main__':
        main()
        # Works just fine.

# Jarvis explanation;
if False:
    # The documentation says map(function, iterable1, iterable2, ...)
    # If you ever pass more than one iterable to map(), it processes elements side-by-side:

    # Function expecting 2 arguments
    def combine(first, second):
        return f"{first.upper()} {second.upper()}"

    names = ["john", "paul", "george", "ringo"]  # 4 elements
    roles = ["guitar", "bass"]                   # 2 elements (shortest)

    # map stops as soon as 'roles' runs out
    result = list(map(combine, names, roles))

    print(result)
    # Output: ['JOHN GUITAR', 'PAUL BASS']
    # In this multi-iterable case, map() stops as soon as roles runs out of items (is exhausted). "george" and "ringo" are ignored.
    # Not relevant for our case because we input only one iterable.

# Let's explore another topic called list comprehension, it's a big phrase but it's effect is quiet opposit; it let's us create a list on the fly. I think I know this one, using a one liner lol.
# For that we need to write a python expression inside square braces that in effect will dynamically generate a brand new list for us using some logic we would write with a loop. 
# Look back on first whisper designing in def yell2() func although it is not functional programming but rather a feature of python.
# Let's explore another feature to filter values in a list and for that let's terminal code 6_griffindors.py

