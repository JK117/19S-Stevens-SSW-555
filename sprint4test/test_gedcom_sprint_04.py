import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint04(unittest.TestCase):
    # US19
    # def test_siblings_spacing(self):
    #     test_case_13_1 = Gedcom("test_example_13_1")
    #     test_case_13_1.siblings_spacing()
    #     test_case_13_1_expected = ["ERROR: US13: Siblings: " + '@I5@' + " and " + '@I4@' + "s' birthdays are not more than 8 months apart or less than 2 days apart."]
    #     self.assertEqual(test_case_13_1_expected, test_case_13_1.error_list)
    #
    #     test_case_13_2 = Gedcom("test_example_13_2")
    #     test_case_13_2.siblings_spacing()
    #     test_case_13_2_expected = []
    #     self.assertEqual(test_case_13_2_expected, test_case_13_2.error_list)

    # US20
    # def test_multiple_births_less_than_5(self):
    #     test_case_14_1 = Gedcom("test_example_14_1")
    #     test_case_14_1.multiple_births_less_than_5()
    #     test_case_14_1_expected = ["ERROR: US14: 5 or more Siblings in family: " + '@F1@' + " have same birthdays."]
    #     self.assertEqual(test_case_14_1_expected, test_case_14_1.error_list)
    #
    #     test_case_14_2 = Gedcom("test_example_14_2")
    #     test_case_14_2.multiple_births_less_than_5()
    #     test_case_14_2_expected = []
    #     self.assertEqual(test_case_14_2_expected, test_case_14_2.error_list)

    # US21
    def test_correct_gender_for_role(self):
        test_case_21_1 = Gedcom("test_example_21_1")
        test_case_21_1.correct_gender_for_role()
        test_case_21_1_expected = ["ERROR: US21: FAMILY: @F1@: Husband: @I1@: Gender is not male"]
        self.assertEqual(test_case_21_1_expected, test_case_21_1.error_list)

        test_case_21_2 = Gedcom("test_example_21_2")
        test_case_21_2.correct_gender_for_role()
        test_case_21_2_expected = ["ERROR: US21: FAMILY: @F1@: Wife: @I2@: Gender is not female"]
        self.assertEqual(test_case_21_2_expected, test_case_21_2.error_list)

    # US25
    def test_unique_first_names_in_families(self):
        test_case_25_1 = Gedcom("test_example_25_1")
        test_case_25_1.unique_first_names_in_families()
        test_case_25_1_expected = []
        self.assertEqual(test_case_25_1_expected, test_case_25_1.error_list)

        test_case_25_2 = Gedcom("test_example_25_2")
        test_case_25_2.unique_first_names_in_families()
        test_case_25_2_expected = ["ANOMALY: US25: FAMILY: @F1@: Children: ['@I4@', '@I5@']: "
                                   "Has duplicated name and birthday"]
        self.assertEqual(test_case_25_2_expected, test_case_25_2.error_list)

    # US23
    def test_check_unique_name_and_birth_date(self):
        test_case_23_1 = Gedcom("test_example_23_1")
        test_case_23_1.check_unique_name_and_birth_date()
        test_case_23_1_expected = ["ANOMALY: US23: INDIVIDUAL: ['@I1@', '@I2@'] are duplicated."]
        self.assertEqual(test_case_23_1_expected, test_case_23_1.error_list)

        test_case_23_2 = Gedcom("test_example_23_2")
        test_case_23_2.check_unique_name_and_birth_date()
        test_case_23_2_expected = []
        self.assertEqual(test_case_23_2_expected, test_case_23_2.error_list)

    # US24
    def test_check_unique_families_by_spouses(self):
        test_case_24_1 = Gedcom("test_example_24_1")
        test_case_24_1.check_unique_families_by_spouses()
        test_case_24_1_expected = ["ANOMALY: US24: FAMILY: ['@F1@', '@F2@'] are duplicated."]
        self.assertEqual(test_case_24_1_expected, test_case_24_1.error_list)

        test_case_24_2 = Gedcom("test_example_24_2")
        test_case_24_2.check_unique_families_by_spouses()
        test_case_24_2_expected = []
        self.assertEqual(test_case_24_2_expected, test_case_24_2.error_list)


if __name__ == '__main__':
    unittest.main()

