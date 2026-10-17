# @title 9_scales
# 2. Configure music21 environment settings to locate MuseScore
from music21 import*
from music21 import environment,converter
us = environment.UserSettings()
us["musescoreDirectPNGPath"] = "/usr/bin/mscore"

def main():

  # The scale module in music21 provides a powerful set of tools to represent and modify a set of predefined or customized scales.
  if False:
    scale_=scale.Scale('c4')
    ionian=scale.MajorScale('c4')
    # Takes input as pitch.Pitch() argument of the tonic. We can also envoke a minor scale.
    aeolian=scale.MinorScale('a4')
    # Let's have all other scales.
    dorian=scale.DorianScale('d4')
    phrygian=scale.PhrygianScale('a4')
    lydian=scale.LydianScale('g4')
    mixolydian=scale.MixolydianScale('e4')
    locrian=scale.LocrianScale('f4')
    # Let's envoke other exotic scales.
    melodicminor=scale.MelodicMinorScale('c4')
    harmonicminor=scale.HarmonicMinorScale('c4')
    #byzantine=scale.ByzantineScale('c4')
    #pentatonic=scale.PentatonicScale('c4')
    #pentatonicmajor=scale.PentatonicMajorScale('c4')
    #pentatonicminor=scale.PentatonicMinorScale('c4')
    chromatic=scale.ChromaticScale('c4')
    wholetones=scale.WholeToneScale('c4')
    octatonic=scale.OctatonicScale('c4')
    #halfdiminished=scale.HalfDiminishedScale('c4')
    #diminished=scale.DiminishedScale('c4')
    #halfdiminished=scale.HalfDiminishedScale('c4')
    # We can explore the makeup of any scales that we have created through a range of in built methods.
  
  # We can use print() to view their return value, let's print couple of the attributes of the scale objects.
  if False:
    print(ionian.name)
    print(aeolian.getPitches)
    print(aeolian.getParallelMinor)
    print(dorian.getScalaData)
    print(locrian.getLeadingTone)
    print(lydian.getDegreeMaxUnique)
    print(mixolydian.getDominant)
    #print(phrygian.getScaleDegreeAndAccidentalFromPitch(5))
    print(ionian.getScaleDegreeFromPitch('c4'))
    #
    print(ionian.pitchFromDegree(2))
    # We can specify the interval the argument of .transpose() attribute using an interval.Interval(i) object or string literal 'Mi' as major iths and 'mi' as minor iths wgile perfect being 'pi's[These are music21 conventions for interval objec arguments].
    print(ionian.transpose(interval.Interval(2)))
    print(ionian.transpose(interval.Interval('P4')))
    print(ionian.transpose(interval.Interval('half')))
    print(ionian.transpose(interval.Interval('M7')))
    print(aeolian.transpose('P4'))
    print(dorian.transpose('half'))
    print(phrygian.transpose('M6'))
    print(lydian.transpose('m3'))
    # THESE TRANSPOSES CAN BE UTILIZED IN THE SCHENKERIAN ENGINES AND LAYERED APPROACH ENGINES FRO ALLAN HOLDSWORTH PEOTO COSMOS SOLO.
    # Allan's progressions are based on crazy parallel modes and my cmyk stories also based on that.

    # The nextPitch() method will return the next higher pitch of our scale.
    print(lydian.nextPitch('E4'))
    # The argument of this attribute can be a pitch.Pitch('str') object or the 'str'
    print(mixolydian.nextPitch(pitch.Pitch('E4')))
    # It has a second int argument space for steps which will give us that many steps from our given pitch. The +i will give us that many pitches higher and -i will give us that many pitches lower.
    print(lydian.nextPitch('E4', -2))
    print(phrygian.nextPitch('E4', 2))
    # We can also get a list of pitches using the getPtches(i0,if) specifying the lowest and highest pitches to be included in the list.
    print(melodicminor.getPitches('D5', 'A6'))
    # By default the return list is based on an ascending list. But we can alter this with direction kwargs assigned to by scale's direction object's attribute DESCENDING.
    print(melodicminor.getPitches('D5', 'A6', direction=scale.Direction.DESCENDING))
    # DIrection has type enumerate and has instances called ASCENDING, DESCENDING and BI.
    print(melodicminor.getPitches('D5', 'A6', direction=scale.Direction.BI))

  # We can iterate over this scale pitch list to append into a stream.
  if False:
    mm_pitches=melodicminor.getPitches('B4', 'B5', direction=scale.Direction.DESCENDING)
    # I know why but BI is creating some enclosure effect, DESCENDING works just fine.
    mm_score=stream.Score()
    mm_part=stream.Part()
    # Iterate over the pitch.Pitch() objects in the list.
    for mm_pitch in mm_pitchesBI:
      # Let's pass in our iterator into the constructor block of new note object;
      mm_note=note.Note(mm_pitch)
      mm_part.append(mm_note)
    mm_score.show()

  # List comprehension;
  if False:
    notated_line=stream.Part([note.Note(mm_pitch)for mm_pitch in mm_pitches])
    notated_line.show()

  # music21 also empowers us to create even more scales beyond those which have created in already predefined classes. Scales are constructed via cycles of intervals. A  wholetone scale may be the simplest example of that.
  # A three note cell concisting of a minor second followed by a major second is the building block of an octatonic scale.
  '''WHOLETONE AND OCTATONIC ARE THE FIRST TWO CYCLIC AND SYMMETIC SCALES OF COMPOSER OLIVIER MESSIAN'S SO CALLED MODES OF LIMITED TRANSPOSITIONS.

  "BASED ON OUR PRESENT CHROMATIC SYSTEM, A TEMPERED SYSTEM OF TWELVE SOUNDS, THESE MODES ARE FORMED OF SEVERAL SYMMETRIC GROUPS, THE LAST NOTE OF EACH GROUP ALWAYS BEING COMMON WITH THE FIRST OF THE FOLLOWING GROUP" '''
  # Scale which produces the same pitch class content when transposed onto at least one other degree of the chromatic scale. Another such scale is the messian's 3rd is based on a 4 note cell consisting of one M2 and two m2 s. The dedicated class to represent this example has not been provided yet.  # In music21 we can create a CyclicalScale object with it's first argument as tonic to to encode it [for scale like such functional arguments like tonic is redundency but it needs some degree1 to build the scale.
  if False:
    # The second argumend can take in a list containing interval objects or the str repesentations of the intervals that make up the cycle used to build our scale [same as .transpose() arguments]
    my_scale=scale.CyclicalScale('C', ['M2','m2','m2'])
    scale_pitches=my_scale.getPitches('c4','c5', direction=scale.Direction.DESCENDING)
    notated_scale=stream.Part([note.Note(sp) for sp in scale_pitches])
    notated_scale.show()
    notated_scale.show('midi')

  # Original scales created with cyclical scale need not necessarily repeat at the first octave.
  if False:
    # For example an interval cycle based on three major seconds followed by two minor seconds will create a two octave scale.
    my_scale=scale.CyclicalScale('C', ['M2','M2','M2','m2','m2'])
    scale_pitches=my_scale.getPitches('c4','c6', direction=scale.Direction.ASCENDING)
    notated_scale=stream.Part([note.Note(sp) for sp in scale_pitches])
    notated_scale.show()
    notated_scale.show('midi')

  '''THESE CYCLIC SCALES SOUND LIKE MODULATIONS HAPPENING AFTER EACH CELLS, INTERESTING COMPOSITIONAL OR IMPROVISATION TOOL'''

  # Having explored the functionality of music21 scale module let's consider how we might leverage its power compositionally within our python
  '''Composition using Scales'''
  if False:
    # To start we will consider a list of pitches perhaps containing the contents of a chord ot Melody and use the music21 to dynamically map it from one type of scale to another thereby generating new potential melodic patterns or harmonies.
    # To do this let's take the distance in scale steps between each pair of pitches in the list and populate a new list by applying these values to traverse a second scale type.
    # To determine the number of scale steps between two pitches we'll define a new custom function called get steps.
    # Coming back for the def get_steps() function to create two CyclicalScale s;
    CclScale1=scale.CyclicalScale('C', ['M2','M2','m2','m2'])
    CclScale2=scale.CyclicalScale('C', ['m3','m2','m2','m2'])
    # Each will repeat at the octave and contain eight pitch classes. Let's create a lis to create a sequence called origin. Consisting of pitches native to our first scale.

    CclScale1_pitches=CclScale1.getPitches('c4','c5')
    CclScale2_pitches=CclScale2.getPitches('c4','c5')
    
    # Create a list of pitches based on CclScale1
    #origin_demo=[pitch.Pitch(p) for p in CclScale1.getPitches('c4','c5')]
    # Here we created a simple scale ascending, but for the purpose we need an arbitrary sequence of notes based on our scale. 
    #For starter let's see what Meowstro is doing.
    origin=[pitch.Pitch(p) for p in ['C4','E4','B3','A#4','G#4','E4','D5','F4']]
    # Now let's introduce random and randrange to generate origin consisting of 8 pitchers.

    # This pitch list will map or translate to a second list called translated.
    translated=[origin[0]]

    # Iterate over the remaining pitches in the list using range() from i=1 to i=len(origin) because we want to have origin[0] as args[0] of get_steps() function in the first iteration and origin[len(origin)] as as args[1] in the last iteration.
    for i in range(1,len(origin)):
      # We will store the steps using get_steps() function where from_pitch:to_pitch will be origin[1-1]:origin[1] to origin[len(origin)-1]:origin[len(origin)]
      n_scale_steps=get_steps(origin[i-1],origin[i],CclScale1)
      # In the first iteration we are getting the steps from origin[1-1]==origin[0] to origin[1], inserted as args[0] and args[1] according to the scale composition of our iserted scale.Scale() object CclScale1 as args[2].
      # The interesting thing about scale.Scale() objects are their modularity as a blueprint stripping upto to the threshold informations of the definition of a scale while housing the relevant attributes and methods.
      next_pitch=CclScale2.nextPitch(translated[i-1],n_scale_steps)
      # The real utility of using (1,len(origin)) as the *args of range(0) function in the for loop statement lies here. 
      #We are taking translated[i-1], starting from translated[0]=orgon[0] of the random list of pitches in origin, fetching next pitch from the random pool origin using origin[i], starting from origin[1] to calsulate random number distance or number of steps between origin[i-1] and origin[i] based on CclScale1 and passing in the translated[i-1], translated[0]==origin[0] as args[0] and number of CclScale1 scale steps between origin[i-1] and origin[i] or n_scale_steps as args[1] of the .nextPitch  method of CclScale2. 
      # We got n_scale_steps:int using the CclScale1 and plugged it in into the steps:int args of CclScale1's nextPitch calculating protocol.
      # We are taking a pitch from the random pitch pool origin and using bits of information of CclScale1, and origin sequence and plugging the remaining information to get next pitch from CclScale2 and appending this translated next pitch into the translated:list pool.
      # We could not do it using the built in default functions provided by the music21, and just witnessed an original algorythm unfold in real time.
      # To complete the mapping process in for loops let's append this new_pitch to the translated list.
      translated.append(next_pitch)

    # Let's create two part objects to show in a stream.Score()
    p1=stream.Part([note.Note(p) for p in origin])
    p2=stream.Part([note.Note(p) for p in translated])
    # We can also create a score object by inserting a list of parts.
    my_score=stream.Score([p1,p2],time=meter.TimeSignature('4/4'))
    my_score.show()
    my_score.show('midi')



