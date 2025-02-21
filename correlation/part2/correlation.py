import numpy as np
import sounddevice as sd
import scipy.signal as signal
import scipy.io.wavfile as wav
import librosa
import os

def load_audio(file_path, fs=44100):
    audio, sr = librosa.load(file_path, sr=fs, mono=True)
    return audio

def play_audio(audio, fs=44100):
    print("Playing audio...")
    sd.play(audio, samplerate=fs)
    sd.wait()

def preprocess_audio(audio, fs=44100):
    # Apply a bandpass filter (300Hz - 3400Hz for speech)
    lowcut, highcut = 300, 3400
    sos = signal.butter(10, [lowcut, highcut], btype='band', fs=fs, output='sos')
    return signal.sosfilt(sos, audio)

def calculate_correlation(x, y):
    min_length = min(len(x), len(y))  # Ensure both arrays are of the same length
    x, y = x[:min_length], y[:min_length]
    return np.corrcoef(x, y)[0, 1]

def main():
    
    fs = 44100  # Sampling frequency
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    password_file = os.path.join(base_path, "password_file.mp3")
    test_file = os.path.join(base_path, "test.mp3")
    
    print("Loading stored audio password")
    x = load_audio(password_file, fs)
    x = preprocess_audio(x, fs)
    play_audio(x, fs)
    
    print("Loading test audio password")
    y = load_audio(test_file, fs)
    y = preprocess_audio(y, fs)
    play_audio(y, fs)
    
    correlation = calculate_correlation(x, y)
    print(f"Correlation coefficient: {correlation:.4f}")
    
    if correlation > 0.9:
        print("Authentication Successful!")
    else:
        print("Authentication Failed!")

if __name__ == "__main__":
    main()
