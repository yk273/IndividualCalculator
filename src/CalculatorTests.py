import unittest
from src.Calculator import Calculate
from csvReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculate()

# instantiation
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculate)

# addition
    def test_addition(self):
        test_data = CSVReader('Unit_Test_Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

# subtraction
    def test_subtraction(self):
        test_data = CSVReader('Unit_Test_Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(float(row['Value 2']), float(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

# multiplication
    def test_multiplication(self):
        test_data = CSVReader('Unit_Test_Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

# division
    def test_division(self):
        test_data = CSVReader('Unit_Test_Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(float(row['Value 2']), float(row['Value 1'])), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

# square
    def test_square(self):
        test_data = CSVReader('Unit_Test_Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(float(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

# square root
    def test_square_root(self):
        test_data = CSVReader('Unit_Test_Square_Root.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square_root(float(row['Value 1'])), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

# result
    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
