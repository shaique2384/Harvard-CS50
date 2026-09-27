# One final program together!
import cowsay
import pyttsx3
# New friend in the library clan, the pyttsx3 text to speach library.

# We are creating a object they call engine.
engine=pyttsx3.init()
# init() Constructs a new TTS engine instance or reuses the existing instance for the driver name.
this=input('What\'s this? ')
cowsay.cow(this)
engine.say(this)
# say() Adds an utterance to the engine to speak to the event queue.
engine.runAndWait()
# Runs an event loop until all commands queued up until this method call complete. Blocks during the event loop and returns when the queue is cleared.

# The gods of python hope that we have fun solving problems with their blessings.
# Ask questions everyday and ask humans and AIs, the essence of human life.
# As always we learn best when we apply, and oNE final prayer to the PYTHON GODS!SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS!