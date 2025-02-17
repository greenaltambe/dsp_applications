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
    
    # Convert stereo to mono if necessary
    if len(original_signal.shape) > 1:
        original_signal = np.mean(original_signal, axis=1)
    if len(filtered_signal.shape) > 1:
        filtered_signal = np.mean(filtered_signal, axis=1)

    # Convert signals to float and normalize
    original_signal = original_signal.astype(np.float32) / np.iinfo(np.int16).max
    filtered_signal = filtered_signal.astype(np.float32) / np.iinfo(np.int16).max
    
    # Ensure both signals have the same length
    min_len = min(len(original_signal), len(filtered_signal))
    original_signal = original_signal[:min_len]
    filtered_signal = filtered_signal[:min_len]
    
    # Compute MSE
    mse = np.mean((original_signal - filtered_signal) ** 2)
    
    # Compute PSNR
    max_val = 1.0  # Since signals are normalized
    psnr = 10 * np.log10((max_val ** 2) / mse) if mse > 1e-10 else float('inf')
    
    return mse, psnr

# Paths to input audio files
original_audio = "case3/noise_free.wav"
filtered_audio = "case3/filtered_output.wav"

# Compute MSE and PSNR
mse, psnr = calculate_mse_psnr(original_audio, filtered_audio)

# Print results
print(f"MSE: {mse}")
print(f"PSNR: {psnr} dB")
