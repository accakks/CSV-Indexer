import unittest
import csv
import solution


class TestSolutionInt(unittest.TestCase):
    # Test to check original Input (Input1.csv)
    test_output_run = solution.record_linkage('input1.csv', 'same_email')
    with open('output1.csv', 'r') as test_output_csv:
        test_output = dict()
        for row in csv.DictReader(test_output_csv, delimiter="\t"):
            test_output.update(row)

    with open('sample_output.csv', 'r') as sample_output_csv:
        sample_output = dict()
        for row in csv.DictReader(sample_output_csv, delimiter="\t"):
            sample_output.update(row)

    def test_run(self):
        self.assertEqual(self.test_output, self.sample_output)

    # Test to check one more input (input2_test)
    test_output_run_2 = solution.record_linkage(
        'input2_test.csv', 'same_contact')
    with open('output1.csv', 'r') as test_output_2_csv:
        test_output_2 = dict()
        for row in csv.DictReader(test_output_2_csv, delimiter="\t"):
            test_output_2.update(row)

    with open('sample_output_2.csv', 'r') as sample_output_2_csv:
        sample_output_2 = dict()
        for row in csv.DictReader(sample_output_2_csv, delimiter="\t"):
            sample_output_2.update(row)

    def test_run2(self):
        self.assertEqual(self.test_output_2, self.sample_output_2)


if __name__ == '__main__':
    unittest.main()
