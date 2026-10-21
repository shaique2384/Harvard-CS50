# @title 10_composing_with_harmonic_series
import random
# 2. Configure music21 environment settings to locate MuseScore
from music21 import*
from music21 import environment,converter
us = environment.UserSettings()
us["musescoreDirectPNGPath"] = "/usr/bin/mscore"

def main():
  '''Overtones'''
  if False:
    # Create a fundamental pitch
    fundamental=pitch.Pitch('A2')
    # Pitch objects have .getHarmonic() methods which takes i:int and returns ith harmonic.
    print(fundamental.getHarmonic(7))
    '''F#~5(+19c)'''
    n=note.Note(fundamental.getHarmonic(7),duration=duration.Duration(4))

    n.show()
    n.show('midi')
    # When notated pitch is rounded to the nearest quarter tone for us it is 3 quarter tone or 1 and a half semitone, discernable as F 3 quarter sharps.

  # Now suppose instead of a single pitch we want to encapsulate a larger posrtion of the harmonic series. The first 16 harmonics for example.
  if False:
    #Let's summon loop;
    fundamental=pitch.Pitch('C2')
    # Create 16 unique Note instances of the fundamental pitch to avoid StreamException redundancy. [n*16] or [n]*16 doesn't work.
    p2=stream.Part([note.Note(fundamental,duration=duration.Duration(4)) for i in range(1,4)], time=meter.TimeSignature('4/4'))
    # In Python, the range(start, stop) function generates numbers starting from start up to, but not including, stop
    p1=stream.Part([note.Note(fundamental.getHarmonic(i),duration=duration.Duration(1)) for i in range(1,17)],time=meter.TimeSignature('4/4'))
    s1=stream.Score([p1,p2])
    s1.show()
    s1.show('midi')


  # One potential aproach to harness the harmonic series for composition is to derive chords and harmonic sequences is to derrive chords and harmonic sequences from it's pitch structure.
  # Let's define a new function called chord_from_fundamental;
  if False:
    # Let's call chord_from_fundamental() with fundamenta;_pitch A1 and list of harmopnic_numbers=[5,6,7,9,12,15]
    my_chord=chord_from_fundamental(pitch.Pitch('A1'),[5,6,7,9,12,15])
    print(my_chord)
    '''<music21.chord.Chord C#4 E4 F#~4 B4 E5 G#5>'''
    my_chord.show()
    my_chord.show('midi')
    # As before the depiction of 7th harmonic as F#~4 or F 3 quarter sharp underscores the potential of the harmonic series to facilitate explore microtonality.
    # This unlocks intriguing composition possibilities but might not always align with our intentions or prove practical.

  # Some instrument prevalent in western music such as piano are confined to the 12 tpitches within the conventional chromatic scale.
  '''WE CAN CERTAINLY EXPAND UPPON TRADITIONAL TONAL VOICE LEADING SYNTAX BASED ON OVERTONES USING MICROTONALITIES TO FACILITATE COMPOSITIONS WITH TURKISH STRING INSTRUMENTS AND OUD ON TOP OF ATONAL MUCIS.'''
  '''WE CAN REINVENT CADENCE WITHIN THE MICROTONAL CELLS OR CONTEXTS'''
  # To account for western piano we will adapt our function by including an option to round pitches to their nearest semitone.
  # We will introduce a third argument called nearest semitone initialize as a boolean set by default to false within the for loop of our function after creating a pitch for the current harmonic but before adding it to our chord.
  # Let's create a new custom func chord_from_fundamentals for this;
  # Came back from the new chord_from_fundamentals def block and let's call it utilizing the new boolean kwargs;
  if False:
    my_chord=chord_from_fundamental2(pitch.Pitch('A1'),[5,6,7,9,12,15],nearest_semitone=True)
    print(my_chord)
    '''<music21.chord.Chord C#4 E4 G4 B4 E5 G#5>'''
    my_chord.show()
    my_chord.show('midi')
    # This time our chord is solely represented by the pitches within the chromatic scale with the seventh harmonic now rounded up to a gn.

  # Let's now explore how we might utilize the chord_from_fundamental function and produce an extended sequence of chords.
  # Within specific bounds each chord will be created with a randomized combination of harmonics and then transposed onto a predefined base pitch.
  # To achieve this we'll need to import python's random module.
  # Now in main() we shall Initialize a Part object to hold the chord sequence.
  chord_sequence=stream.Part()

  # Define a bassline as a list of pitch object
  bass_line=[pitch.Pitch(midi=(random.randrange(11)+48)) for i in range(9)]

  # Iterate through each bass_note in the bass_line
  for bass_note in bass_line:

    # To choose which harmonics should be included within the chord we'll use random.sample()
    # Generate a random set of 3-5 harmonnics between 4 and 20
    random_harmonics=random.sample(range(4,21),random.randrange(3,6))
    # This .sample() function when given an iterable as args[0] returns a new iterable containing randomly selected elements from the original iterable.
    # We will pass in range(4,20) as args[0] since the first four harminics are widely spaced and tend to give to much prominence to the fundamental pitch. 20 as upperlimit will give decent amount of tension and color before making things noisy.
    # args[1] determines the number of elements to be selected and therefore the number pitches within the chord.
    # We are assigning that as another randrange(3,6),<as we want chords ranging from 3 note clusters to 6 note clusters> to create nuances in the number of selected elements which we could otherwise hard assign by a constant number.

    # This random harmonics is the int list to plug in into the args[1], harmonic_numbers argument of our custom function chord_from_fundamental2.
    new_chord=chord_from_fundamental2(bass_note,random_harmonics)

    # Meowstro wants to transpose the clustures' lowest note to our bass_note to create harmonic series from new_chord[0]. We could render untransposed but in that case we would always get roots or fandamentals or .getHarmonic(0) as our lowest note. We don't want that, for composition we want more nuance.
    # Calculate the interval between the chord's lowest pitch and the bass_note
    transpose_by=interval.Interval(new_chord[0],bass_note)

    # To transpose our new_chord we shall invoke chord's transpose metheod and designate it's transposition level by passing our transposed_by variable as args[0].
    # To modify the existing chord instead of constructing a new instance we will set kwargs inPlace=True
    # Transpose the chord onto the bass_note
    new_chord.transpose(transpose_by,inPlace=True)

    # Assign random duration to the chord from quarterLength 2 and 4.
    new_chord.duration=duration.Duration(random.choice([2,4]))
    # Append the new chord to the chord_sequence stream.Part() object
    print(new_chord)
    chord_sequence.append(new_chord)


  chord_sequence.show()
  chord_sequence.show('midi')

  '''NUMEROUS POSSIBILITIES REMAIN OPEN FOR DEVELOPING HARMONIC MATERIAL BASED ON THIS ALGORYTHM'''
  '''AN EXPERIMENT OF ALTERATION OF THE NUMBER OF HARMONICS WITHIN EACH CHORD, PERHAPS GRADUALLY INCREASING OR DECREASING THE HARMONIC DENSITY[RN IT IS RANDOM, REF. random.Sample() args[1]]'''
  '''WE COULD LIMIT THE CHOICE OF HARMONICS MORE PRECISELY TO CONTROL THE FLOW OF CONSONANCE OR DISSONANCE'''
  '''WE COULD ALSO CRAFT MORE COMPLEX HARMONY BY MERGING CHORDS GENERATED FROM TWO OR MORE DISTINCT HARMONIC SERIES TO REPRESENT THE VERY MECHANISM OF HARMONY|ORCHESTRATION ITSELF[HERE WE HAVE DONE IT ON EACH BASSNOTE, SO SAME HARMONIC SERIES THROUGHOUT EACH CHORD PITCHCLASS CONTINUUM]'''
