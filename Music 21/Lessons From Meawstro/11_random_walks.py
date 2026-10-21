# @title 11_random_walking
import random
import copy
from music21 import *

# Configure music21 environment settings to locate MuseScore
us = environment.UserSettings()
us["musescoreDirectPNGPath"] = "/usr/bin/mscore"

def main():
  # We increase steps to 32 to give the walk more room to explore negative values
  if True:
    my_random_walk = random_walk(128,0,8,[1,4,1,4,6,6,10,1])
    print("Random Walk Path:", my_random_walk)
    constrainedRandomWalk=generateConstrainedSteps(128,12)
    print("Constrained Random Walk Path:", my_random_walk)

    p = stream.Part(clef=clef.TrebleClef)
    P = pitch.Pitch(midi=72)

    if False:
      n_negative_steps = sum(1 for step in constrainedRandomWalk if step < 0)
      if 0 <= n_negative_steps <= 24:
        P.midi = 72
    p.midi=72
    p.append(note.Note(P, duration=duration.Duration(0.25)))

    # Final tweak and appending into stream
    for step in constrainedRandomWalk:
      P = copy.deepcopy(P)
      # Prevent the pitch from drifting out of readable octaves
      if P.octave < 4:
        P.midi += step  # Force it back up if it goes too low
      elif P.octave > 7:
        P.midi -= step  # Force it back down if it goes too high
      else:
        P.midi += step

      p.append(note.Note(P, duration=duration.Duration(0.25)))

    p.show()
    p.show('midi')
    # Sounds like that guitar shred speed guines book record challenge
    '''NEURAL NETWORKS AND XGBOOSTS WILL BE THE VEHICLE FOR CONTROLED CHAOS AND BIASES, OPEN WEIGHT TRAINING MODEL<FREE TO USE; IMPOSSIBLE TO PLAGIARIZE>'''

  '''THEY SOUND FANTASTIC! NOW NEED TO DEPLOY CLUSTERS OF REPEATITIONS IN STRATGEIC PULSE OR QUANTAS'''
  '''LET'S USE SCALE NEXT THEN WE CAN USE THE MATH OF OUR PLUGDATA PATCH TO CREATE SCALE ENCLOSURES USING CYCLYCAL SCALE AND DEPLOY THIS STEP GENERATOT IN NON CHROMATIC FASHION'''
  '''THEN LET'S CREATE SCOPE AND PARAMETERS FOR STEPS AND LEAPS AS NN CLASSIFICATION. ON TOP OF BINARY CLASSIFICATIONS WE CAN ALSO ADD CLASSIFICATIONS WITH ARPEGGIATION, ENCLOSURE, CHROMATIC NEIGHBORING NOTES ENCLOSURES, ALSO MOTIFIC PATTERN FINDING OF DEMUCS>FFT>FTOM OF IMPROVISED PIECES ON YOUTUBE.'''
  '''MORE INTELLIGENT[MORE OUTPUT WITH LESS DATA] ONES CAN BE USED TO PLAY ALONG RESPOINSIVELY WITH 1 MEASURE OR 4 MEASURES BUFFER SIZE, OR UPDATE BUFFER SIZES BASED ON THE CONTENTS OF PLAYED SOLO[SEQUENCE NEEDS LESS COMPUTE, ALLAN'S MASSIVE LINES NEED MORE COMPUTE POWER]'''
  '''START THINGS ON YOUR LESSON TEMPLATES AND START USING BASIC THINKING, MIMIC HOW YOU AND I IMPROVISE OR RESPOND IN THE MOMENT AND QUANTIFY THOSE. START EASY; EVERY PIECES MATTER'''
  if False:
    my_random_walk=random_walk(16,0)
    print("Random Walk Path:", my_random_walk)
    my_stream=stream.Stream()
    starting_pitch=pitch.Pitch('A4')

    # Iterate over my_random_walk
    for step_value in my_random_walk:

      # Check wheather step_value reptresents the starting value
      if step_value==my_random_walk[0]:
        next_pitch=starting_pitch
      else:
        # Transpose the pitch according to step_value
        next_pitch=starting_pitch.transpose(step_value)
      my_stream.append(note.Note(next_pitch))

    my_stream.show()
    my_stream.show('midi')
  # Horrible repeats nots, we can use tie notes if repeatation happens, but for composition quarterLength works better.
  # Let's introduce variation in step sizes to bring forth greater levels of randomness. Foe that we need to modify our custom function random_walk() by adding a third argument called possible_steps.

  # We came back; let's now rewrite the same meowstro function; well a little of shaique's touch by adding hardcoding, unpack and range to create a set int numberline limit in both directions.
  if False:
    usr_n_steps:int=int(input('n_steps: '))
    usr_start:int=int(input('start: '))
    usr_step_max:int=int(input('step_max[upto 10]: '))
    weights=[]
    for i in range(usr_step_max):
      usr_weight=int(input(f'for {i+1}th step pick a weight from 0 to 10: '))
      weights.append(usr_weight)

    my_random_walk=random_walk(usr_n_steps,usr_start,usr_step_max,weights)
    #print("Random Walk Path:", my_random_walk)
    my_stream=stream.Stream()
    starting_pitch=pitch.Pitch('A4')

    # Iterate over my_random_walk
    for step_value in my_random_walk:

      # Check wheather step_value reptresents the starting value
      if step_value==my_random_walk[0]:
        next_pitch=starting_pitch
      else:
        # Transpose the pitch according to step_value
        next_pitch=starting_pitch.transpose(step_value)
      my_stream.append(note.Note(next_pitch, duration=duration.Duration(random.choice([1,0.5,0.25]))))
      # Let's create a separate custom func for duration objects and deploy on this part of the code.

    my_stream.show()
    my_stream.show('midi')

  # To refine this further we could encode the ability to adjust the probability of choosing one interval or another.
  # This will result in greater control over the resulting pitch structure allowing us to create a biased random walk that favors certain intervals over others.
  # We'll add a 4th optional argument to random walk called wrights and set it by default to None.

  '''WORKS PERFECTLY! NEXT LET'S TRANSLATE SAME PARAMETERS i.e, BIASES AND OPTIONS INTO OUR NOTE'S DURATION ATTRIBUTE'''

