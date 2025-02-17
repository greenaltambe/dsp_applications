import librosa
import numpy as np
from scipy.signal import correlate
import sounddevice as sd
import soundfile as sf
import os
import warnings

# Filter out the deprecation warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

class AudioPasswordAuthenticator:
    def __init__(self, threshold=0.9):
        self.threshold = threshold
        self.sample_rate = 22050  # Default sample rate

    def verify_file_exists(self, file_path):
        """
        Verify if the audio file exists
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        return True

    def load_and_process_audio(self, file_path):
        """
        Load and preprocess audio file
        """
        self.verify_file_exists(file_path)
        
        try:
            # Load audio file with error handling
            audio, sr = librosa.load(file_path, sr=self.sample_rate)
            
            # Apply noise reduction using librosa
            # Using simple high-pass filter to remove low frequency noise
            audio_filtered = librosa.effects.preemphasis(audio)
            
            # Normalize the audio
            audio_normalized = librosa.util.normalize(audio_filtered)
            
            return audio_normalized
        except Exception as e:
            raise Exception(f"Error processing audio file {file_path}: {str(e)}")

    def play_audio(self, audio_signal):
        """
        Play the audio signal
        """
        try:
            sd.play(audio_signal, self.sample_rate)
            sd.wait()  # Wait until audio is finished playing
        except Exception as e:
            print(f"Warning: Could not play audio: {str(e)}")

    def calculate_correlation(self, signal1, signal2):
        """
        Calculate correlation coefficient between two signals
        """
        try:
            # Ensure signals are of same length
            min_length = min(len(signal1), len(signal2))
            signal1 = signal1[:min_length]
            signal2 = signal2[:min_length]
            
            # Calculate correlation coefficient
            correlation = np.corrcoef(signal1, signal2)[0,1]
            return correlation
        except Exception as e:
            raise Exception(f"Error calculating correlation: {str(e)}")

    def authenticate(self, password_file, test_file):
        """
        Authenticate user by comparing stored password and test audio
        """
        try:
            # Load and process both audio files
            print(f"Loading stored password audio from: {password_file}")
            password_audio = self.load_and_process_audio(password_file)
            
            print(f"Loading test password audio from: {test_file}")
            test_audio = self.load_and_process_audio(test_file)
            
            # Play both audios
            print("\nPlaying stored password audio...")
            self.play_audio(password_audio)
            
            print("Playing test password audio...")
            self.play_audio(test_audio)
            
            # Calculate correlation
            correlation = self.calculate_correlation(password_audio, test_audio)
            print(f"\nCorrelation coefficient: {correlation:.4f}")
            
            # Authentication decision
            is_authenticated = correlation >= self.threshold
            
            if is_authenticated:
                print("\nAuthentication successful! ✅")
            else:
                print("\nAuthentication failed! ❌")
                print(f"Correlation {correlation:.4f} is below threshold {self.threshold}")
            
            return is_authenticated, correlation
            
        except Exception as e:
            print(f"Error during authentication: {str(e)}")
            return False, 0.0

def main():
    # Initialize authenticator
    authenticator = AudioPasswordAuthenticator(threshold=0.9)
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # File paths - using os.path.join for proper path handling
    password_file = os.path.join(current_dir, "password_file.mp3")
    test_file = os.path.join(current_dir, "test.mp3")
    
    # Perform authentication
    is_auth, corr = authenticator.authenticate(password_file, test_file)
    
    return is_auth, corr

if __name__ == "__main__":
    main()