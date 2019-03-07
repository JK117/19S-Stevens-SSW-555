# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom


if __name__ == '__main__':
    test_case = Gedcom("example.ged")
    # url = input("Please input test GEDCOM file url (press ENTER to use default url [./example.ged]): ")

    # Project 02
    # sprint_1_demo.create_arrow_output()
    # sprint_1_demo.print_arrow_records()

    # Project 03 v1
    # sprint_1_demo.record_to_dict()
    # sprint_1_demo.print_table()

    # Project 03 v2
    test_case.set_output_url("pj_03_output.txt")
    test_case.print_pretty_table()
