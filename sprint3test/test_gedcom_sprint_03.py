import unittest
from gedcom import Gedcom
import us13
import us14
import us15
import us16
import us17
import us18


class TestCheckFunctionsSprint03(unittest.TestCase):
    # US13
    def test_siblings_spacing(self):
        test_case_13_1 = Gedcom("sprint3test/test_example_13_1")
        us13.siblings_spacing(test_case_13_1)
        test_case_13_1_expected = ["ERROR: US13: Siblings: " + '@I5@' + " and " + '@I4@' + "s' birthdays are not more than 8 months apart or less than 2 days apart."]
        self.assertEqual(test_case_13_1_expected, test_case_13_1.error_list)

        test_case_13_2 = Gedcom("sprint3test/test_example_13_2")
        us13.siblings_spacing(test_case_13_2)
        test_case_13_2_expected = []
        self.assertEqual(test_case_13_2_expected, test_case_13_2.error_list)

    # US14
    def test_multiple_births_less_than_5(self):
        test_case_14_1 = Gedcom("sprint3test/test_example_14_1")
        us14.multiple_births_less_than_5(test_case_14_1)
        test_case_14_1_expected = ["ERROR: US14: 5 or more Siblings in family: " + '@F1@' + " have same birthdays."]
        self.assertEqual(test_case_14_1_expected, test_case_14_1.error_list)

        test_case_14_2 = Gedcom("sprint3test/test_example_14_2")
        us14.multiple_births_less_than_5(test_case_14_2)
        test_case_14_2_expected = []
        self.assertEqual(test_case_14_2_expected, test_case_14_2.error_list)

    # US15
    def test_fewer_than_15_siblings(self):
        test_case_15_1 = Gedcom("sprint3test/test_example_15_1")
        us15.fewer_than_15_siblings(test_case_15_1)
        test_case_15_1_expected = []
        self.assertEqual(test_case_15_1_expected, test_case_15_1.error_list)

        test_case_15_2 = Gedcom("sprint3test/test_example_15_2")
        us15.fewer_than_15_siblings(test_case_15_2)
        test_case_16_2_expected = ["ANOMALY: US15: FAMILY: @F1@ has: 16 siblings, more than 15"]
        self.assertEqual(test_case_16_2_expected, test_case_15_2.error_list)

    # US16
    def test_male_last_names(self):
        test_case_16_1 = Gedcom("sprint3test/test_example_16_1")
        us16.male_last_names(test_case_16_1)
        test_case_16_1_expected = []
        self.assertEqual(test_case_16_1_expected, test_case_16_1.error_list)

        test_case_16_2 = Gedcom("sprint3test/test_example_16_2")
        us16.male_last_names(test_case_16_2)
        test_case_16_2_expected = ["ANOMALY: US16: FAMILY: @F1@: Male member: Elizabeth /Miller/: has different last names"]
        self.assertEqual(test_case_16_2_expected, test_case_16_2.error_list)

    # US17
    def test_check_no_marriages_to_descendants(self):
        test_case_17_1 = Gedcom("sprint3test/test_example_17_1")
        us17.check_no_marriages_to_descendants(test_case_17_1)
        test_case_17_1_expected = ['ERROR: US17: FAMILY: @F2@, there is marriage between parents and descendants.']
        self.assertEqual(test_case_17_1_expected, test_case_17_1.error_list)

        test_case_17_2 = Gedcom("sprint3test/test_example_17_2")
        us17.check_no_marriages_to_descendants(test_case_17_2)
        test_case_17_2_expected = []
        self.assertEqual(test_case_17_2_expected, test_case_17_2.error_list)

    # US18
    def test_check_siblings_should_not_marry(self):
        test_case_18_1 = Gedcom("sprint3test/test_example_18_1")
        us18.check_siblings_should_not_marry(test_case_18_1)
        test_case_18_1_expected = ['ERROR: US18: FAMILY: @F2@, there is marriage between siblings.']
        self.assertEqual(test_case_18_1_expected, test_case_18_1.error_list)

        test_case_18_2 = Gedcom("sprint3test/test_example_18_2")
        us18.check_siblings_should_not_marry(test_case_18_2)
        test_case_18_2_expected = []
        self.assertEqual(test_case_18_2_expected, test_case_18_2.error_list)


