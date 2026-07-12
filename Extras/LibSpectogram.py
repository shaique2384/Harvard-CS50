import librosa
import librosa.display as libdis
import matplotlib.pyplot as plt
import numpy as np

# load() loads the audio file. It returns a numpy array of audio sample value that make up the waveform. 
# By default librosa converts a stereo file to mono and resamples it to 22050 hz. 
# This helps speed up and simplify the downstream processing.
waveform, sample_rate = librosa.load('Acoustic Demo.mp3')               # sr=None, mono=False

# spectogram is a visual map showing time on x axis and frequency on the y axis with intensity or amplitude represented with color
# we will also need numpy so impirt numpy as np
# to break a sound down to it's constituent frequencies we will use a fourier transform, ft
# ft takes a complex sound and decomposes it into a combination of pure sine waves at different frequencies(lambda/T), amplitude(y=asin(pi)) and phases(theta or x)
# the basic fourier transform however only shows which frequencies are present and not when those frequencies are occuring in time.\
# to solve this we will use the short time fourier transform, stft
# stft gives us the picture of how frequencies evolve over time by splitting the signal into short overlapping windows or delta t(s) and then apllying ft to each one. Can we use sr for that?
# the result is what we plot as a spectogram

# calculate the Short-Time Fourier Transform
stft = librosa.stft(waveform)                                          
# we will pass our waveform variable and it will return a 2D array;
# each row reprents a frequency bin, the slice of the spectrum measured in hz
# each column represents a window of the short burst of time
# each cell or block or the element in the array is a complex number tells us the phase, amplitude = (x,y) of that frequency at that time
# raw amplitudes can vary over a huge range and don't reflect how we parcieve loudness
# our ears respond to ratios and not to raw numbers and are much more sensitive to quiet sounds than the loud ones
# to better match with hearing experience we will convert these amplitude values to decibels which is a logarithmic scale
# db compresses data to visualize and interprete easily librosa.amplitude_to_db() converts amplitudes to db
# but first we need to convert these complex numbers(a+bj) = (cosx+sinxj) from stft into plar coordinates as it is easy magnitude using abs()[(a^2+b^2)^(1/2)] and phase or Time Alignment/shift using angle()[tan^-1(b/a)]
# we need hear phase[exact time-shift or alignment] but we need it when we want the computer to reconstruct the waveform back to audible sound waves using the inverse stft or istft()
magnitude = np.abs(stft)
phase = np.angle(stft)
# print(f'magnitude: {magnitude }, phase: {phase}')
# for spectogram we don't need phase, so let's use librosa.amplitude_to_db and we get decibels form the magnitude dataset
spectrogram = librosa.amplitude_to_db(magnitude)

# we are now ready to plot the spectogram
# Create a window
plt.figure(figsize=(10,4))

# display the spectogram as an image. specshow generates spectogram compared to waveshow from before
libdis.specshow(spectrogram, sr=sample_rate, x_axis='time', y_axis='log')
# we are passing in the spectogram data as first argument, then the original sample_rate from librosa.load() into sr of specshow.
# we are also specify the x_axis parameter into 'time'
# we also specify the y_axis parameter into 'log'; logarithmic where the lower frequencies spread out more and higher frequencies are compressed like our perception of pitch
# Let's add a colorbar next to the plot to show the db values corresponding with the color using plt.colorbar()
plt.colorbar()
plt.title('Spectogram (dB)')
plt.tight_layout
plt.show()