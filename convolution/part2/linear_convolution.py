from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile

print("Converting MP3 to WAV...")

mp3_file = AudioSegment.from_file("case1/audio.mp3", format="mp3")

wav_file = mp3_file.export("case1/audio.wav", format="wav")

print("Filtering...")
sample_rate, samples = wavfile.read("case1/audio.wav")

samples = samples / 32768.0

x = samples

h = []

y = []
h = [
    -0.0009,
    -0.0011,
    -0.0008,
    0.0001,
    0.0014,
    0.0027,
    0.0028,
    0.0011,
    -0.0024,
    -0.0063,
    -0.0081,
    -0.0054,
    0.0020,
    0.0116,
    0.0182,
    0.0162,
    0.0033,
    -0.0173,
    -0.0365,
    -0.0421,
    -0.0237,
    0.0217,
    0.0868,
    0.1555,
    0.2077,
    0.2272,
    0.2077,
    0.1555,
    0.0868,
    0.0217,
    -0.0237,
    -0.0421,
    -0.0365,
    -0.0173,
    0.0033,
    0.0162,
    0.0182,
    0.0116,
    0.0020,
    -0.0054,
    -0.0081,
    -0.0063,
    -0.0024,
    0.0011,
    0.0028,
    0.0027,
    0.0014,
    0.0001,
    -0.0008,
    -0.0011,
    -0.0009,
]

M = len(h)
L = len(x)
N = L + M - 1
for i in range(N):
    y.append(0)
for i in range(L):
    for j in range(M):
        y[i + j] += x[i] * h[j]

y = np.array(y)

y = np.int16(y * 32768)

wavfile.write("case1/filtered_output.wav", sample_rate, y)

print("Filtering completed successfully...")
