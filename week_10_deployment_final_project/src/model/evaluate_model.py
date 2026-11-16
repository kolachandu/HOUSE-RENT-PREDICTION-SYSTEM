from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.csv_tools import read_csv
from model.predictor import predict_rent

BASE = Path(__file__).resolve().parents[2]

def main():
    rows = read_csv(BASE / "data" / "processed" / "properties_clean.csv")
    errors = []

    for r in rows:
        actual = float(r["monthly_rent"])
        res = predict_rent(
            int(r["bhk"]),
            float(r["area_sqft"]),
            r["city_zone"],
            r["furnishing"],
            int(r["floor_no"])
        )
        pred = res["predicted_rent"]
        errors.append(abs(actual - pred) / actual * 100)

    mape = sum(errors) / len(errors)
    print("=== RENTAL MODEL EVALUATION ===")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
    print(f"Model Pricing Confidence: {100.0 - mape:.2f}%")

if __name__ == "__main__":
    main()
