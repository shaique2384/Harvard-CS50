if False:
    from music21 import*

    # Our current focust==rhythm. 
    # So Note Instance Assignment with .pitch='C4' and .duration=2[quarternotes]
    my_note=note.Note(duration=duration.Duration(2))
    my_note=note.Note()

    # Our current focust==rhythm. So .pitch='C4' and .duration=2[quarternotes]
    my_note.duration=duration.Duration(2)

    # Let's create a stream object and inside the stream object let's insert a meter.TimeSigna() which allows us inputing complex meters and music21 adds ties automatically
    my_stream=stream.Stream()
    my_stream.insert(meter.TimeSignature())
    # Insert Inserts an item(s) at the given offset(s). A review of the library happened;

#import os
#os.environ["DISPLAY"] = ":99"

#import music21 as m21
#m21.environment.set('musescoreDirectPNGPath', '/usr/bin/mscore3')
from music21 import*
'''
The TimeSignature object represents time signatures in musical scores (4/4, 3/8, 2/4+5/16, Cut, etc.).

TimeSignatures should be present in the first Measure of each Part that they apply to. Alternatively you can put the time signature at the front of a Part or at the beginning of a Score, and they will work within music21, but they won't necessarily display properly in MusicXML, Lilypond, etc. So best is to create structures where the TimeSignature goes in the first Measure of the score, as below:

>>> s = stream.Score()
>>> p = stream.Part()
>>> m1 = stream.Measure()
>>> ts = meter.TimeSignature('3/4')
>>> m1.insert(0, ts)
>>> m1.insert(0, note.Note('C#3', type='half'))
>>> n = note.Note('D3', type='quarter')
>>> m1.insert(1.0, n)
>>> m1.number = 1
>>> p.insert(0, m1)
>>> s.insert(0, p)
>>> s.show('t')
'''
# Let's Follow above regulations.

# Introfuction Block [HARD]
my_stream=stream.Stream()
my_part=stream.Part()





# Body Block [SOFT]
# Each body block should have mechanisms as sub blocks. For us we are creating different kinds of notes assigning functionalities to them and inserting into my_measure.
# Body Block will have, 
## measure creation, 
## everything in note class creation and manipulation, 
## measure append|insertion
## part append|insertion
if True:
    my_measure=stream.Measure()
    my_ts=meter.TimeSignature('3/4')
    my_measure.insert(0,my_ts)
    my_note=note.Note(duration=duration.Duration(3.25))
    # Our current focust==rhythm. So .pitch==default
    my_measure.append(my_note)
    #my_measure.number=16
    my_part.insert(0,my_measure)

# We have so far dealt with 1/2^n as note length.
# But we havent yet worked with any duration that breaks away from this conventional molds.
# Let's create something using tuplets, 3 1/3 notes
if False:
    my_measure=stream.Measure()
    my_ts=meter.TimeSignature('3/4')
    my_measure.insert(0,my_ts)
    nBase3=note.Nore()
    nBase3.duration=duration.Duration(1/3)
    #my_measure.repeatAppend(mBase3, 3)
    my_measure.repeatInsert(nBase3, 3)
    my_part.inser(0,my_measure)

# We can easily extend this aproach to other tuplet durations, in this case quintuplets.
# Let's now create three quintuplet note objects and let's assign to their duration.Duration() using keyword duration.
if False:
    my_measure=stream.Measure()
    my_ts=meter.TimeSignature('3/4')
    my_measure.insert(0,my_ts)
    n1=note.Note(duration=duration.Duration(1/5))
    n234=note.Note(duration=duration.Duration(3/5))
    n5=note.Note(duration=duration.Duration(1/5))
    my_measure.insert(n1,n234,n5)
    my_part.inser(0,my_measure)

