import unittest
import csv
import solution


class TestSolutionUnit(unittest.TestCase):
    def test_arg1(self):
        arg1_test = ('input.cv', 'input')
        for arg1 in arg1_test:
            with self.assertRaises(TypeError):
                solution.check_arg1(arg1)

    def test_arg2(self):
        arg2_test = ('same_name', '', 543)
        for arg2 in arg2_test:
            with self.assertRaises(ValueError):
                solution.check_arg2(arg2)

    def test_fieldnames(self):
        with self.assertRaises(AttributeError):
            with open('test.csv', 'r') as test_csv:
                read_test = csv.DictReader(test_csv)
                solution.check_fieldnames(read_test.fieldnames)


if __name__ == '__main__':
    unittest.main()
