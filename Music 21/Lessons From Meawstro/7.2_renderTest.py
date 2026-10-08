if False:
    import music21
    
    # Create your stream
    my_stream = music21.converter.parse('tinyNotation: 3/4 c4 d e f2.')
    
    # Export as MusicXML (creates output.xml in your working directory)
    my_stream.write('musicxml', fp='output.xml')
    
    # Export as MIDI
    my_stream.write('midi', fp='output.mid')
    
    print("Export complete!")

if True:
    from music21 import *
    
    my_score = stream.Score()
    my_part = stream.Part()
    my_measure = stream.Measure()
    my_ts=meter.TimeSignature('3/4')
    my_measure.insert(0,my_ts)
    
    # Safe note declaration
    my_note = note.Note('c4', quarterLength=4.0)
    
    # Appending builds the time sequence automatically
    my_measure.insert(my_note)
    my_part.insert(my_measure)
    my_score.insert(my_part)
    
    my_score.write('musicxml', fp='output.xml')
    my_score.write('midi', fp='output.mid')
    
    for element in my_score.recurse():
        print(element)
    
    print("Export complete!")
    

