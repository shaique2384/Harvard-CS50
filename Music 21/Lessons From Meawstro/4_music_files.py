# The ability to manipulate and analyze musical scores whether they are part of a bundled corpus or external files with supported format are primary features of music21
# In music, a corpus (plural: corpora) is a structured, systematic collection of musical data curated for analysis, computation, or sound design. 
# It is the musical equivalent of a text corpus in linguistics. 
# Instead of analyzing a single song, researchers use corpora to uncover statistical trends, evolutionary patterns, or stylistic fingerprints across thousands of pieces.
# Todays lesson is on how to access both internal and external works and numerous tools at our disposal for passing and analtizing them
# The music21 corpus is a large repository of freely distributable music containing works in various file formats such music xml and humdrum
# : MusicXML serves as a universal translation bridge between commercial score writers like MuseScore, Sibelius, and Dorico. 
# Humdrum is a research-oriented syntax built to manipulate, parse, and analyze music data using command-line tools.
# : MusicXML relies on a highly verbose, hierarchical tree format structured into nested XML tags (<score-partwise> or <score-timewise>). 
# Humdrum uses a compact, column-based ("spine") format that represents music as a lattice of parallel time and pitch trajectories [like csv files]
# we can simply just import corpus from music21

from music21 import corpus
# importing the entire music21 library works too
# Various methods can be accessed to search and explore what works are contained within the corpus
# For insrance, the get composer method can be used to retrieve all the works in the corpus by a specified composer

# Retrieve all works by Bach
bach_work = corpus.getComposer('bach')
# The function getComposer(str) returnw all filenames in the corpus that match a composer's or a collection's name. 
# An fileExtensions, if provided, defines which extensions are returned. 
# An fileExtensions of None (default) returns all extensions.
# we can easily print the list returned by the function as it is a list
if False:
    print(bach_work)
# it ususally prints a list of locations
'''
[WindowsPath('C:/Users/User/AppData/Local/Programs/Python/Python313/Lib/site-packages/music21/corpus/bach/bwv1.6.mxl'), 
WindowsPath('C:/Users/User/AppData/Local/Programs/Python/Python313/Lib/site-packages/music21/corpus/bach/bwv10.7.mxl'), 
WindowsPath('C:/Users/User/AppData/Local/Programs/Python/Python313/Lib/site-packages/music21/corpus/bach/bwv101.7.mxl'), 
WindowsPath('C:/Users/User/AppData/Local/Programs/Python/Python313/Lib/site-packages/music21/corpus/bach/bwv102.7.mxl'), 
WindowsPath('C:/Users/User/AppData/Local/Programs/Python/Python313/Lib/site-packages/music21/corpus/bach/bwv103.6.mxl'), 
...]
'''
# Should we wish to locate a more specific subset of works we can leverage the search method provided by the music21 corpus
# Search metod enables us to use multiple search fields as keyword arguments
works = corpus.search(composer='bach', timeSignature='3/4')
# The function searches all stored metadata bundles and return a list of file paths.
# This function uses stored metadata and thus, on first usage, will incur a performance penalty during metadata loading.
# We can access any of these works via indexing.
# If we intend to analyze or manipulate aspects of musical score we can then use the pass method to convert our chosen work into a music21 stream object.
# It can be treated like any other music21 stream

# let's convert work into a stream. Work is the iteratble list works with index integer inside square brackets
# then we will apply method parse() on that WindowsPath
bach_work0 = works[0].parse()
# bach-work0 has automatically become a stream object, which can be shown
if False:
    bach_work0.show()
# The WindowsPath acts as a precise pointer to the file on your hard drive. 
# The parser reads the file extension (e.g., .mxl, .xml, or .krn) to determine the file format automatically. 
# It then reads the raw text or decompresses the archive data.
# Instead of returning raw text, music21 builds an in-memory structural layout called a music21.stream.Score. 
# This object acts as the top-level container for the entire piece of music.
# Stream is a specialized container dataset, but it behaves more like a smart, music-aware Python list than a typical data table (like a spreadsheet or database).
# While a normal Python list only tracks the position index of its elements (0, 1, 2...), a music21 Stream tracks elements using two simultaneous dimensions:
# 1. The Object Dimension: It holds a collection of music objects (Note, Chord, Rest).
# 2. The Timeline Dimension: Every object inside a Stream is stamped with an offset, which is its exact starting position in musical beats (e.g., beat 0.0, beat 1.5, beat 4.0).
# Key Features of a Stream Dataset:
# 1. Time-Based Filtering: Because it tracks offsets, you can query a Stream to instantly find every note playing exactly on beat 3, or grab everything between beats 10 and 20.
# 2. Recursive Nesting: Streams can hold other Streams. A Score Stream holds a list of Part Streams, which hold a list of Measure Streams, which finally hold individual Note objects.
# 3. Automatic Attribute Routing: If you ask a Stream for its current keySignature or timeSignature, it will automatically search backwards through its timeline to find the active signature for that moment.

