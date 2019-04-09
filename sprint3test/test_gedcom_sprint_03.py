import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint03(unittest.TestCase):
    # US13
    def test_siblings_spacing(self):
        test_case_13_1 = Gedcom("test_example_13_1")
        test_case_13_1.siblings_spacing()
        test_case_13_1_expected = ["ERROR: US13: Siblings: " + '@I5@' + " and " + '@I4@' + "s' birthdays are not more than 8 months apart or less than 2 days apart."]
        self.assertEqual(test_case_13_1_expected, test_case_13_1.error_list)

        test_case_13_2 = Gedcom("test_example_13_2")
        test_case_13_2.siblings_spacing()
        test_case_13_2_expected = []
        self.assertEqual(test_case_13_2_expected, test_case_13_2.error_list)

    # US14
    def test_multiple_births_less_than_5(self):
        test_case_14_1 = Gedcom("test_example_14_1")
        test_case_14_1.multiple_births_less_than_5()
        test_case_14_1_expected = ["ERROR: US14: 5 or more Siblings in family: " + '@F1@' + " have same birthdays."]
        self.assertEqual(test_case_14_1_expected, test_case_14_1.error_list)

        test_case_14_2 = Gedcom("test_example_14_2")
        test_case_14_2.multiple_births_less_than_5()
        test_case_14_2_expected = []
        self.assertEqual(test_case_14_2_expected, test_case_14_2.error_list)

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