def get_steps(from_pitch,to_pitch,origin_scale):
  '''
  Determine the number of scale steps between two pitches.
  :param: from_pitch and to_pitch denotes the range of pitches and origin_scale specifies the scale from which the pitches are drawn.

  '''
  # Sort the 'from' and 'to' pitches in ascending order.
  pitch_range=sorted([from_pitch,to_pitch])
  # It's just sorting two inputs, not index range like list_[i:j]
  # We need to sort as we want to use same .getPitches() method for both cases of desired ascending or descending order.

  # List of all scale pitches within pitch_rang e 
  scale_pitches=origin_scale.getPitches(pitch_range[0],pitch_range[1])
  # We can also unpack pitch_range list which is sorted and have two elements we will use as lower and upper limit of .getPitches() method.
  pitches_in_range=origin_scale.getPitches(*pitch_range)

  # Calculate the number of steps
  steps=len(pitches_in_range)-1
  # steps is like an [int] pd object stores the number of ascending steps between the pitches supplied to the function therefore it is necessary to account for cases where from_pitch descends to to_pitch.

  # If the pitches descend, reverse the polarity of steps
  if from_pitch>to_pitch:
    #steps=-steps
    steps*=-1
  # Now let's return steps
  return steps

    


if __name__=='__main__':
  main()

  '''MAKE SURE TO CREATE NEW SCALES FROM SCHILLINGERS INFINIT SCALES'''