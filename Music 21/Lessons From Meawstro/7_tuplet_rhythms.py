if False:
    from music21 import*

    # Our current focust==rhythm. 
    # So Note Instance Assignment with .pitch='C4' and .duration=2[quarternotes]
    my_note=note.Note(duration=duration.Duration(2))
    my_note=note.Note()

    # Our current focust==rhythm. So .pitch='C4' and .duration=2[quarternotes]
    my_note.duration=duration.Duration(2)

    # Let's create a stream object and inside the stream object let's insert a meter.TimeSigna() which allows us inputing complex meters and music21 adds ties automatically
    my_stream=stream.Stream()
    my_stream.insert(meter.TimeSignature())
    # Insert Inserts an item(s) at the given offset(s). A review of the library happened;

import os
os.environ["DISPLAY"] = ":99"

import music21 as m21
m21.environment.set('musescoreDirectPNGPath', '/usr/bin/mscore3')
from music21 import*
'''
The TimeSignature object represents time signatures in musical scores (4/4, 3/8, 2/4+5/16, Cut, etc.).

TimeSignatures should be present in the first Measure of each Part that they apply to. Alternatively you can put the time signature at the front of a Part or at the beginning of a Score, and they will work within music21, but they won't necessarily display properly in MusicXML, Lilypond, etc. So best is to create structures where the TimeSignature goes in the first Measure of the score, as below:

>>> s = stream.Score()
>>> p = stream.Part()
>>> m1 = stream.Measure()
>>> ts = meter.TimeSignature('3/4')
>>> m1.insert(0, ts)
>>> m1.insert(0, note.Note('C#3', type='half'))
>>> n = note.Note('D3', type='quarter')
>>> m1.insert(1.0, n)
>>> m1.number = 1
>>> p.insert(0, m1)
>>> s.insert(0, p)
>>> s.show('t')
'''
# Let's Follow above regulations.

# Introfuction Block [HARD]
my_stream=stream.Stream()
my_part=stream.Part()
my_measure=stream.Measure()
my_ts=meter.TimeSignature('3/4')
my_measure.insert(0,my_ts)
#my_measure.number=16

# Body Block [SOFT]
# Each body block should have mechanisms as sub blocks. For us we are creating different kinds of notes assigning functionalities to them and inserting into my_measure.

if True:
    my_note=note.Note()
    # Our current focust==rhythm. So .pitch==default
    my_note.duration=duration.Duration(3.25)
    my_measure.insert(0,my_note)

# We have so far dealt with 1/2^n as note length.
# But we havent yet worked with any duration that breaks away from this conventional molds.
# Let's create something using tuplets, 3 1/3 notes
if True:
    nBase3=note.Nore()
    nBase3.duration=duration.Duration(1/3)
    #my_measure.repeatAppend(mBase3, 3)
    my_measure.repeatInsert(nBase3, 3)

# We can easily extend this aproach to other tuplet durations, in this case quintuplets.
# Let's now create three quintuplet note objects and let's assign to their duration.Duration() using keyword duration.
if True:
    n1=note.Note(duration=duration.Duration(1/5))
    n234=note.Note(duration=duration.Duration(3/5))
    n5=note.Note(duration=duration.Duration(1/5))
    my_measure.insert(n1,n234,n5)

# We discover in music21 the remarkable ability to wield rhythm with great flexibilty through tuplets such as 5 subdivisions within the customary span of 4.
# We might however wish to push the bounderies further still with the subdivision of five within the space of three or seven within the space of five leading us into the territory of what some call irrational rhythms a terrain often traversed by   those Avant Guard composers like Brian Ferow, James Dylan and Michael Finnessy who are associated with the so called new complexity movement. 
#In music21 tuplets are defined by their own dedicated class and we can utilize it to create tuplets with even more control and flexibility.
# Let's translate a traditional composer's 'workflow into the realms of python and music21 and show strength as well as limitations.
if True:
    # Let's first create a tuplet object called my tuplet and as arguments let's provide integer values of five and three; representing the number of subdivisions we desire and the number of usual subdivisions.
    my_tuplet=duration.Tuplet(5,3) 
    # It's an object inheriting from the duration class and objects.
    # Whenever we introduce an irrational rhythm it is customary to display their ratio in notation within brackets above so.
    # We can do this by introducing the tupletNormalShow attriput of the tuplet object and assign 'number'
    my_tuplet.tupletNormalShow='number'
    # We have a tuplet object but we don't have a note yet so let's create one into niTuplet short for noteIrrationalTuplet 
    niTuplet=note.Note()
    # The note automatically has a default duration object nested and we can easily append our tuplet object into the notes duration attribute[somehow the duration object and variables are nested in the class bock, I don't knopw yet] using appendTuplet().
    niTuplet.duration.appendTuplet(my_tuplet)
    # Let's now repeatAppend and repeatInsert niTuplet into my_measure and check while running in codespace which one works and to what extent.
    my_measure.repeatAppend(niTuplet, 5)
    # repeatAppend() has (items, numberOfTimes) as args
    my_measure.repeatInsert(niTuplet, 5)
    # repeatInsert() has (items, offsets) as args so it should mess up.
    # Let's find out which stream objects allow append and which allow only inserts.


# Conclusion Block [HARD]
my_part.insert(0,my_measure)
my_stream.insert(my_part)

my_stream.write('musicxml.png', fp='7_tuplet_rhythms2.png')
my_stream.write('musicxml.png', fp='7_tuplet_rhythms2.musicxml')
