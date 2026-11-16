import unittest
from pathlib import Path
import sys
PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_DIR / "src"))

from model.predictor import predict_rent

class TestRentPrediction(unittest.TestCase):
    def test_larger_area_increases_rent(self):
        small = predict_rent(2, 800, "Tech Corridor", "Semi-Furnished", 2)
        large = predict_rent(2, 1400, "Tech Corridor", "Semi-Furnished", 2)
        self.assertGreater(large["predicted_rent"], small["predicted_rent"])

    def test_furnished_premium(self):
        unfurn = predict_rent(2, 1000, "Downtown", "Unfurnished", 3)
        furn = predict_rent(2, 1000, "Downtown", "Furnished", 3)
        self.assertGreater(furn["predicted_rent"], unfurn["predicted_rent"])

    def test_downtown_multiplier_exceeds_rural(self):
        rural = predict_rent(1, 500, "Rural", "Unfurnished", 1)
        downtown = predict_rent(1, 500, "Downtown", "Unfurnished", 1)
        self.assertGreater(downtown["predicted_rent"], rural["predicted_rent"])

if __name__ == "__main__":
    unittest.main()
