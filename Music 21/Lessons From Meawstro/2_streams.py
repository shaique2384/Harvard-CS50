# stream object function is a container function for the assortment of other musical objects
# musical objects being notes, rests and time signatures but also has the capability of storing other stream objects
# It provides an effective and efficient means of organizing musical ideas and compositions
# let's work on it's crucial sub classes like voice, part and score
# these sub classes can also be considered musical containers each with it's unique purpose and functionality
# how these classes can be employed to effectively in musical structures in music21
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
    # Create a score object to hold all the musical parts and measures. [stream is like an empty list = [], hence append works]
    score = stream.Score()
    # The largest containing Stream in a piece could be a generic Stream, or a Part, or a Staff. 
    # The Stream Maxima
    # And Scores can be embedded in other Scores 
    # Developer's original thought was to call this class a Fragment because of this possibility of continuous embedding
    # Embedding is basically nesting, i.e, Opus containing 24 piano preludes
    # I like Fragments tho, more modular
    # score object acts as a blank slate onto which we can add our other voices or parts[fragments]

    # Create a part object to represent a single instrument or vocal part; the module here is the stream, a stream of data as music happens in time
    part = stream.Part()

    # Create a part object to represent a bass part. 
    # We are just creating empty containers where we will append materials later
    # We are just defining variables like a mathmatical equation
    bass_line = stream.Part()

    # to create musical lines within a single part we need a voice object
    # a voice object is a specialized kind of stream that can be used to help represent multiple overlapping musical ideas or layers within a single staff
    # Let's create a part with two voices, one for the melody and the other for the harmony [remember streams are like empty lists]
    voice1 = stream.Voice()
    voice2 = stream.Voice()

    # to represent a simple C maj scale as a melody we'll add some notes to the voice of one object
    # We'll use a list called notes which holds note names as strings
    notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    # remember for future you wanna use midi values for notes and use numpy, matrix or tensors to manipulate data

    # Create a note object for each note using a for loop and append it to voice1 in each iteration
    for notename in notes:
        melody_note = note.Note(notename)
        # We can manipulate duration and velocity arg parameters of Note() method using more loops and create systems of generation
        voice1.append(melody_note)

        # we will create some harmony notes and add them to voice2 inside the same loop
        # to create a harmony note for each melody note we shall utilize the note object's transpose method.
        # With this method we will create a new note that is a specific interval away from the original note
        # For this case the interval would be 8 half steps I.E a minor sixt lower than the melody note
        # then will will append each harmony note to voice2
        harmony_note = melody_note.transpose(-8)
        voice2.append(harmony_note)

        # lastly let's create a bass note using the octave property[it only takes integer, it's not a function so no parentheses in octave()] and append it to the bass voice
        bass_note = note.Note(notename)
        bass_note.octave -= 2
        # octave property return or set the octave value from the Pitch object. It takes in integers
        # -= operator in python is a subtraction assignment operator [x = x - 5] == [x -= 5]
        bass_line.append(bass_note)

    # Let's append voice objects to their relevant parts
    # next we can append both voice objects to the first part object [a stream] 
    # we will pass a list that contains voice1 list and and voice2 list
    part.append([voice1, voice2])

    # we have already saturated the bass_line part object at end end of the for loop with every iteration
    # Now let's insert both the part objects into the score object and specify a time offset of zero [The Unit: music21 measures offsets using Quarter Lengths (where 1.0 equals one quarter note)]
    # we can use time offset to create fuges
    # if item is passed then python looks inside the first items for their internal native offsets
    # ignoreSort=False (Default): Every time you insert a note or part, music21 instantly resorts the entire score chronologically. This guarantees that if you immediately call a method or print a list of notes, everything is in perfect musical order
    # ignoreSort=True: This tells music21 not to sort the container immediately.
    # When to use it: If you are writing a script that loops through and inserts thousands of notes into a massive score all at once. 
    # Setting this to True prevents Python from performing thousands of heavy sorting operations. 
    # You can manually call .elementsChanged() or let music21 auto-sort everything right at the very end of your script to drastically save processing time.
    # setActiveSite (Defaults to True)This handles the low-level relational tracking between musical objects in Python's memory hierarchy.
    # What is a "Site"?: In music21, a musical element (like a specific middle C note) can simultaneously exist in multiple contexts (e.g., inside a specific Measure, inside a Part, and inside a global Score). 
    # The activeSite attribute tells the note object which container it currently considers its "home base".
    # setActiveSite=True (Default): When you insert the element into the Score, the element's internal tracking pointer shifts so that it acknowledges this specific Score as its active environment. 
    # This ensures that if you query properties like .offset directly on that note object, it returns its position relative to this container.
    # setActiveSite=False: The element is successfully placed into the Score container, but the element itself does not switch its primary internal reference pointer to this score. 
    # This is typically reserved for specialized backend processing or advanced manipulation where you want an object to stay tethered to a previous context.
    if True:
        score.insert(0, part)
        score.insert(0, bass_line)

        score.show()

    # The voice part and score subclasses play adistinct role in structuring musical compositions.
    # It offers versatile and effective way to compose music. 
    # Through creation of a score object as the top level container [compare levels of schenkerian analysis to the levels of coding] and the addition of part objects containing their additional voice objects to represent intricate and multilayered musical pieces

    # I feel like the utility of the libray depends on it's modularity. If I can manipulate better using the same mechanism using basic python functions then it's a bad library
    # Let's find out if it's good or bad

# now cleaner version

if False:
    from music21 import *

    score = stream.Score()
    part = stream.Part()
    bass_line = stream.Part()
    voice1 = stream.Voice()
    voice2 = stream.Voice()
    notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    for notename in notes:
        melody_note = note.Note(notename)
        voice1.append(melody_note)
        harmony_note = melody_note.transpose(-8)
        voice2.append(harmony_note)
        bass_note = note.Note(notename)
        bass_note.octave -= 2
        bass_line.append(bass_note)
    part.append(voice1)
    part.append(voice2)
    score.insert(0, part)
    score.insert(0, bass_line)

    score.show()


# Gemini Helped with it
from music21 import *

score = stream.Score()
part = stream.Part()
bass_line = stream.Part()

notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Track current measures for both tracks
# current_m_upper = None
# current_m_bass = None

for i, notename in enumerate(notes):
    # Every 4 notes (index 0, 4, etc.), build a fresh container block
    if i % 4 == 0:
        # 1. Create upper measure and its distinct local voices
        current_m_upper = stream.Measure()
        v1 = stream.Voice()
        v2 = stream.Voice()
        
        # 2. Insert the fresh voices into this specific measure
        current_m_upper.insert(0, v1)
        current_m_upper.insert(0, v2)
        part.append(current_m_upper)
        
        # 3. Create the matching bass measure
        current_m_bass = stream.Measure()
        if i == 0:
            current_m_bass.insert(0, clef.BassClef())
        bass_line.append(current_m_bass)

    # --- Note Processing Stage ---
    # Append to the currently active v1 voice
    melody_note = note.Note(notename)
    v1.append(melody_note)

    # Append to the currently active v2 voice
    harmony_note = melody_note.transpose(-8)
    v2.append(harmony_note)

    # Append to the currently active bass measure
    bass_note = note.Note(notename)
    bass_note.octave -= 2
    current_m_bass.append(bass_note)

# Add both fully-measured parts to the score
score.insert(0, part)
score.insert(0, bass_line)

score.show()

