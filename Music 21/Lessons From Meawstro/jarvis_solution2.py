from music21 import *
import random
import copy

def main():
    trio_row = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10])
    Grand_Score = stream.Score()
    
    # 1. Generate serial streams (S -> A -> T -> B)
    s = serial_melody(trio_row, 0.5, (4, 6))
    a = random_pitch_transform(s)
    t = random_pitch_transform(a)
    b = random_pitch_transform(t)
    
    # Helper to construct 4-note measure-segmented parts
    def build_voice_part(stream_input, octave_target):
        part = stream.Part()
        current_measure = None
        for i, n in enumerate(stream_input.notes):
            if i % 4 == 0:
                current_measure = stream.Measure()
                part.append(current_measure)
                
            n_copy = copy.deepcopy(n)
            n_copy.pitch.octave = octave_target
            current_measure.append(n_copy)
        return part

    # 2. Build individual SATB voice parts
    soprano_part = build_voice_part(s, 5)
    alto_part = build_voice_part(a, 4)
    tenor_part = build_voice_part(t, 3)
    bass_part = build_voice_part(b, 2)

    # 3. Combine & Chordify Soprano + Alto into Treble Staff
    SA_score = stream.Score()
    SA_score.insert(0, soprano_part)
    SA_score.insert(0, alto_part)
    
    treble_clef_part = SA_score.chordify()
    #treble_clef_part.id = 'Treble Staff (S+A)'
    treble_clef_part.insert(0, clef.TrebleClef())

    # 4. Combine & Chordify Tenor + Bass into Bass Staff
    TB_score = stream.Score()
    TB_score.insert(0, tenor_part)
    TB_score.insert(0, bass_part)
    
    bass_clef_part = TB_score.chordify()
    #bass_clef_part.id = 'Bass Staff (T+B)'
    bass_clef_part.insert(0, clef.BassClef())

    # 5. Assemble Grand Score
    Grand_Score.insert(0, treble_clef_part)
    Grand_Score.insert(0, bass_clef_part)
    
    Grand_Score.show()

def random_pitch_transform(melody: stream.Stream) -> stream.Stream:
    melody_transformed = stream.Stream()
    melody_pitch_list = melody.pitches
    pitch_only_row = serial.ToneRow(melody_pitch_list)
    transformed_pitch_row = random_row_transform(pitch_only_row).pitchClasses()    
    
    for i, n in enumerate(melody.notes):
        new_note = copy.deepcopy(n) # Duration preserved via deepcopy
        new_note.pitch = pitch.Pitch(transformed_pitch_row[i])
        melody_transformed.append(new_note)
        
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