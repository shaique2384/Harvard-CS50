# This is an introduction to music 21, a powerful tool developed by MIT using python to help reasearchers, musicians and students to analyze and create music
# let's import the package [if we imported it using standard method we would have to use music21. everytime]
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

# music21 is based on the concepts of musical objects such as note, chord, stream, part and score representing different elements of a piece of music
# each has properties and methods which allows use to manipulate and analyze music in a variety of ways
n = note.Note('C4')
# C4 is the middle C and n.name gives us note's name and n.octave gives us its octave
print(n.name)
print(n.octave)
# we can also use sub attribute frequency with pitch
print(n.pitch.frequency)
# by default the duration of the note object is one quarter note or crotchet, n.quarterLength gives us an eighth note
n.quarterLength = 2
# we can view the notes in notation softwares such as MuseScore by calling the show() method
n.show()
# the stream class is one of the most important class of music21
# it is thought of a container of notes, chords and otherr musical objects
# let's create a stream object, s
from music21 import *
s = stream.Stream()
# now we can use its append method to add objects to it
s.append(meter.TimeSignature('3/4'))
# let's use append to add some note objects, order matters. But can we catenate on one? obviously check the module files
s.append(note.Note('C4'))
s.append(note.Note('D4'))
s.append(note.Note('E4'))
# now let's add show method
s.show()