# We discover in music21 the remarkable ability to wield rhythm with great flexibilty through tuplets such as 5 subdivisions within the customary span of 4.
# We might however wish to push the bounderies further still with the subdivision of five within the space of three or seven within the space of five leading us into the territory of what some call irrational rhythms a terrain often traversed by   those Avant Guard composers like Brian Ferow, James Dylan and Michael Finnessy who are associated with the so called new complexity movement. 
#In music21 tuplets are defined by their own dedicated class and we can utilize it to create tuplets with even more control and flexibility.
# Let's translate a traditional composer's 'workflow into the realms of python and music21 and show strength as well as limitations.
if False:
    my_measure=stream.Measure()
    my_ts=meter.TimeSignature('3/4')
    my_measure.insert(0,my_ts)
    # Let's first create a tuplet object called my tuplet and as arguments let's provide integer values of five and three; representing the number of subdivisions we desire and the number of usual subdivisions.
    my_tuplet=duration.Tuplet(5,3) 
    # It's an object inheriting from the duration class and objects.
    # Whenever we introduce an irrational rhythm it is customary to display their ratio in notation within brackets above so.
    # We can do this by introducing the tupletNormalShow attriput of the tuplet object and assign 'number', this will be an inherent quality(probably init) assigned to our tuplet class object.
    my_tuplet.tupletNormalShow='number'
    # We have a tuplet object but we don't have a note yet so let's create one into niTuplet short for noteIrrationalTuplet. It's duration would be the duration of the entirity of the tuplet.
    niTuplet=note.Note(duration=duration.Duration(3))
    # The note automatically has a default duration object nested and we can easily append our tuplet object into the notes duration attribute[somehow the duration object and variables are nested in the class bock, I don't knopw yet] using appendTuplet().
    niTuplet.duration.appendTuplet(my_tuplet)
    # Let's now repeatAppend and repeatInsert niTuplet into my_measure and check while running in codespace which one works and to what extent.
    my_measure.repeatAppend(niTuplet, 5)
    # repeatAppend() has (items, numberOfTimes) as args
    my_measure.repeatInsert(niTuplet, 5)
    # repeatInsert() has (items, offsets) as args so it should mess up.
    # Let's find out which stream objects allow append and which allow only inserts.
    # With this knowledge creating rhythms inside of our tuplet is also straightforward.
    my_part.inser(0,my_measure) 
    
# Suppose this time we want to create a rhythm comprising of an 8th note followed by a dotted quarter note and another 8th note in total 5 8th notes(1/8+1.5/4+1/8=5/8) within the customary span of 3. 
if False:
    my_measure=stream.Measure()
    my_ts=meter.TimeSignature('3/4')
    my_measure.insert(0,my_ts)
    # So let's summon the tuplet object inside our note creation block.
    nit1=note.Note(duration=duration.Duration(0.5))
    nit234=note.Note(duration=duration.Duration(1.5))
    nit5=note.Note(duration=duration.Duration(0.5))
    t2=duration.Tuplet(5,3,tupletNormalShow='number')
    # The tuplet units<1/3 [3/5=0.6 outside base 2^Z] will be multiplied by each to give total 0.6*(0.5+2.5+0.5)=1.5 quarterLengths. Therefore the tuplet comprises of half the.entire measure of 3/4 meter[total 3 quarterLength]. So what means by that is this tuplet system, squeashes 5 8th notes[hint:total quarterLenth of note.Duration carried out by .appendRuplet() method and the intefers passed in into the duration.Tuplet() object creation]. 
    # So if integer inputs are as duration.Tuplet(m,n) this m:n is a blueprint like ratio operating on the total querterLength of the tuplet[tupletSystemDuration= sum(quarterLength of notes '.'appendeTuplet'ed')*(n/m)]. This Total is the duration of my_tuplet tuplet system's duration in the entirity of the measure. For this case it is one dotter quarter note and the remaining quarternote is empty in the m1.
    #'Dividing this tuplet duration by n gives us the interlocking real part of the poly rhythm while m gives us the syncopated complex part of the polyrhythm. 
    # appendTuplet() section;
    nit1.duration.appendTuplet(my_tuplet)
    nit234.duration.appendTuplet(my_tuplet)
    nit5.duration.appendTuplet(my_tuplet)
    # On the contrary, insert is when we wan't to feed numeric input as offsets, problematic as they are deppendent on the previous note objects so that nesting regulations don't break.
    my_measure.append(nit1,nit234,nit5)
    my_part.inser(0,my_measure)
    

# [custom function territory]
# Now let's pivot towards the practical applications of these ideas with the goal of crafting material to integrate into our composition.
# In his article duration and rhythms as compositional resources(1989) Brian offers valuable insights into his rhythmic thought processes
# One interesting and straight forward example involves the dynamic interplay of two cycles; the first cycle comprisinf the numbers 3,4 and 5 governs the meter within each bar and the second cycle encompassing 4,5,6 and 7 determines the count of evenly spaces notes per bar referred to by Fernow as impulses. So the cycles themselves are interlocking as the first cycle called the meter cycle repeating after 3 measures while the impulse carriying ones called the density cycle repeating after evety 4 measures comprising layers of accents and resultant syncopation. Cycles or a circles are best to describe such rhythms containing micro to macro phases.
# To encode these interlocking cycles within our program let's define a function called impulses_in_meter()
def meter_impulse_m(m:int,n:int)->stream.Measure:
    '''
    Creates a new measure containing m impulses within the n note meter
    '''
    '''
    custom_m=stream.Measure()
    custom_m.remove(clef.TrebleClef())
    # We need to hard code the meter denominator as it can not be other than 2^Z, let's pick Z=-3
    custom_ts=meter.TimeSignature(f'{n}/8')
    custom_m.insert(0,custom_ts)
    # Let's summon our note creation block with the special conditional.
    if m<n*2:
        custom_nit=note.Note(duration=duration.Duration(.5))
        # We input 0.25 as we want our tuple span unites to be 8th note i.e, half quarterLenths sqweashing each to be (n/m)th of the 8th notes.
        custom_t=duration.Tuplet(m,n,tupletNormalShow='number')
    else:  
        custom_nit=note.Note(duration=duration.Duration(.25))
        custom_t=duration.Tuplet(m,(n*2),tupletNormalShow='number')
    custom_nit.duration.appendTuplet(custom_t)
    custom_m.repeatAppend(custom_nit,m)
    return custom_m
    '''
    ...
    
