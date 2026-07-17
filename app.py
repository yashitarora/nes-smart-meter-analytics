from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import os

app = FastAPI(title="NES Smart Meter API", version="1.0")

class PredictionInput(BaseModel):
    features: list[float]

class PredictionOutput(BaseModel):
    prediction: float
    status: str

@app.get("/")
def root():
    return {"message": "NES Smart Meter Analytics API", "version": "1.0"}

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": os.path.exists("model.pkl")}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        # Load model (uncomment when you have model.pkl)
        # with open("model.pkl", "rb") as f:
        #     model = pickle.load(f)
        # prediction = model.predict(np.array(input_data.features).reshape(1, -1))
        
        # Placeholder prediction
        prediction = np.random.uniform(70, 100)
        
        return PredictionOutput(prediction=round(prediction, 2), status="success")
    except Exception as e:
        return PredictionOutput(prediction=0, status=f"error: {str(e)}")

@app.get("/meters")
def list_meters():
    return {
        "meters": ["MTR001", "MTR002", "MTR003", "MTR004", "MTR005"],
        "count": 5
    }
