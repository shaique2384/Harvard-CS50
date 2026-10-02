from music21 import *
import random
import copy

def main():
    trio_row = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10])
    ATScore = stream.Score()
    treble_part = stream.Part()
    bass_part = stream.Part()
    
    s = serial_melody(trio_row, .5, (4, 6))
    b = (random_pitch_transform(s))
    recursed_s = s.recurse()
    recursed_b = b.recurse()
    
    for i, n in enumerate(recursed_s.notes):
        if i % 4 == 0:
            s_measure = stream.Measure()
            vs = stream.Voice()
            s_measure.insert(0, vs)
            treble_part.append(s_measure)        
        print(f"Index {i} | Note: {n.nameWithOctave} | Duration: {n.duration.quarterLength}")
        vs.append(n)
            
    for i, n2 in enumerate(recursed_b.notes):
        if i % 4 == 0:            
            b_measure = stream.Measure()
            vb = stream.Voice()
            if i == 0:
                b_measure.insert(0, clef.BassClef())
            b_measure.insert(0, vb)
            bass_part.append(b_measure)
        n2 = n2.transpose(-12)
        vb.append(n2)

    ATScore.insert(0, treble_part)
    ATScore.insert(0, bass_part)
    ATScore

def random_pitch_transform(melody: stream.Stream) -> stream.Stream:
    melody_transformed = stream.Stream()
    melody_pitch_list = melody.pitches
    pitch_only_row = serial.ToneRow(melody_pitch_list)
    transformed_pitch_row = random_row_transform(pitch_only_row).pitchClasses()    
    for i, note in enumerate(melody.notes):
        new_note = copy.deepcopy(note)
        new_note.pitch = pitch.Pitch(transformed_pitch_row[i])
        melody_transformed.append(new_note)
        print(f"Index {i} | Note: {note.nameWithOctave} | Duration: {note.duration.quarterLength}")
    return melody_transformed
    
def serial_melody(row: serial.ToneRow, duration_unit: float, octave_range: tuple[int, int]) -> stream.Stream:
    melody = stream.Stream()
    pitch_row = random_row_transform(row)
    duration_row = random_row_transform(row).pitchClasses()
    for i, class_number in enumerate(pitch_row.pitchClasses()):
        p = pitch.Pitch(class_number)
        n = note.Note(p)
        n.pitch.octave = random.randint(*octave_range)
        n.duration = duration.Duration(duration_unit * (duration_row[i] + 1))    
        melody.append(n)
    return melody    

def random_row_transform(row: serial.ToneRow) -> serial.ToneRow:
    row_form = random.choice(['P', 'I', 'R', 'RI'])
    row_index = random.randrange(0, 11)
    return row.zeroCenteredTransformation(row_form, row_index)
   
if __name__ == '__main__':
    main()