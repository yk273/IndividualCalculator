import unittest
from src.Calculator import Calculate


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculate()

# instantiation
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculate)

# addition
    def test_addition(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)

# subtraction
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.result, 0)

# multiplication
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.result, 12)

# division
    def test_division(self):
        self.assertEqual(self.calculator.divide(8, 2), 4)
        self.assertEqual(self.calculator.result, 4)

# square
    def test_square(self):
        self.assertEqual(self.calculator.square(4), 16)
        self.assertEqual(self.calculator.result, 16)

# square root
    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(16), 4)
        self.assertEqual(self.calculator.result, 4)

# result
    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
