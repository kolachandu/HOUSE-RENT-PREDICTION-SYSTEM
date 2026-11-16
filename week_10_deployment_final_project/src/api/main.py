from pathlib import Path
import sys
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.csv_tools import read_csv
from model.predictor import predict_rent

BASE = Path(__file__).resolve().parents[2]
app = FastAPI(title="House Rent Prediction API")

class RentRequest(BaseModel):
    bhk: int
    area_sqft: float
    city_zone: str
    furnishing: str
    floor_no: int

@app.get("/")
def home():
    return {"service": "House Rent Prediction API", "status": "running"}

@app.get("/properties")
def list_properties():
    return read_csv(BASE / "data" / "processed" / "properties_clean.csv")

@app.post("/predict-rent")
def predict(req: RentRequest):
    return predict_rent(
        req.bhk,
        req.area_sqft,
        req.city_zone,
        req.furnishing,
        req.floor_no
    )
