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
my_note=note.Note()
# Our current focust==rhythm. So .pitch==default
my_note.duration=duration.Duration(3.25)
# We have so far dealt with 1/2^n as note length.
# But we havent yet worked with any duration that breaks away from this conventional mold.

my_measure.insert(0,my_note)

# Conclusion Block [HARD]
my_part.insert(0,my_measure)
my_stream.insert(my_part)

my_stream.show('musicxml.png', fp='7_tuplet_rhythms.py')