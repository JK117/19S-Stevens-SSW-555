# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom
import us02
import us04


if __name__ == '__main__':
    test_case = Gedcom("sprint1demo/sprint_1_test")
    # url = input("Please input test GEDCOM file url (press ENTER to use default url [./example.ged]): ")

    # Project 02
    # sprint_1_demo.create_arrow_output()
    # sprint_1_demo.print_arrow_records()

    # Project 03 v1
    # sprint_1_demo.record_to_dict()
    # sprint_1_demo.print_table()

    # Project 03 v2

    us02.check_birth_b4_marr(test_case)
    us04.check_marr_b4_div(test_case)

    # test_case.set_output_url("test_output.txt")
    # test_case.print_pretty_table()
    print(test_case.error_list)
