# The groundbreaking 12 tone technique was championed by Arnold Schoenberg, Albenberg and Anton Vabund.
# It was during the early 20th century, saw it's momentum sustained by subsequent vanguards of serial composition such as boules, stockhausen and babbit.
# Inspired by innovative aproach luminaries like stravinsky, copeland, harrison, andresen and ades also ventured into this realm of serial experimentation
# Building blocks of this revolutionary techniques are tone rows, sets of musical pictures that adhere to fixed order.
# They typiclly compasses all 12 pitch classes of the chromatic scale.
# Within the robust tool sets of the music21 a range of functionalities will let us delve deeper into the intricacies of tonal manipulation.
# Tonal Manipulation: Manipulation of the Tonal syntax to genrate color



# Let's encode a tonerow by employing a row object, a specialized stream accepting a sequence of arguments
# As an illustration we will consider the row from the string trio opus. 45 by arnold schoenberg
# Let's define a variable named Trio row and initialize it with a row object.
# We provide a list of strings to denote pitch classes adhering to the custom re-representation in music21.
# Sharp == '#'; Flat == '-'
#trio_row_1 = serial.ToneRow(['C', 'G#', 'C#', 'G', 'D', 'B', 'A', 'F#', 'E', 'F', 'E-', 'B-'])
# A Stream representation of a tone row, or an ordered sequence of pitches; 
## can most importantly be used to deal with serial transformations.
# Unlike a normal Stream, the first argument is assumed to be a ToneRow, a list
# An alternative strategy would be to leverage integers ranging from 0 to 11
#trio_row_2 = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10])
#trio_row.show()
# Let's utilize this in the ambigram project
# Within the context of the 12 tone technique this fundatmental incarnation of the row is commonly refered to as prime form
# By applying transposition along with specific operations upon it, composers can generate multiple derrived versions.
## Inverting each interval within the row gives us inverion
## Reversing the order of pitches creates a retrograde form
### The simultanous operation of inversion and retrograde yields the retrigrade inversion

# in music21 we can invoke the zero-centered transformation method to create versions of a row derrived by such operations
# The method() accepts a string parameter that specifies the desired transformation type
# The transformation type representations are P for Prime, I for Inversion, R for Retrograde or RI for Retrogade Inversion
# Additionally the method expects an integer parameter representing a pitch class which serves as the basis for the transposition
#transformed_row = trio_row_2.zeroCenteredTransformation('RI', 0)
# In the "zero-centered" convention, the transformations Pn and In start on the pitch class n, and the transformations Rn and RIn end on the pitch class n.
#transformed_row.show()

# Let's create a main() enclosure

from music21 import *
# Kindly follow the these regulation for accurate nesting.
'''
It is best practice is to create structures where the TimeSignature goes in the first Measure of the score, as below:

>>> s = stream.Score()
>>> p = stream.Part()
>>> m1 = stream.Measure()
>>> ts = meter.TimeSignature('3/4')
>>> m1.insert(0, ts)
>>> m1.insert(0, note.Note('C#3', type=('half'|(2*0.25)))
>>> n = note.Note()
    n.pitch=pitch.Pitch()
    n.duration=duration.Duration()
>>> m1.insert(1.0, n)
>>> m1.number = 1
>>> p.insert(0, m1)
>>> s.insert(0, p)
>>> s.show('t')
'''
import random

def main():
    trio_row = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10])
    #transformed_row = trio_row.zeroCenteredTransformation('RI', 0)

    # Select a transformation of pitches, let's assign our custom function with trio_row passed in into local variable melodic_row and show()
    if False:
        melodic_row = random_row_transform(trio_row)
        melodic_row.show()
    # The output of our function while aligned with our objective is limited solely to pitch series transformation
    # To generate composition of greater interest and depth we must broaden the scope of our progam to Encompass additional musical parameters
    # Consequently our focus will shift to how we might manipulate and integrate rhythmic elements within our pitch series
    # One avenuw we might explore to achieve this is the application of serial techniques to the domain of rhythm
    # Interpreting the 12 integers employed to represent pitch classes as durations is a straightforward process
    # We initially must establish a minimum duration such as a 32th note which will be assigned to the integer 0
    # We shall increment the duration by another 32th note for each subsequent integer to form a durational series
    # Leveraging the scale we can generate a durational row and apply the same operation we utilized on the tonerow mod
    # Let's introduce another function called cereal melody
    
    #treble_line = stream.Stream()

    # Now let's manifest our serial_melody() function by passing in the trio_row and respective arguments
    # Then finally let's assign it into our treble_line empty stream and show() it
    ## Correction: Don't create another stream object serial_melody() will return a stream already
    if True:
        treble_line = serial_melody(trio_row, 0.125, (4, 6))
        treble_line.show()
    
