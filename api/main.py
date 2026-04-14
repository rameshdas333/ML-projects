from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel  # better input validation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Fuel CO2 Emission Predictor")

# Model load
model = pickle.load(open("fuel_model.pkl", "rb"))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Home route
@app.get("/")
def home():
    return {"message": "Fuel Consumption Prediction API is running!"}

# Input model (Pydantic)
class PredictionInput(BaseModel):
    engine_size: float
    cylinders: int
    fuel_consumption_comb: float

    



@app.post("/predict")
def predict(data: PredictionInput):
    # Model expects 2D array [[eng, cyl, fuel_comb]]
    input_array = np.array([[data.engine_size, data.cylinders, data.fuel_consumption_comb]])
    prediction = model.predict(input_array)
    
    return {
        "CO2_Emission_Prediction": round(float(prediction[0]), 2),
        "input": {
            "engine_size": data.engine_size,
            "cylinders": data.cylinders,
            "fuel_consumption_comb": data.fuel_consumption_comb
        }
    }

# Optional: GET method o rakhte parba (query params diye)
@app.get("/predict")
def predict_get(engine_size: float, cylinders: int, fuel_consumption_comb: float):
    input_array = np.array([[engine_size, cylinders, fuel_consumption_comb]])
    prediction = model.predict(input_array)
    return {"CO2_Emission_Prediction": round(float(prediction[0]), 2)}