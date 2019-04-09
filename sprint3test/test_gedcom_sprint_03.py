import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint03(unittest.TestCase):
    # US15
    def test_fewer_than_15_siblings(self):
        test_case_15_1 = Gedcom("test_example_15_1")
        test_case_15_1.fewer_than_15_siblings()
        test_case_15_1_expected = []
        self.assertEqual(test_case_15_1_expected, test_case_15_1.error_list)

        test_case_15_2 = Gedcom("test_example_15_2")
        test_case_15_2.fewer_than_15_siblings()
        test_case_16_2_expected = ["ANOMALY: US15: FAMILY: @F1@ has: 16 siblings, more than 15"]
        self.assertEqual(test_case_16_2_expected, test_case_15_2.error_list)

    # US16
    def test_male_last_names(self):
        test_case_16_1 = Gedcom("test_example_16_1")
        test_case_16_1.male_last_names()
        test_case_16_1_expected = []
        self.assertEqual(test_case_16_1_expected, test_case_16_1.error_list)

        test_case_16_2 = Gedcom("test_example_16_2")
        test_case_16_2.male_last_names()
        test_case_16_2_expected = ["ANOMALY: US10: FAMILY: @F1@: Male member: Elizabeth /Miller/: has different last names"]
        self.assertEqual(test_case_16_2_expected, test_case_16_2.error_list)


if __name__ == '__main__':
    unittest.main()

