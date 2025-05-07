import unittest
import pandas as pd
from main import load_data, calculate_average

class TestMainFunctions(unittest.TestCase):
    def test_load_data(self):
        data = load_data("data/sample_data.csv")
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)

    def test_calculate_average(self):
        data = pd.DataFrame({
            "alter": [30, 25, 35],
            "ergebnis": [85, 92, 78]
        })
        self.assertEqual(calculate_average(data, "alter"), 30.0)
        self.assertEqual(calculate_average(data, "ergebnis"), 85.0)

if __name__ == "__main__":
    unittest.main()