# Let's create a meter_impulse_m() taking in different values of tuplets as p,q and create complexity in the step by step manner.
    
def meter_impulse_p(m:int,n:int,part:stream.Part())->stream.Part:
    '''
    Creates a new measure containing m impulses within the n note meter and isert into a given stream.part() object.
    '''
    '''
    custom_m=stream.Measure()
    custom_m.remove(clef.TrebleClef())
    custom_ts=meter.TimeSignature(f'{m}/8')
    microPhase.insert(0,custom_ts)
    # Let's summon our note creation block.
    if m<n*2:
        custom_nit=note.Note(duration=duration.Duration(.5))
        custom_t=duration.Tuplet(m,n,tupletNormalShow='number')
    else:  
        custom_nit=note.Note(duration=duration.Duration(.25))
        custom_t=duration.Tuplet(m,(n*2),tupletNormalShow='number')
    custom_nit.duration.appendTuplet(custom_t)
    custom_m.repeatAppend(custom_nit,m)
    part.insert(custom_m)
    return part
    '''
    ...

## *This is a projects*
# Goal would be to create a loop with yield instead of a return and also creating more complexity by adding args and kwargs in the fumctions geowing microphases inside each unitMacroPhases.  

def selfSimilarTupletSystem(density_range:list,meter_range:list,part_input:stream.Part())->stream.Part:
    '''
    Takes in lists comprising of brians density and meter cycle's minimum, maximum and step as first and second arguments. Thirs argument is the stream.part() provided by the user
    :density_range: A list of three int type elements as min, max and step of the density cycle.
    :meter_range: A list of three int type elements as min, max and step of the meter cycle.
    :part_input: stream.Part() provided. The system comprising measures will be inserted into the part and returned.
    :rtype: stream.Part()
    '''
    '''
    #densityMeasuresNumber=x
    #x=int(input('Number of Measures in Density Cycles: '))
    #meterMeasuresNumber=y
    #y=int(input('Number of Measures in Meter Cycles: '))
    dMin=density_range[0]
    x=dMin
    dMax,dStep=density_range[1],density_range[2]
    mMin=meter_range[0]
    y=mMin
    mMax,mStep=meter_range[1],meter_range[2]
    for _ in range((densityMax-densityMin)*(meterMax-meterMin)):
        if 4<=x<=7 and 3<=y<=5:
            uMp=meter_impulse_m(x,y)
            part_input.insert(uMp)
            if x==densityMax:
                x-=(dMax-dMin-dStep
            if y==mMax:
                y-=(mMax-mMin-mStep)
        x+=dStep
        y+=mStep
    return part_input
    '''
    ...
    
def impulses_in_meter_p():
    ...
    
