# Let's import the library
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

if False:
    # let's assign a chord object to my_chord local variable
    chord.Chord()
    # A Chord functions like a Note object but has multiple pitches.
    # Create chords by passing a list of strings of pitch names
    my_chord = chord.Chord(['C4', 'E4', 'G4'])
    # we can also provide a list of intergers ranging from 0 to 11 representing pitch classes within the chromatic scale
    my_chord_pc = chord.Chord([0, 4, 7])
    # if the list contains integer greater thatn 11 they will be interpreted as as midi numbers
    # We can also append note objects
    # My block
    if False:
        notes = []
        p1 = 60
        for i in range(100):
            p2 = p1+4
            if p2 -60 <= 24:
                print(p1, p2)
                n1, n2 = note.Note(p1), note.Note(p2)
                notes.append(n1)
                notes.append(n2)
                p1 = p2+3
            else:
                break

        my_chord_listedNotes = chord.Chord(notes)
        my_chord_listedNotes.show()

    # We can also invoke the add method, it's almost like the append method of list objects
    my_chord.add('A5')
    #my_chord.duration = duration.Duration(4)
    #my_chord.show()
    # We can also use this method to merge two chords into one
    # Let's define at first and then pass its .pitches attribute into the .add() method of the first chord
    my_chord2 = chord.Chord(['E5', 'G5', 'B5'])
    my_chord.add(my_chord2.pitches)
    my_chord.remove('G5')
    # Two ways of changing the duration
    ##
    my_chord.quarterLength = 8
    ##
    my_chord.duration = duration.Duration(2)

    # The chord object has a range of attributes and methods which can be called upon to yield valuable harmonic insights
    # Let's utilize .isTriad() and .isSeventh() method which gives us a string which we can print
    print(my_chord.isTriad()) 
    print(my_chord.isSeventh())
    # Questions give booleans which we can use as triggers like in max

    # .root() method gives us the root from the set of notes
    print(my_chord.root())

    # .commonName attribute returns the most commonly associated name of the triad providing us where applicable
    print(my_chord.commonName)
    print(my_chord.pitchedCommonName)

    # In the context of post-tonal analysis several attributes and methods such as,
    ## Forte class, interval Vector, normal order and get Z relation proved particularly useful for conducting pitch class set analysis
    print(my_chord.forteClass)
    print(my_chord.intervalVector)
    print(my_chord.normalOrder)
    print(my_chord.getZRelation())

#my_chord.show()

# Let us explore chordify, another unique feature of music21 that can be employed to distill a complex score
# The score can comprise multiple parts and chorify renders a sequence of chords within a sinfle part
# To demonstrate this, let's at first pass a music xml file containing the first movement of bethoven's seventh string quartet
# It exists within music21's bundled corpus, let's pass it to a variable
bethoven_quartet = corpus.parse('beethoven/opus59no1/movement1.mxl')

# Now let's chorify
quartet_chords = bethoven_quartet.chordify()
# It creates a chordal reduction of polyphonic music, where each change to a new pitch results in a new chord. 
# If a Score or Part of Measures is provided, a Stream of Measures will be returned. 
# If a flat Stream of notes, or a Score of such Streams is provided, no Measures will be returned.

# We can obtain a new stream where in all the notes and rests are gathered into chord objects
# show() the quartet chord
quartet_chords
# Upon close inspection we can see that chordify has dilligently crafted a new chord for wach vertical sonority
# It is important to recognize that some of the chords created may Encompass functional harmony whereas others might harbor non-harmonic tones such as,
## Passing notes, appoggiaturas, changinf notes, suspensions and various other embelishments
# Therefore it is incumbent upon the analyst to embark on further investigations to determine the true harmonic content of the work
# Chordify serves as a powerful launchpad for the pursuit of deeper harmonic analysis
bethoven_quartet.show()
# Let's comeback today and proceed on a new file by terminaling code 7Complex_rhythm_withTuplets.py