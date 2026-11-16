from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))

ZONE_MULT = {"Downtown": 1.45, "Tech Corridor": 1.25, "Suburb": 0.90, "Rural": 0.55}
FURNISH_MULT = {"Furnished": 1.30, "Semi-Furnished": 1.12, "Unfurnished": 1.0}

def predict_rent(bhk: int, area_sqft: float, zone: str, furnishing: str, floor_no: int):
    z_mult = ZONE_MULT.get(zone.title(), 1.0)
    f_mult = FURNISH_MULT.get(furnishing.title(), 1.0)

    # Base formula: (area * 18.5 + bhk * 2500 + floor * 300) * zone * furnish
    base_val = (area_sqft * 16.0) + (bhk * 3000) + (floor_no * 250)
    predicted = base_val * z_mult * f_mult
    predicted = round(predicted, -2) # nearest hundred

    deposit = predicted * 3
    return {
        "predicted_rent": predicted,
        "formatted_rent": f"INR {predicted:,.0f} / mo",
        "estimated_deposit": f"INR {deposit:,.0f} (3 months)",
        "zone_tier": zone.title()
    }

def main():
    print("=== House Rent Predictor CLI ===")
    bhk = int(input("Enter BHK (1, 2, 3, 4): ") or 2)
    area = float(input("Enter area in sq.ft (e.g. 1000): ") or 1000)
    zone = input("City Zone (Downtown / Tech Corridor / Suburb / Rural): ") or "Tech Corridor"
    furnish = input("Furnishing (Furnished / Semi-Furnished / Unfurnished): ") or "Semi-Furnished"
    floor = int(input("Floor number (0 - 30): ") or 3)

    res = predict_rent(bhk, area, zone, furnish, floor)
    print(f"\nEstimated Monthly Rent: {res['formatted_rent']}")
    print(f"Security Deposit Est. : {res['estimated_deposit']}")

if __name__ == "__main__":
    main()
