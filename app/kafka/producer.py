from kafka import KafkaProducer
import json
import os

KAFKA_TOPIC = 'motor_sounds'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

audio_directory = 'path/to/your/audio/files'

for file_name in os.listdir(audio_directory):
    if file_name.endswith('.wav'):  # Or the file extension of your audio files
        audio_file_path = os.path.join(audio_directory, file_name)
        message = {'file_path': audio_file_path}
        producer.send(KAFKA_TOPIC, value=message)

producer.flush()
producer.close()
