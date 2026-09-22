import librosa
import librosa.display
import matplotlib.pyplot as plt

# load() loads the audio file. It returns a numpy array of audio sample value that make up the waveform. 
# By default librosa converts a stereo file to mono and resamples it to 22050 hz. 
# This helps speed up and simplify the downstream processing.
waveform, sample_rate = librosa.load('Acoustic Demo.mp3')               # sr=none, mono=False

# to display the waveform we will use matplot.pipplot
# let's first create a blank canvas to draw our plot on using figure
plt.figure(figsize=(10, 4))

# draw the waveform
librosa.display.waveshow(waveform, sr=sample_rate, color='blue')

# we need title and labels in our plot axis so it's clear what we are looking at
plt.title('Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# let's adjust the layout using tight_layout() so all the simbols fil neatly without overlapping or being cut iff
plt.tight_layout()

# let's display the plot using show()
plt.show()
