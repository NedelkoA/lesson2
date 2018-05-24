import unittest
from .stringcalculator import StringCalculator


class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add(''), 0)

    def test_add_2(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('3'), 3)

    def test_add_3(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('1,2'), 3)

    def test_add_4(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('1\n2'), 3)

    def test_add_5(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('1\n2,3\n4'), 10)

    def test_add_6(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('-1,2,-3'), 'Отрицательные числа запрещены: -1,-3')

    def test_add_7(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('1000, 3000, 4, 10, 854'), 1868)

    def test_add_8(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('//#\n1#2'), 3)

    def test_add_9(self):
        str_calc = StringCalculator()
        self.assertEqual(str_calc.add('//###\n1###2'), 3)

