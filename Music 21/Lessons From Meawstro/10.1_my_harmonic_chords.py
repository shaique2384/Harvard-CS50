# @title 10.1_my_harmonic_chords.py

# 2. Configure music21 environment settings to locate MuseScore
from music21 import*
from music21 import environment,converter
us = environment.UserSettings()
us["musescoreDirectPNGPath"] = "/usr/bin/mscore"

def main():
  '''Overtones'''


  if True:
    fundamental=pitch.Pitch('C2')
    color=int(input('Pick a color from [1,2,3,4]: '))
    cell=input('Pick a cell from 0 to 1 {close:0,open:1}')
    chord1=chordOfDifferentColors(fundamental,color,cell)
    print(chord1)
  if True:
    p1=stream.Part(chordOfDifferentColors(fundamental,color,cell),time=meter.TimeSignature('4/4'))
    s1=stream.Score([p1])
    s1.show()
    s1.show('midi')

  # One potential aproach to harness the harmonic series for composition is to derive chords and harmonic sequences is to derrive chords and harmonic sequences from it's pitch structure.
  # Let's define a new function called chord_from_fundamental;
def chordOfDifferentColors(fundamental:pitch.Pitch,color:int,cell:int)->chord.Chord:

  pitches1=[fundamental.getHarmonic(i) for i in range(1,5)]
  pitches2=[fundamental.getHarmonic(i) for i in range(5,9)]
  pitches3=[fundamental.getHarmonic(i) for i in range(9,13)]
  print(pitches3)
  pitches4=[fundamental.getHarmonic(i) for i in range(13,17)]
  # Fixed: removed redundant pitch.Pitch wrapper around already initialized Pitch objects.
  pitches=[fundamental.getHarmonic(i) for i in range(1,16)]
  chordPitches=[]
  if color==1:
    chordNotes=[note.Note('C3')]
    # Fixed: added enumerate to prevent NameError: name 'i' is not defined.
    for i, p in enumerate(pitches1[0:-1]):
      if p.pitchClass!=0:
        if 4<(pitches1[i+1].pitchClass%p.pitchClass)<8:
          if 2<p.octave<5 and (pitches2[i+1].pitchClass%p.pitchClass>=4):
            chordPitches.append(p)
        else:
          p.octave+=1
          chordPitches.append(p)
    if pitches1[-1].pitchClass!=0:
      if (pitches1[-1].pitchClass%chordPitches[-1].pitchClass)<4:
        pitches1[-1].octave+=1
      chordPitches.append(pitches1[-1])
    else:
      pass
  elif color==2:
    chordNotes=[note.Note('C2')]
    for i, p in enumerate(pitches2[0:-1]):
      if p.pitchClass!=0:
        if 3<(pitches2[i+1].pitchClass%p.pitchClass)<9:
          if 2<p.octave<5 and (pitches2[i+1].pitchClass%p.pitchClass>=4):
            chordPitches.append(p)
        else:
          p.octave+=1
          chordPitches.append(p)
    if pitches2[-1].pitchClass!=0:
      if (pitches2[-1].pitchClass%chordPitches[-1].pitchClass)<4:
        pitches2[-1].octave+=1
      chordPitches.append(pitches2[-1])
    else:
      pass
  elif color==3:
    chordNotes=[note.Note('C5')]
    for i, p in enumerate(pitches3[0:-1]):
      if p.pitchClass!=0:
        if 2<(pitches3[i+1].pitchClass%(p.pitchClass))<10:
          if ((pitches3[i+1].pitchClass)%(p.pitchClass))>=4:
            print(f'if{p}')
            chordPitches.append(p)
        elif ((pitches3[i+1].pitchClass)%(p.pitchClass))<=4:
          p.octave+=1
          print(f'else{p}')
          chordPitches.append(p)
        else:
          pass
    if pitches3[-1].pitchClass!=0:
      if (pitches3[-1].pitchClass%chordPitches[-1].pitchClass)<4:
        pitches3[-1].octave+=1
      print(f'last {pitches3[-1]}')
      chordPitches.append(pitches3[-1])
    else:
      pass
  elif color==4:
    chordNotes=[note.Note('C4')]
    for i, p in enumerate(pitches4):
      if p.pitchClass!=0:
        if 1<(pitches4[i+1].pitchClass%p.pitchClass)<11:
          if 2<p.octave<5 and (pitches4[i+1].pitchClass%p.pitchClass>=4):
            chordPitches.append(p)
        else:
          p.octave+=1
          chordPitches.append(p)
    if pitches4[-1].pitchClass!=0:
      if (pitches4[-1].pitchClass%chordPitches[-1].pitchClass)<4:
        pitches4[-1].octave+=1
      chordPitches.append(pitches4[-1])
    else:
      pass

  else:
    raise ValueError('Provide a number between 1 and 4')



  for i,cp in enumerate(chordPitches[0:-1]):
    if -4<=(chordPitches[i+1].pitchClass-chordNotes[i].pitch.pitchClass)<=4:
      if chordPitches[i+1].octave-chordNotes[i].octave==0:
        if cp.octave<8:
          cp.octave+=1
        else:
          cp.octave-=1
    chordNotes.append(note.Note(cp))
  if -4<=(chordPitches[-1].pitchClass-chordNotes[-1].pitch.pitchClass)<=4:
    if (chordPitches[-1].octave-chordNotes[-1].octave)==0:
      if chordPitches[-1].octave<8:
        chordPitches[-1].octave+=1
      else:
        chordPitches[-1].octave-=1
  chordNotes.append(note.Note(chordPitches[-1]))

  return chord.Chord(chordNotes)

def sort_pitches(pitches_str):
  for p in pitches_str:
    if '#' in p:
      if 2 in p:
        p.replace('2','')
      elif 3 in p:
        p.replace('3','')
      elif 4 in p:
        p.replace('4','')
      elif 5 in p:
        p.replace('5','')
      pitch=pitch.Pitch(p)
    elif '2' in p:
      p.replace('2','')
    elif '3' in p:
      p.replace('3','')
    elif '4' in p:
      p.replace('4','')
    elif '5' in p:
      p.replace('5','')
      pitch=pitch.Pitch(p)
    return pitch

if False:
  # @title 10.2_Gemini_demo
  from music21 import pitch, interval

  p_high = pitch.Pitch('G4')
  p_low = pitch.Pitch('C4')

  # Higher pitch first -> Descending (negative) interval
  descending_interval = interval.Interval(p_high, p_low)
  print(f"Interval from high to low: {descending_interval.name} (Directed semitones: {descending_interval.semitones})")

  # Lower pitch first -> Ascending (positive) interval
  ascending_interval = interval.Interval(p_low, p_high)
  print(f"Interval from low to high: {ascending_interval.name} (Directed semitones: {ascending_interval.semitones})")


if __name__=='__main__':
  main()