# Serial melody will generate a melodic line based on two randomly selected tranformation from our row
# One transformation will determine the pitches while the other will dictate durations
# The function will expect a ToneRow object as its initial parameter and a float as its second parameter
# The float will represent the minimum duration for the notes comprising the melody
# Additionally it will require a tuple of two integers as it's third parameter to specify limits for the lower and upper octave values of our melody
# It will help to infuse further variety into the melody to random octave displacement
# The function will return a music21 stream object which represents the sequence of musical elements within our melody
def serial_melody(row: serial.ToneRow, duration_unit: float, octave_range: tuple[int, int]) -> stream.Stream:
    '''
    Creates a melody by combining a tone row with a durational series.
    '''
    # First, let's initialize a stream to contain the melody
    # This object(It's dragging music21 library object from class stream:) will contain our serial melody 
    
    melody = stream.Stream()

    # To determine a pitch sequence we'll invoke our own random_row_transformation() passing the row mold, the arg of this custom fuction
    # So our custom function will be dealt similarly to other function inside this block which is also our own function
    pitch_row = random_row_transform(row)

    # Let's define another local variable duration_row , which is same as pitch_row but transformed to get the int representation of pitch classes
    # For this we will additionally add the method pitchClasses() on it
    duration_row = random_row_transform(row).pitchClasses()
    # pitchClasses() is a Convenience function showing the pitch classes of a ToneRow as a list.

    # We will procede by creating a melody within a for loop
    # we will enumerate over the elements within pitch_row to get both index and iterator pitch_class
    # Correction: pitch_class is an object, we gotta apply pitchClasses to make it a list
    # We can use duration_row but why not enjoy the one additional scope of randomness
    for i, pitch_class in enumerate(pitch_row.pitchClasses()):
        # Let's create a duration object with duration_unit multiplied by duration_row[i], the similarly(similar to the index of current iteration) indexed element of duratio_row.
        ## then let's assign this duration.Duration() object to the .duration attribute of our iterator
        # Correction: The iterator here is an int which does not have duraion and octave attributes.
        ## First we need to make a picth object using the pitchClasses value in pitch_class as input 
        p = pitch.Pitch(pitch_class)
        # Now let's create a note object using this p which will have duration and octave attributes
        n = note.Note(p)
        # Now let's assign duration to n similarly
        n.duration = duration.Duration(duration_unit * (duration_row[i]+1))
        # (duration_row[i]+1)) because all the python indexing starts at 0 by convention
        # A Duration represents a span of musical time measurable in terms of quarter notes (or in advanced usage other units). 
        # A Duration object is made of one or more immutable DurationTuple objects stored on the components list. 

        # Let's randomly assign an octave using the randInt function from random
        # The randint function requires two arguments, the bounds of random int to be generated
        # In this case we will use the octave_range argument as input
        # as it is a touple we need to unpack it with an aesterisl
        #pitch_class.octave = random.randint(*octave_range)
        ## Correction: we need to use n inplace of pitch_class and add class .pitch
        n.pitch.octave = random.randint(*octave_range)

        # Finally let's append the pitch_class iterator with unique controled randomized pitch identifiers utilizing the random_row_transform() on each iteration.
        #melody.append(pitch_class)
        # Correction: Let's append n in place of pitch_class
        melody.append(n)
        # As first arg of our custom function we will already be applying serial.ToneRow method to a input row
        # We will also be inputing scope for our custom duration_unit and octave_range parameters to utilize the power of .duration and .octave attributes of individual note objects in each iteration.
        # By appending the note objects to the stream object melody we are updating the musical dataset with additional notes using our random .duration and .octave on each iteration
    
    # In the end we are returning an updated, filled version of empty stream object [like coll in max] as the output of our custom function
    return melody
    # Let's go back to main() block and introduce a new stream object into treble_line
    # This is wrong, will break your code

# Within our program we shall leverage the transformative operations applied to our tone r
# Thus we shall derive a linear sequences of pitches fo composition
# The order of transformation could be determined by a myriad[chief number of things tends to infinity] of potential strategies.
# We might opt to incorporate various constraints or base our decision on an analysis of the row's intervalic structure
# For the purpose of this demonstration we shall embrace a randomized aproach
# To embrace a randomized aproach we can access a variety of functions under the module random


# Now let's define a function called random_row_transform() 
# It will take as input a ToneRow object andreturns as output a randomly transformed row
def random_row_transform(row: serial.ToneRow) -> serial.ToneRow:
    # Here we are performing the ToneRow() method in the arg input where,
    ## arg has serial.ToneRow enabled where we will input a list of numbers in the main() block
    ## the second part of the operation is defined within this block usinf random library where we manipulate the input of zeroCenteredTransformation using choice and randrange
    # Basically we are specifying the input of our custom func
    '''
    Selects a random row form and transposition and returns the transformed row
    '''
    # Within this function we need to select a row form from prime inversion retrograde and retrograde inversion
    # choice() chooses a random element from a non-empty sequence.
    # It is represented as P, I, R and RI 
    # To return an element of random let's use the random.choice() functions and assign it to local variable row_form
    row_form = random.choice(['P', 'I', 'R', 'RI'])

    # To select a pittch class on which our row will be transposed we will use randrange() function
    # Choose a random item from range(stop) or range(start, stop[, step]).
    # It will select a random integer from our specified range 0 to 11 and assign them to local variable row_index
    row_index = random.randrange(0, 11)

    # To complete the function we will return row.zeroCenteredTranformation() and put our variables as inputs
    # row comes from the input constructor of our def function, like the self arg of class object methods
    return row.zeroCenteredTransformation(row_form, row_index)
    # Now let's test this within our main() function

if __name__ == '__main__':
    main()



