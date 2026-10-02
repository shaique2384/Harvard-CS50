# Within western music duration is conventionally represented through a system of note values
# It delineates the relative length of each note
# in music21 this concept is adopted through a dedicated duration class
# Let's first import our music21 library
from music21 import *
# Kindly follow the this regulation for accurate nesting.
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
if False:
    # let's create a quarter note by creating a duration object which takes a float value
    dur = duration.Duration(1.5)
    # we can instantiate [The process of creating a specific, actionable realization (called an instance) of an abstract blueprint or data type],
    # an equivalent duration from a string representation of the note type and dots arg = 0, 1
    dur = duration.Duration(type = 'quarter', dots=1)

    # once we have a duration object we can use it to define the duration of a note or a rest object by assigning it,
    # to the object's duration attribute
    middle_c = note.Note('C4')
    # when we are adding .duration with middle_c at left side we are using it as a property, like the octave property
    # it's assignable
    middle_c.duration = dur
    middle_c.show()
    # show() can also be a method

# in common practice when we encounter durations that can not be represented by a single unit
# or when we need to split them across various beam groups or bar lines we typically resort to using tied notes
# it is also possible in music 21 but for that we need to create a new stream object first, stream.Stream() like lesson1
if False:
    from music21 import *

    s = stream.Stream()
    # let's define a time signature using the time signature class using the insert() method
    # here meter is a module, so mudules inside modules in different levels
    s.insert(meter.TimeSignature('4/4'))
    n = note.Note('F4')
    # it means assigning duration.Duration(5.25) to the duration property of the n variable as it already stored the note class with pitch 'F4'
    n.duration = duration.Duration(5.25)
    # let's call now insert() and show() methods that comes with the library
    s.insert(n)
    s.show()
    # we will observe a whole note tied across the bar line to a quarter note, then tied again to a 16th note


# The music21 object also provides several methods that allow for more flexibility in the way we notate durations
# let's consider the case where we want to notate the same duration with two ties notes in the first bar
if False:
    from music21 import *

    s = stream.Stream()
    s.insert(meter.TimeSignature('4/4'))
    n = note.Note('F4')
    n.duration = duration.Duration(5.25)
    # Now let's call n.splitAtQuarterLength(2) and storre in a variable, defining quarter note with float multiple is easier
    split_note1 = n.splitAtQuarterLength(2)
    split_note4 = n.splitByQuarterLengths([1, 1, 1, 2.25])
    # splitByQuarterLengths() takes input as a list of float numbers and split them in series to render notes as they are the multiples of quarter notes tied together
    # for splitByQuarterLengths() make sure that the sun of the floats equals to the float that was inserted in duration.Duration(). Otherwidse we will get music21.base.Music21ObjectException
    # instead of insert() we need to use append()
    # When you run n.splitAtQuarterLength(2), music21 doesn't give you back a single Note object. It gives you a Score or Stream containing multiple split and tied notes.
    # If you try to do s.insert(split_note), music21 would try to put the entire sequence of notes at the exact same starting point (beat 0), stacking them on top of each other like a chord.
    # On the other hand, s.append() works like adding items to the end of a timeline, like a series
    s.append(split_note4)
    s.show()

# to create rhythm in music21 we can combine individual note duration into sequences
# let's start by defining a list of floats called note values
from music21 import *

s = stream.Stream()
s.insert(meter.TimeSignature('4/4'))
# A list representing the durations of notes in a rhythmic sequence
note_values = [1.5, 0.5, 0.25, 0.25, 1] 
# how about fibonacci sequence as the data structure in list ;), 
# let's make a youtube video ;) idea is dibonacci sequence with 0<n<10 , some simple ratio  for pitch change
# after finishing the lessons
# we can utilize this in the data analysis-manipulation for carrying out and learning schenkeriyan analysis
# Main challenge is many disoersed syntaxes of music theory, goal would be to create building blocks, modularity and emergence using maths
# And also utilizing the different ptential and strengths of shchillinger systems, let's use gemini, the strength would be quantity of writing and quality og  supervision to create useful papers
# for the sake of this work let's iterate over our list using a for loops
for note_value in note_values:
    # within each iteration we will use s.apped to append a new note objects to the stream
    # Set the new duration to the current note value
    s.append(note.Note('C4', duration = duration.Duration(note_value)))
    # we will then assign each new note object with the same pitch 'C4' but note_value durations in series into the stream
# s.show()

# to edit our rhythm we can insert new note objects at any point within our stream by calling the insert and shift method
# to insert a single object we specify the offset using a float value to denote an offset measured in quarter notes from the begining of our stream
# and provide the object we want to insert as the second argument, ins this case
d1 = float(0.75)
new_note_1 = note.Note('C4', duration = duration.Duration(d1))
# insertAndShift() Inserts an item at a specified or native offset, and shift any elements found in the Stream to start at the end of the added elements.
# s.insertAndShift(2, new_note_1)
# to insert multiple objects into music21 stream at different offsets we can use the same insertAndShift method 
# We will need to use a list that alternates between the offsets and the objects we want to insert at those offsets
new_note_2 = note.Note('C4', duration = duration.Duration(0.25))
s.insertAndShift([2, new_note_1, (2+d1), new_note_2])
# We can insert and shift but it has to sum up or the code will break like the note should break
# if we insert multiple notes into the stream we need to input a list of inputes
s.show()