def generateConstrainedSteps(nOfSteps:int=32,maxRepeat:int=6):
  '''
  Returns a more dynamic random walk using normal distribution and a parameter for maximum directional repeat.
  '''
  steps=[]
  currentRunStep=None
  # None so that we can deploy it when there was no value assigned
  repeat=0

  for i in range(nOfSteps-1):
    stepFloat=random.gauss(0,1.0)
    step = -1 if stepFloat<0 else 1
    # We are at the mercy of function itself; this is where the quality of function, or gBoosts or NNs come into play
    # Let's distribute things into repeat preveious or not
    if step==currentRunStep:
      # Always start with the ptoblematic ones then we can just use else; easy;
      if repeat>=maxRepeat:
        step=-(step)
        # We need to deploy here the things in the outer else block as it is an exclisive condiotional flow
        currentRunStep=step
        repeat=1
        # this updates the repeat after each repeat==(maxRepeat|6)
        # Now everything else under this flow; when we don't want to change the step sign, we just want to append as it is.
      else:
        # Basically when repeat==([1:7])[i]
        currentRunStep=step
        repeat+=1
        # We gotta keep updating for non repeat values or else we can not include upto 6 repeats. There will be only one repeat per iteration.

    else:
      currentRunStep=step
      repeat=1
            # This is our first iteration as step!=()currentRunStep|None)
            # Repeat gets first update of first iteration

    steps.append(step)
        # This is already giving us step=(-1|1)
        # Let's go back under conditional <if step==currentRunStep>
  return steps

def random_walk(n_steps:int, start:int, step_max:int=6,weights=None):
  '''
  Returns a more dynamic random walk using a rounded normal distribution
  '''
  walk = [start]
  #step_max=6
  step_value=[-(step_max-i) for i in range(step_max)]+[(i) for i in range(1,(step_max+1))]
  #print(step_value)
  step_total=step_max*2
  weights_demo=[1 for i in range(step_max)]

  weights_of_choices=[weights[i]/step_total for i in range(step_max)]+[weights[step_max-i]/step_total for i in range(1,(step_max+1))]

  for i in range(n_steps - 1):
    # Using a normal distribution centered at 0 with standard deviation of 1.8
    # This allows steps of 0, -1, 1, -2, 2, -3, 3, etc.
    # This one is better for more nuanced randomness.
    #step_change = int(round(random.gauss(0, 1.4)))
    #next_step = walk[i] + step_change
    # Here goes Meowstro's method;
    #step=walk[i]+random.choice([(i+1) for i in range(step_max-1)]+[(i+1)*(-1) for i in range(step_max-1)])
    step=walk[i]+random.choices(step_value,weights=weights_of_choices)[0]
    #print(step)
    walk.append(step)
  return walk

# @title 11.1_rough
if False:
  #print([*[(i+1) for i in range(5)]+[(i-1) for i in range(-5)]])

  step_max=6
  step_value=[-(step_max-i) for i in range(step_max)]+[(i) for i in range(1,(step_max+1))]
  print(step_value)
  step_total=step_max*2
  weights_demo=[1 for i in range(step_max)]
  weights=[4,6,1,1,1,1]

  print([weights[i]/step_total for i in range(step_max)]+[weights[step_max-i]/step_total for i in range(1,(step_max+1))])

if __name__ == '__main__':
  main()