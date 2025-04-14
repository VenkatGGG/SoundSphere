from fastapi import FastAPI
from .model import MotorSounds
from .predictor import predict  

app = FastAPI()

model = YourModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()

@app.on_event("startup")
async def startup_event():
    print("Starting up the FastAPI application...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down the FastAPI application...")

@app.get("/")
async def root():
    return {"message": "Welcome to the Motor Sound Detection API"}

@app.post("/predict")
async def predict_anomalous_sound(audio_file_path: str):
    prediction = predict(audio_file_path, model)
    return {"prediction": prediction}
