import librosa

def preprocess_audio(audio_data):
    """
    Preprocess raw audio data (or text data from files).
    :param audio_data: Raw data from the file.
    :return: Preprocessed data.
    """
    processed_data = audio_data.lower().strip()  # Example preprocessing logic
    return processed_data

def extract_audio_features(file_path):
    """
    Extract MFCC features from a .wav file.
    :param file_path: Path to the .wav file.
    :return: Extracted features as a list.
    """
    try:
        y, sr = librosa.load(file_path, sr=None)  # Load audio file
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # Extract MFCCs
        return mfccs.mean(axis=1).tolist()  # Return mean of MFCCs
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None
