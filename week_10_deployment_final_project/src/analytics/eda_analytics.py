from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.csv_tools import read_csv

BASE = Path(__file__).resolve().parents[2]

def main():
    rows = read_csv(BASE / "data" / "processed" / "properties_clean.csv")
    rents = [float(r["monthly_rent"]) for r in rows]
    areas = [float(r["area_sqft"]) for r in rows]

    rates = [r/a for r, a in zip(rents, areas)]
    print("=== HOUSE RENTAL MARKET EXPLORATORY ANALYSIS ===")
    print(f"Properties Sampled  : {len(rows)}")
    print(f"Mean Price / SqFt   : INR {sum(rates)/len(rates):.2f}")
    print(f"Lowest Monthly Rent : INR {min(rents):,.0f}")
    print(f"Highest Monthly Rent: INR {max(rents):,.0f}")

if __name__ == "__main__":
    main()
