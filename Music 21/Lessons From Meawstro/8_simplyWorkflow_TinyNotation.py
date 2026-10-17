# 2. Configure music21 environment settings to locate MuseScore
from music21 import*
from music21 import environment,converter
us = environment.UserSettings()
us["musescoreDirectPNGPath"] = "/usr/bin/mscore"

def main():
  #pass
  # Previously we have worked on weaving together music21 objects within streams. This whilst flexible and comprehensive can sometimes become needlessly cumbersome.

  # To solve this music21 offers a streamlined way of writing music using a string of characters called tiny notation. To use tiny notation we will first initialize a variable called tiny_stream and assign it to converter.parse() function. This function will convert a string argument into a music21 stream.part() object that we can manipulate and display.
  #tiny_stream=converter.parse()
  # To use tiny stream it is important to create a string using double and not single quotes. Let'a type in this format "tinyNotation: 2/4 c d c# cn e- en"
  tiny_stream=converter.parse("tinyNotation: 2/4 c d c# cn e- en")
  # c denotes middle c or c4 where c', c'' and so on denotes higher numbers. Capiral letters like C denotes C3, and repeating them CC, CCC renders lower octaves. r means rest.
  tiny_stream1=converter.parse("tinyNotation: 2/4 c' A GG# Gn FFF FF#")
  # We can also specify a duration by 1, 2, 4... denoting the denominator of the duration. 1=whole, 2=half and so on. Once we specify a duration subsequent notes will all assume that duration until we specify the duration. BY default the duration is quarterLength. Also . means dotted the quarterLength and ~ means tie with the next one. 
  tiny_stream2=converter.parse("tinyNotation: 2/4 r8 c'8 A4 GG#. Gn8~ FFF8 FF#")
  # We can also create triplets typing notes inside trip{}.
  tiny_stream3=converter.parse("tinyNotation: 2/4 r trip{e-4 c'8} c-4 a g#8. gn8~ f8 f#")

  # Let's now envoke .show()
  tiny_stream.show()
  tiny_stream1.show()
  tiny_stream2.show()
  tiny_stream3.show ()

  # tinyNotation is deliberately concise and user friendly. A design choice that carries inherent limitations.
  # We've therefore covered the breadth of what tiny notation in its standalone form can achieve. But having crafted the basic musical streams we can now continue to add layers of complexity and combine them together by leveraging the broader capabilities of the music21 library. 
  # This should not be the norm to explore music using python as with oop we get more comprehensive utilization of the real world music entities when we are utilizing the computational tools to explore the manifestation of number of innovative mathematical patterns into musical forms and compare them to find common ground and rethinking traditional music pedagogy.


if __name__=='__main__':
  main()




if False:
    # Conclusion Block [HARD]
    my_score.insert(my_part)
    
    # Export as MusicXML (creates output.xml in your working directory)
    my_score.write('musicxml', fp='my_code_creation.xml')
    
    # Export as MIDI
    #my_score.write('midi', fp='output2.mid')
    
    #my_score.show('txt')
    print("Export complete!")
    
