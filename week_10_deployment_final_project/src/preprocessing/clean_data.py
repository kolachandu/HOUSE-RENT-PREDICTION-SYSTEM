from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.csv_tools import read_csv, write_csv

BASE = Path(__file__).resolve().parents[2]

def clean_data():
    raw = read_csv(BASE / "data" / "raw" / "properties.csv")
    cleaned = []
    for r in raw:
        bhk = max(1, int(r["bhk"]))
        area = max(200.0, float(r["area_sqft"]))
        zone = r["city_zone"].strip().title()
        furnish = r["furnishing"].strip().title()
        floor = max(0, int(r["floor_no"]))
        rent = max(3000.0, float(r["monthly_rent"]))

        cleaned.append({
            "prop_id": r["prop_id"].strip(),
            "bhk": str(bhk),
            "area_sqft": f"{area:.0f}",
            "city_zone": zone,
            "furnishing": furnish,
            "floor_no": str(floor),
            "monthly_rent": f"{rent:.0f}"
        })
    write_csv(BASE / "data" / "processed" / "properties_clean.csv", cleaned)
    print(f"Wrote {len(cleaned)} cleaned records to data/processed/properties_clean.csv")

if __name__ == "__main__":
    clean_data()