def chord_from_fundamental2(fundamental_pitch:pitch.Pitch,harmonic_numbers:list,nearest_semitone:bool=False)->chord.Chord:
  '''
  Creates a chord from a fundamental pitch and a list of harmonic numbers.
  '''
  # Initialize an empty chord object
  harmonic_chord=chord.Chord()
  # Iterate through the specified harmonic numbers
  for harmonic in harmonic_numbers:

    # Get the pitch of the current harmonic from the fundamental picth
    current_pitch=fundamental_pitch.getHarmonic(harmonic)

    # If the nearest_semitone:bool=True we can lever the midi property of the current pitch;
    if nearest_semitone:

      # Round the pitch to the nearest semitone.

      # Standard midi numbers are integers that corresponds to equally tempered pitches. current_pitch.midi will create a new pitch object based on the nearest midi note to the current pitch effecvtively rounding it to the closest semitone.
      current_pitch=current_pitch.midi
      # When we call the .midi atrribute of a pitch object it provides us rounded of midi number as midi because that id how they store number as rounded version of pitchClass number with octave==12 added.
      '''If we want to feed microtones to the f input of plugdata phasor we muct use pitch.Pitch() object's .getHarmonic() method.'''
      # Let's go back to the main function.

    # Add the pitch to the chord
    harmonic_chord.add(current_pitch)

  return harmonic_chord
def chord_from_fundamental(fundamental_pitch:pitch.Pitch,harmonic_numbers:list)->chord.Chord:
  '''
  Creates a chord from a fundamental pitch and a list of harmonic numbers.
  '''
  # Initialize an empty chord object
  #harmonic_chord=chord.Chord()
  # Iterate through the specified harmonic numbers
  # Get the pitch of the current harmonic from the fundamental pithc
  return chord.Chord([fundamental_pitch.getHarmonic(harmonic) for harmonic in harmonic_numbers])


if __name__=='__main__':
  main()