# Now let's carbon copy our mewstro's custom func.
def impulses_in_meter(meter_numerator:int,n_impulses:int)->stream.Measure:
    '''
    Creates a new measure containing n impulses within the specified eighth note meter.
    '''
    '''
    # Create a measure object to contain the impulses
    combined_measure=stream.Measure()
    # Within music21 each new measure object is assigned as appropriate clef when created. But in this program we will ultimately combine multiple measures within a single stream.
    # To avoid the redundancy and clutter that would reult from encountering a new clef every measure we will employ the remove method to delete this.
    # Remove Clef
    combined_measure.remove(clef.TrebleClef())
    # Append the Time Signature.
    # We need to append a time signature object which requires a string as input, we'll employ an f'str' to dynamically set the numerator according to the meter_numerator args provided by our function.
    # Since our meter cycle consistently operates on 8th notes, the denominator will be hardcoded as 8.
    combined_measure.insert(meter.TimeSignature(f'{meter_numerator}/8'))
    # Let's proceed to construct a note object along with it's corresponding tuplet to convey our impulses. The critical aspect here is determining the duration of our note which is contingent upon the relationship between the number of inpulses and the meter numerator.
    # To illustrate suppose our measure maintains the same 3/8 meter but forced with a 7:3 tuplet instead of 4:3 meters the convention depiction shifts to a tuplet of 7 16th notes within the span of 6 16th note denoted by the ratio 7:6. This happens when the n_impulses is >= twice the meter_numerator.

    # Determine wheather n impulses should be eighth or 16th notes.
    if n_impulses>=meter_numerator*2:
        current_note=note.Note(duration=duration.Duration(0.25))
        current_tuplet=duration.Tuplet(n_impulses,meter_numerator*2)
    # Let's create else path;
    else:
        current_note=note.Note(duration=duration.Duration(0.5))
        current_tuplet=duration.Tuplet(n_impulses,meter_numerator)   
    # Display the tuplet ratio within brackets
    current_tuplet.tupletNormalShow='number'
    # Append the tuplet to notes duration meaning multiplying the meter unit by n/m.
    current_note.duration.appendTuplet(current_tuplet)
    # Append n impulses using stream.Measure() object's repeatAppend method to our combined_measure and return it.
    combined_measure.repeatAppend(current_note,n_impulses)
    return combined_measure
    '''
    ...

# Let's now collect 4 measures conttaining the tuplets as unit macroPhases themselves. We will call them uMp.
if False:
    # The measure time signature creation is done in our custom function.
    uMp1=meter_impulse_m(4,3)
    uMp2=meter_impulse_m(5,4)
    uMp3=meter_impulse_m(6,5)
    uMp4=meter_impulse_m(7,3)
    my_part.insert(uMp1,uMp2,uMp3,uMp4)

# Let's summon brian's part into our system;
if False:
    my_part=selfSimilarTupletSystem([4,7,1],[3,5,1],my_part)

# Let's summon mewstro's main
if False:
    # Cycles as lists governing the meter and number of impulses per meter.
    meter_cycle=[3,4,5]
    impulse_cycle=[4,5,6,7]
    # The distinct length of these cycles will allow them to be repeated and recombined to yield fresh rhythmic material. 
    # Each can undergo a number of repeation as the len() of the other before reaching a point of convergence where the rhythmic potentials have been fully explored.
    # Consequently we will create two new lists which will contain the complete repetitions of each cycles to do this in each cycle.
    # Meawstro's version;

    # Multiply the cycles by each other's lengths will extend our list. Multiplication is similar to concatenating with the same list that many times and concatenating simple lists gives us the list elements collowing the sequence the lists themselves into a bigger extended list as oposed to nested lists[lists or dictionaries inside of each others as elements, concatenation does not put one list into another, we can only do that by assignments] 
    meter_cycles=meter_cycle*len(impulse_cycle)
    # for this case; meter_cycles=[3,4,5]*4=[3,4,5]+[3,4,5]+[3,4,5]+[3,4,5]=[3,4,5,3,4,5,3,4,5,3,4,5]
    impulse_cycles=impulse_cycle*len(meter_cycle)

    # Let's apply impulses_in_meter() to each cycles.
    combined_cycles_measures=list(map(impulses_in_meter,meter_cycles,impulse_cycles))
    # Both has equal number of elements == len(meter_cycle)*len(impulse_cycle)

    # Part takes both items and lists as input for our case it is a list of measures returned by mapping impulses_in_meter() function.
    my_part.insert(combined_cycles_measures)


# Shaique's Magic Loop from impulses_in_meter()
if False:
    # Cycles as lists governing the meter and number of impulses per meter.
    meter_cycle=[3,4,5]
    impulse_cycle=[4,5,6,7]
    n=0
    for _ in len(impulse_cycle):
        for i in meter_cycle:
            if n>=3:
                n-=3
            impulses_in_meter(impulse_cycle[n],meter_cycle[i])
            n+=1
             
# Conclusion Block [HARD]
my_stream.insert(my_part)
#my_stream.write('musicxml.png', fp='7_tuplet_rhythms2.png')
#my_stream.write('musicxml.png', fp='7_tuplet_rhythms2.musicxml')

# Test juno inline render
#import music21
from music21 import converter,ipython21

# Create stream
#s=music21.converter.parse('tiniNotation: 3/4 c4 d e f2.')

# Write to SVG image file locally
#fp=my_stream.write('musicxml.png') only works in codespace

# Render using music21's internal ipython converter

# Create your stream
#my_stream = music21.converter.parse('tinyNotation: 3/4 c4 d e f2.')

# Export as MusicXML (creates output.xml in your working directory)
my_stream.write('musicxml', fp='output.xml')

# Export as MIDI
my_stream.write('midi', fp='output.mid')

print("Export complete!")
