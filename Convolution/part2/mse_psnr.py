import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_file(mp3_file, format="mp3")
    audio.export(wav_file, format="wav")

def calculate_mse_psnr(original_file, filtered_file):
    # Read original and filtered audio files
    sample_rate1, original_signal = wavfile.read(original_file)
    sample_rate2, filtered_signal = wavfile.read(filtered_file)
    
    # Ensure both files have the same sampling rate
    if sample_rate1 != sample_rate2:
        raise ValueError("Sampling rates do not match!")
    
    # Convert signals to float for computation
    original_signal = original_signal.astype(np.float32)
    filtered_signal = filtered_signal.astype(np.float32)
    
    # Ensure both signals have the same length
    min_len = min(len(original_signal), len(filtered_signal))
    original_signal = original_signal[:min_len]
    filtered_signal = filtered_signal[:min_len]
    
    # Compute MSE
    mse = np.mean((original_signal - filtered_signal) ** 2)
    
    # Compute PSNR
    max_val = np.max(original_signal)  # Maximum possible signal value
    psnr = 10 * np.log10((max_val ** 2) / mse) if mse > 0 else float('inf')
    
    return mse, psnr

# Convert MP3 to WAV
# mp3_audio = "case3/audio.mp3"
# wav_audio = "case3/audio.wav"
# convert_mp3_to_wav(mp3_audio, wav_audio)

# Paths to input audio files
original_audio = "case3/audio.wav"
filtered_audio = "case3/filtered_output.wav"

# Compute MSE and PSNR
mse, psnr = calculate_mse_psnr(original_audio, filtered_audio)

# Print results
print(f"MSE: {mse}")
print(f"PSNR: {psnr} dB")
