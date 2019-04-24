import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint04(unittest.TestCase):
    # US27
    def test_list_individual_ages(self):
        test_case_27_1 = Gedcom("test_example_32_1")
        temp_test = test_case_27_1.list_individual_ages()
        test_case_27_1_expected = '''+-------+----------------------+-----+
|   ID  |         Name         | Age |
+-------+----------------------+-----+
|  @I1@ |  Jackson /Williams/  |  77 |
|  @I2@ |    Diana /Smith/     |  82 |
|  @I3@ |   John /Williams/    |  62 |
|  @I4@ | Jennifer /Williams/  |  53 |
|  @I5@ | Elizabeth /Williams/ |  53 |
| @I17@ |   Karen /Miller3/    |  53 |
| @I18@ |   Karen /Miller4/    |  53 |
| @I19@ |   Karen /Miller5/    |  53 |
|  @I6@ |    Sarah /Adams/     |  62 |
|  @I7@ |   Micheal /Davis/    |  64 |
|  @I8@ |  Steven /Williams/   |  34 |
|  @I9@ |   Charles /Davis/    |  22 |
| @I10@ |   Robert /Miller/    |  32 |
| @I11@ |    Karen /Miller/    |  28 |
| @I12@ |    Nancy /Miller/    |  26 |
| @I13@ |    Clark /Murphy/    |  53 |
| @I14@ |   Daniel /Murphy/    |  28 |
| @I15@ |   Ashley /Murphy/    |  25 |
| @I16@ |     Carol /Gray/     |  30 |
+-------+----------------------+-----+'''
        self.assertEqual(test_case_27_1_expected, temp_test)

    # US32
    def test_list_multiple_births(self):
        test_case_32_1 = Gedcom("test_example_32_1")
        temp_test = test_case_32_1.list_multiple_births()
        test_case_32_1_expected = '''+-------+----------------------+------------+
|   ID  |         Name         |  Birthday  |
+-------+----------------------+------------+
|  @I4@ | Jennifer /Williams/  | 1965-05-14 |
|  @I5@ | Elizabeth /Williams/ | 1965-05-14 |
| @I17@ |   Karen /Miller3/    | 1965-05-14 |
| @I18@ |   Karen /Miller4/    | 1965-05-14 |
| @I19@ |   Karen /Miller5/    | 1965-05-14 |
+-------+----------------------+------------+'''
        self.assertEqual(test_case_32_1_expected, temp_test)

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

