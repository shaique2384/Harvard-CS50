''' @brugazoni Copy and paste this text into your IDE '''
from music21 import *
import random

def main():
    trio_row = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10])
    # Correction: Don't create another stream object serial_melody() will return a stream already.
    treble_line = (serial_melody(trio_row, 0.125, (3, 5)))
    treble_line.show()

def serial_melody(row: serial.ToneRow, duration_unit: float, octave_range: tuple[int, int]) -> stream.Stream:
    '''
    Creates a melody by combining a tone row with a durational series.
    '''
    melody = stream.Stream()
    pitch_row = random_row_transform(row)
    print(pitch_row)
    duration_row = random_row_transform(row).pitchClasses()
    print(duration_row)
    # Correction: pitch_class is an object, we gotta apply pitchClasses() to make it a list.
    # We can use duration_row but why not enjoy the one additional scope of randomness.
    for i, class_number in enumerate(pitch_row.pitchClasses()):
        # Correction: The iterator here is an int which does not have duraion and octave attributes.
        ## First we need to make a picth object using the pitchClasses value in pitch_class as input
        p = pitch.Pitch(class_number)
        # Now let's create a note object using this p which will have duration and octave attributes
        n = note.Note(p)
        # Correction we need to use n inplace of pitch_class and add class .pitch
        n.pitch.octave = random.randint(*octave_range)
        # Now let's assign duration to n similarly
        n.duration = duration.Duration(duration_unit * (duration_row[i] + 1))    
        print(f"Index {i} | Note: {n.nameWithOctave} | Duration: {n.duration.quarterLength}")
        # Correction: Let's append n in place of pitch_class
        melody.append(n)
    return melody    

def random_row_transform(row: serial.ToneRow) -> serial.ToneRow:
    '''
    Selects a random row form and transposition and returns the transformed row
    '''
    row_form = random.choice(['P', 'I', 'R', 'RI'])
    row_index = random.randrange(0, 11)
    return row.zeroCenteredTransformation(row_form, row_index)
   
if __name__ == '__main__':
    # Make sure to add extra sets of underscores before and after _name_
    main()


'''

from music21 import *
import random

def main():
    trio_row = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10])
    main_line = serial_melody(trio_row, 0.125, (3, 5))
    main_line.show()  # Prints ASCII score structure to terminal, or use main_line.show() for MuseScore

def serial_melody(row: serial.ToneRow, duration_unit: float, octave_range: tuple[int, int]) -> stream.Stream:
    '''
    #Creates a melody by combining a tone row with a durational series.
'''
    melody = stream.Stream()
    
    pitch_row = random_row_transform(row).pitchClasses()
    duration_row = random_row_transform(row).pitchClasses()
    
    print("Pitch Row:", pitch_row)
    print("Duration Row:", duration_row)
    
    for i, pitch_class in enumerate(pitch_row):
        p = pitch.Pitch(pitch_class)
        n = note.Note(p)
        n.pitch.octave = random.randint(*octave_range)
        n.duration = duration.Duration(duration_unit * (duration_row[i] + 1))
        
        print(f"Index {i} | Note: {n.nameWithOctave} | Duration: {n.duration.quarterLength}")
        melody.append(n)
        
    return melody

def random_row_transform(row: serial.ToneRow) -> serial.ToneRow:
    '''
    #Selects a random row form and transposition and returns the transformed row
'''
    row_form = random.choice(['P', 'I', 'R', 'RI'])
    row_index = random.randrange(0, 11)
    return row.zeroCenteredTransformation(row_form, row_index)

if __name__ == '__main__':
    main()
'''