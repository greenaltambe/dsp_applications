import numpy as np
from scipy.io import wavfile

print("Filtering...")

# Load WAV file
sample_rate, samples = wavfile.read("case3/audio.wav")

# Normalize to float (-1 to 1)
samples = samples.astype(np.float32) / 32768.0

# Filter coefficients
h = np.array([
    -0.0009, -0.0011, -0.0008,  0.0001,  0.0014,  0.0027,  0.0028,  0.0011,
    -0.0024, -0.0063, -0.0081, -0.0054,  0.0020,  0.0116,  0.0182,  0.0162,
     0.0033, -0.0173, -0.0365, -0.0421, -0.0237,  0.0217,  0.0868,  0.1555,
     0.2077,  0.2272,  0.2077,  0.1555,  0.0868,  0.0217, -0.0237, -0.0421,
    -0.0365, -0.0173,  0.0033,  0.0162,  0.0182,  0.0116,  0.0020, -0.0054,
    -0.0081, -0.0063, -0.0024,  0.0011,  0.0028,  0.0027,  0.0014,  0.0001,
    -0.0008, -0.0011, -0.0009
])


# Apply convolution
filtered_output = np.convolve(samples, h, mode="same")

# Convert back to 16-bit PCM
filtered_output = np.int16(filtered_output * 32768)

# Save filtered output
wavfile.write("case3/filtered_output.wav", sample_rate, filtered_output)

print("Filtering completed successfully...")