if __name__ == '__main__':
    class TestCheckFunctionsSprint03(unittest.TestCase):
        # US13
        def test_siblings_spacing(self):
            test_case_13_1 = Gedcom("test_example_13_1")
            us13.siblings_spacing(test_case_13_1)
            test_case_13_1_expected = [
                "ERROR: US13: Siblings: " + '@I5@' + " and " + '@I4@' + "s' birthdays are not more than 8 months apart or less than 2 days apart."]
            self.assertEqual(test_case_13_1_expected, test_case_13_1.error_list)

            test_case_13_2 = Gedcom("test_example_13_2")
            us13.siblings_spacing(test_case_13_2)
            test_case_13_2_expected = []
            self.assertEqual(test_case_13_2_expected, test_case_13_2.error_list)

        # US14
        def test_multiple_births_less_than_5(self):
            test_case_14_1 = Gedcom("test_example_14_1")
            us14.multiple_births_less_than_5(test_case_14_1)
            test_case_14_1_expected = ["ERROR: US14: 5 or more Siblings in family: " + '@F1@' + " have same birthdays."]
            self.assertEqual(test_case_14_1_expected, test_case_14_1.error_list)

            test_case_14_2 = Gedcom("test_example_14_2")
            us14.multiple_births_less_than_5(test_case_14_2)
            test_case_14_2_expected = []
            self.assertEqual(test_case_14_2_expected, test_case_14_2.error_list)

        # US15
        def test_fewer_than_15_siblings(self):
            test_case_15_1 = Gedcom("test_example_15_1")
            us15.fewer_than_15_siblings(test_case_15_1)
            test_case_15_1_expected = []
            self.assertEqual(test_case_15_1_expected, test_case_15_1.error_list)

            test_case_15_2 = Gedcom("test_example_15_2")
            us15.fewer_than_15_siblings(test_case_15_2)
            test_case_16_2_expected = ["ANOMALY: US15: FAMILY: @F1@ has: 16 siblings, more than 15"]
            self.assertEqual(test_case_16_2_expected, test_case_15_2.error_list)

        # US16
        def test_male_last_names(self):
            test_case_16_1 = Gedcom("test_example_16_1")
            us16.male_last_names(test_case_16_1)
            test_case_16_1_expected = []
            self.assertEqual(test_case_16_1_expected, test_case_16_1.error_list)

            test_case_16_2 = Gedcom("test_example_16_2")
            us16.male_last_names(test_case_16_2)
            test_case_16_2_expected = [
                "ANOMALY: US16: FAMILY: @F1@: Male member: Elizabeth /Miller/: has different last names"]
            self.assertEqual(test_case_16_2_expected, test_case_16_2.error_list)

        # US17
        def test_check_no_marriages_to_descendants(self):
            test_case_17_1 = Gedcom("test_example_17_1")
            us17.check_no_marriages_to_descendants(test_case_17_1)
            test_case_17_1_expected = ['ERROR: US17: FAMILY: @F2@, there is marriage between parents and descendants.']
            self.assertEqual(test_case_17_1_expected, test_case_17_1.error_list)

            test_case_17_2 = Gedcom("test_example_17_2")
            us17.check_no_marriages_to_descendants(test_case_17_2)
            test_case_17_2_expected = []
            self.assertEqual(test_case_17_2_expected, test_case_17_2.error_list)

        # US18
        def test_check_siblings_should_not_marry(self):
            test_case_18_1 = Gedcom("test_example_18_1")
            us18.check_siblings_should_not_marry(test_case_18_1)
            test_case_18_1_expected = ['ERROR: US18: FAMILY: @F2@, there is marriage between siblings.']
            self.assertEqual(test_case_18_1_expected, test_case_18_1.error_list)

            test_case_18_2 = Gedcom("test_example_18_2")
            us18.check_siblings_should_not_marry(test_case_18_2)
            test_case_18_2_expected = []
            self.assertEqual(test_case_18_2_expected, test_case_18_2.error_list)

    unittest.main(verbosity=2)

