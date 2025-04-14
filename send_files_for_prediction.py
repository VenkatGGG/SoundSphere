import os
import requests

# Ensure this matches the order of classes your model was trained on!
CLASS_NAMES = ["fan", "gearbox", "pump", "valve"]

def send_to_api(file_path, log_file):
    """
    Send .wav file path to FastAPI endpoint for prediction and log results.
    :param file_path: Path to the .wav file.
    :param log_file: File object to log predictions.
    """
    url = "http://127.0.0.1:8000/predict/files/"
    payload = {"file_path": file_path}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        prediction = response.json()
        predicted_class = prediction.get("predicted_class", None)
        confidence = prediction.get("confidence", None)

        # Handle predicted_class (convert to class name)
        try:
            predicted_class_index = int(predicted_class) if predicted_class is not None else None
            predicted_class_name = CLASS_NAMES[predicted_class_index] if predicted_class_index is not None else "Unknown"
        except (ValueError, IndexError, TypeError) as e:
            predicted_class_name = "Unknown"
            print(f"Error parsing predicted_class: {e}")

        # Handle confidence (ensure it is a float)
        try:
            confidence = float(confidence) if confidence is not None else None
        except (ValueError, TypeError) as e:
            confidence = None
            print(f"Error parsing confidence: {e}")

        # Print prediction to terminal
        print(f"\nPrediction for {file_path}:")
        print(f"  Predicted Class: {predicted_class_name}")
        if confidence is not None:
            print(f"  Confidence: {confidence:.5f}")
        else:
            print(f"  Confidence: Not available")

        # Save beautified prediction to file
        log_file.write(f"Audio File: {file_path}\n")
        log_file.write(f"Predicted Class: {predicted_class_name}\n")
        if confidence is not None:
            log_file.write(f"Confidence: {confidence:.5f}\n")
        else:
            log_file.write("Confidence: Not available\n")
        log_file.write("-" * 40 + "\n")
    else:
        error_message = f"Error for {file_path}: {response.status_code}, {response.text}"
        print(error_message)
        log_file.write(f"{error_message}\n")
        log_file.write("-" * 40 + "\n")

def process_folder(folder_path, log_file):
    """
    Process all .wav files in a folder and send them for prediction.
    :param folder_path: Path to the folder containing .wav files.
    :param log_file: File object to log predictions.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                print(f"\nProcessing {file_path}...")
                send_to_api(file_path, log_file)

if __name__ == "__main__":
    # Define folders to process
    base_folder = "input_files"
    subfolders = ["valve", "pump", "fan", "gearbox"]
    
    # Open log file for writing predictions
    with open("prediction_results.txt", "w") as log_file:
        log_file.write("Prediction Results\n")
        log_file.write("=" * 40 + "\n\n")
        
        for subfolder in subfolders:
            folder_path = os.path.join(base_folder, subfolder)
            print(f"\nProcessing folder: {folder_path}")
            log_file.write(f"Processing folder: {folder_path}\n")
            process_folder(folder_path, log_file)
