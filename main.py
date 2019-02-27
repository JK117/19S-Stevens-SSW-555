# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom


if __name__ == '__main__':
    test_case = Gedcom()
    # url = input("Please input test GEDCOM file url (press ENTER to use default url [./example.ged]): ")
    test_case.load_file('')

    # Project 02
    # test_case.create_arrow_output()
    # test_case.print_arrow_records()

    # Project 03 v1
    # test_case.record_to_dict()
    # test_case.print_table()

    # Project 03 v2
    test_case.separate_line()
    test_case.create_indi_object()
    test_case.create_fam_object()
    test_case.print_pretty_table()
