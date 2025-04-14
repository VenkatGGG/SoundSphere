from kafka import KafkaConsumer
import json
import numpy as np
import librosa
import torch
from model import YourModel
from sklearn.preprocessing import StandardScaler

KAFKA_TOPIC = 'motor_sounds'
KAFKA_SERVER = 'localhost:9092'
GROUP_ID = 'motor-sound-consumer'

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    group_id=GROUP_ID,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

model = YourModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()

scaler = StandardScaler()

for message in consumer:
    audio_data = message.value
    audio_file_path = audio_data['file_path']

    audio, sr = librosa.load(audio_file_path, sr=None)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

    mfcc = scaler.fit_transform(mfcc.T).T

    mfcc_tensor = torch.tensor(mfcc).float().unsqueeze(0)

    with torch.no_grad():
        prediction = model(mfcc_tensor)

    predicted_label = 'Anomaly' if prediction.item() > 0.5 else 'Normal'

    print(f"Prediction: {predicted_label}")

consumer.close()
