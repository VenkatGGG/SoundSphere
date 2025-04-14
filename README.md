SoundSphere - Motor Sound Detection for Anomalous Sound Detection (ASD)

This project focuses on unsupervised anomalous sound detection (ASD) for machine condition monitoring under domain-shifted conditions. 
It leverages a dataset from the DCASE 2021 Challenge Task 2, which involves detecting anomalous machine sounds in the presence of environmental noise.

1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Requirements](#requirements)
5. [Usage](#usage)
6. [Model](#model)
7. [Infrastructure](#infrastructure)
8. [Results](#results)

---

Overview

The aim of this project is to develop a model capable of detecting anomalous motor sounds in real-time under varying operating conditions.
 The system was built for unsupervised anomaly detection, where the goal is to identify anomalous motor sounds from the normal operational 
sounds of machines, even when conditions shift between training and testing.

This system uses a Audio based Anomoly Detectorprocess the audio data, and deploys Kafka for streaming input data and FastAPI for model inference.
 It works with machine sounds from seven types of machines: **fan, gearbox, pump, slide rail, car, train, and valve**, under noisy, real-world conditions.

---
Dataset

The dataset used in this project is from the DCASE 2021 Challenge Task 2 on Anomalous Sound Detection. 
It contains real-world machine sound recordings, including both normal and anomalous operating sounds, with various levels of noise.

Dataset Details:
- Machine Types**:
  - Fan
  - Gearbox
  - Pump
  - Slide Rail
  - Car
  - Train
  - Valve
- Data Composition**:
  - Around 1,000 normal sound clips** per machine type in the source domain (for training).
  - Three normal sound clips per machine in the target domain (for training).
  - Approximately **100 normal and anomalous clips** in both source and target domains for testing.

- Audio Details:
  - 10-second single-channel audio clips.
  - Includes both machine sounds and environmental noise from industrial and domestic environments.
  - Anomalous sounds recorded from deliberately damaged machines.
  
The domain shift includes variations such as:
- Motor speed changes.
- Environmental noise differences between seasons.

### Data Access:
For more information about the dataset and access, refer to the official DCASE 2021 Challenge website: [DCASE 2021](https://dcase.community/).

---

**Installation**

Follow these steps to set up the environment and run the project.

 **Clone the repository**:
```bash
git clone https://github.com/VenkatGGG/SoundSphere.git
cd SoundSphere
```

**Set up the environment**:
We recommend using a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### **Install dependencies**:
```bash
pip install -r requirements.txt
```

---

## **Requirements**

### **Dependencies**:
- Python 3.7+
- Kafka (for streaming input)
- FastAPI (for inference API)
- PyTorch/TensorFlow (for model training)
- librosa (for audio preprocessing)
- scikit-learn (for evaluation)
- numpy, pandas, matplotlib, seaborn (for analysis and visualization)

---

## **Usage**

### **Training the Model**:
To train the motor sound detection model, use the following command:

```bash
python train_model.py
```

This will train the model using the dataset and save the trained model to a specified directory.

### **Inference with FastAPI**:
The FastAPI app is used to deploy the model for inference. You can run the API with the following command:

```bash
uvicorn main:app --reload
```

This will start a development server on `http://127.0.0.1:8000`. You can test it by sending audio data for prediction.

### **Kafka Streaming**:
Kafka is used for streaming motor sound inputs. To stream data to the system, you need to set up the Kafka producer and consumer:

1. **Start Kafka**:
   If you haven’t already, install Kafka and start a Kafka server.
   
2. **Run the Kafka Producer**:
   Stream audio data to Kafka by running the producer:

```bash
python kafka_producer.py
```

3. **Run the Kafka Consumer**:
   The consumer will receive the stream and process the incoming data:

```bash
python kafka_consumer.py
```

---

## **Model**

The model used in this project is designed for **unsupervised anomalous sound detection (ASD)**. The architecture consists of **Convolutional Neural Networks (CNNs)** or **Recurrent Neural Networks (RNNs)**, depending on the feature extraction and modeling strategy used.

### **Model Details**:
- **Input**: 10-second single-channel audio clips.
- **Preprocessing**: Audio features like **Mel-frequency cepstral coefficients (MFCC)** or **Spectrogram** are extracted.
- **Model Type**: CNN or RNN-based architecture to capture temporal and spectral features from the audio.
- **Output**: Anomalous or normal prediction based on the learned patterns.

---

## **Infrastructure**

### **Kafka**:
Kafka is used to stream audio data into the system. The Kafka producer sends real-time motor sound clips to the Kafka broker, while the consumer listens for and processes the audio clips for anomaly detection.

### **FastAPI**:
FastAPI is used for real-time inference. After the model is trained, you can deploy it through FastAPI, allowing you to send requests with motor sound clips for real-time predictions.

---

## **Results**

After training the model, we evaluated it on the test set, considering factors such as:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

The model performs well in detecting anomalous sounds, even under varying conditions, including motor speed changes and environmental noise shifts.

---

## **Contributing**

We welcome contributions! If you'd like to contribute, please follow these steps:
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add new feature'`).
- Push to the branch (`git push origin feature-branch`).
- Create a pull request.

---
