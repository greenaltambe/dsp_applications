from scipy.signal import firwin
import numpy as np

# Filter specifications
fs = 44000  # Sampling frequency
fpass = 4000  # Passband edge frequency
fstop = 6000  # Stopband edge frequency
num_taps = 63  # Filter order (higher = better filtering)

# Design FIR Low Pass Filter
h = firwin(num_taps, cutoff=fpass, fs=fs, pass_zero=True)

# Print the filter coefficients
print("FIR Filter Coefficients:", h)

# Save coefficients to a file (optional)
np.savetxt("fir_coefficients.txt", h)
