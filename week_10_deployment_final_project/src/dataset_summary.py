from pathlib import Path
from utils.csv_tools import read_csv

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "properties.csv"

def main():
    rows = read_csv(DATA_PATH)
    print(f"Loaded {len(rows)} rental properties.")
    rents = [float(r["monthly_rent"]) for r in rows]
    print(f"Average Monthly Rent: INR {sum(rents)/len(rents):,.0f}")
    zones = {r["city_zone"] for r in rows}
    print(f"Zones Covered: {', '.join(sorted(zones))}")

if __name__ == '__main__':
    main()