# music21 extends beyond the confines of the bundled corpus and allows us to effortlessly handle our own music files. 
# It will work smoothly as long as they are adhered to support standard formats like musicxml, humdrum or midi
# To achieve this we will make use of the converter module upon providing the path to our file as a string argument. 
# This way converter.parse() creates a music21 stream object our file in this case a music XML existing in the current working directory.
# Therefore its name is all that is needed to create a parsed representation of the work
# parse() automatically creates a stream object so we can definitely use the show() method to view this.
# It is outside of corpus module so we must import the wholesome of the music21 module
if False:
    from music21 import *
    parsed_work = converter.parse('solo-violin-partita-no-2-in-d-minor-j-s-bach-bwv-1004.mxl')
    # parsed_work.show()

    # Once we have obtained a score object either from the corpus or passing it from our own file we may widh to perform various manipulations or anlysis on it.
    # Since music21 strerams are hierarchical meaning that they can contain other streams we need to access the entire nested structure to effectively work with a score.
    # Luckily muisc21 provides the recurse method to enable us to do this conveniently.
    # By default the recurse method, visits all elements in the stream and its substream in a first reversal order
    # In other words it starts with the top level stream and then recursively visits all substreams untill it reaches the leaf nodes of the hierarchy
    # This allows us to Traverse through the entire score accessing and manipulating any element we want.
    # Wheather it's a note, chord, rest or any other element in the score.
    # The recurse method is most effective when used in conjunction with a for Loop.

    # suppose we oddly desire to create a new score that contains only the 16th notes in our original file.
    # First we call the recurse method on past work and assign the results to a variable named recurse work.
    recurse_work = parsed_work.recurse()
    # .recurse() is a fundamental method of music21 for getting into elements contained in a Score, Part, or Measure, where elements such as notes are contained in sub-Stream elements.
    # Returns an iterator that iterates over a list of Music21Objects contained in the Stream, starting with self's elements (unless includeSelf=True in which case, it starts with the element itself), and whenever finding a Stream subclass in self, that Stream subclass's elements.
    # create a new score object
    new_score = stream.Score()

    # Nexts we will iterate through all the note objects inn the score using for element in recursework.notes.
    for element in recurse_work.notes:
        # (property) notes: StreamIterator[NotRest]. 
        # Returns all NotRest objects. (will sometime become simply Note and Chord objects.)
        # Within this loop we can use a conditional statement to check wheather the quarterLenght duration of each note = 0.25.
        if element.quarterLength == 0.125:
            # If the condition is true we append the note to our new score. [remember? no offset, in series]
            new_score.append(element)
            # At the end of this process we have a new score object containing only 16th notes 

    # we can then view and further analyze or manipulate this new score object.
    new_score.show()

# Kindly follow the these regulation for accurate nesting.
'''
It is best practice is to create structures where the TimeSignature goes in the first Measure of the score, as below:

>>> s = stream.Score()
>>> p = stream.Part()
>>> m1 = stream.Measure()
>>> ts = meter.TimeSignature('3/4')
>>> m1.insert(0, ts)
>>> m1.insert(0, note.Note('C#3', type=('half'|(2*0.25)))
>>> n = note.Note()
    n.pitch=pitch.Pitch()
    n.duration=duration.Duration()
>>> m1.insert(1.0, n)
>>> m1.number = 1
>>> p.insert(0, m1)
>>> s.insert(0, p)
>>> s.show('t')
'''


















from music21 import *
parsed_work = converter.parse('solo-violin-partita-no-2-in-d-minor-j-s-bach-bwv-1004.mxl')
recurse_work = parsed_work.recurse()
new_score = stream.Score()
for element in recurse_work.notes:
    if element.quarterLength == 0.25:
        new_score.append(element) 
new_score.show()
