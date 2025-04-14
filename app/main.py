from fastapi import FastAPI, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pyAudioAnalysis import audioTrainTest as aT
import os
import uuid

app = FastAPI()

# Serve static files (CSS) and templates (HTML)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Temporary directory for uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

CLASS_NAMES = ["fan", "gearbox", "pump", "valve"]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.wav")
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Run prediction
        c, p, _ = aT.file_classification(file_path, "app/models/motorsoundsmodel", "svm_rbf")
        predicted_class = CLASS_NAMES[int(c)]
        confidence = round(float(max(p)), 5)

        # Clean up: Delete the temporary file
        os.remove(file_path)

        return {
            "filename": file.filename,
            "predicted_class": predicted_class,
            "confidence": confidence
        }
    except Exception as e:
        return {"error": str(e)}
