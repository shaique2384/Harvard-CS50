from music21 import *
import random
import copy



def main():
    trio_row = serial.ToneRow([0, 8, 1, 7, 2, 11, 9, 6, 4, 5, 3, 10, 7, 2, 11, 9, 6, 4, 5, 3])
    Grand_Score = stream.Score()
    SA_chord = stream.Score()
    TB_chord = stream.Score()
    
    s = serial_melody(trio_row, 0.25, (4, 6))
    a = random_pitch_transform(s)
    t = random_pitch_transform(a)
    b = random_pitch_transform(t)

    soprano_part = process_voice(s, 5)
    alto_part = process_voice(a, 4)
    tenor_part = process_voice(t, 3)
    bass_part = process_voice(b, 2)

    SA_chord.insert(0, soprano_part)
    SA_chord.insert(0, alto_part)
    SA_part = SA_chord.chordify()
    SA_part.insert(0, clef.TrebleClef())
    TB_chord.insert(0, tenor_part)
    TB_chord.insert(0, bass_part)
    TB_part = TB_chord.chordify()
    TB_part.insert(0, clef.BassClef())
    Grand_Score.insert(0, SA_part)
    Grand_Score.insert(0, TB_part)
    Grand_Score.show()



def process_voice(melody_stream_input, octave_target: int):
    part = stream.Part()
    measure_fill = 0.0
    current_measure = None
    for i, n in enumerate(melody_stream_input.notes):
        if i % 4 == 0:
            current_measure = stream.Measure()
            current_voice = stream.Voice()
            current_measure.insert(0, current_voice)
            part.append(current_measure)
            measure_fill = 0.0       
        n_copy = copy.deepcopy(n)
        n_copy.pitch.octave = octave_target
        remaining_in_measure = 4.0 - measure_fill
        if n_copy.quarterLength > remaining_in_measure and remaining_in_measure > 0:
            n_copy.quarterLength = remaining_in_measure
        measure_fill += n_copy.quarterLength
        current_voice.append(n_copy)
    return part    



def random_pitch_transform(melody: stream.Stream) -> stream.Stream:
    melody_transformed = stream.Stream()
    melody_pitch_list = melody.pitches
    pitch_only_row = serial.ToneRow(melody_pitch_list)
    transformed_pitch_row = random_row_transform(pitch_only_row).pitchClasses()        
    for i, n in enumerate(melody.notes):
        new_note = copy.deepcopy(n) 
        new_note.pitch = pitch.Pitch(transformed_pitch_row[i])
        melody_transformed.append(new_note)
        print(f'Transformed Pitch Class Note: {new_note.name} | Duration: {new_note.duration.quarterLength}')        
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