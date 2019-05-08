# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

import sys
import getopt
from gedcom import Gedcom
import us01
import us02
import us03
import us04
import us05
import us06
import us07
import us08
import us09
import us10
import us12
import us22
import us13
import us14
import us15
import us16
import us17
import us18


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hetf:", ["help", "example", "test", "file_url="])
    except getopt.GetoptError:
        print('Error: run_gedcom.py -f <file_url>')
        print('   or: run_gedcom.py --file <file_url>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("run_gedcom.py -h: show help info")
            print("              -e: run example gedcom file")
            print("              -t: run unittest")
            print("              -f <file_url>: run with input file")
            print("           or --help: show help info")
            print("              --example: run example gedcom file")
            print("              --test: run unittest")
            print("              --file <file_url>: run with input file")
            sys.exit()
        # elif opt in ("-t", "--test"):

        elif opt in ("-e", "--example"):
            example_case = Gedcom("example.ged")
            example_case.set_output_url("example_case_output.txt")
            example_case.print_pretty_table()
        elif opt in ("-f", "--file"):
            run_case = Gedcom(arg)
            run_case.set_output_url("run_case_output.txt")
            run_case.print_pretty_table()


if __name__ == '__main__':
    # test_case = Gedcom("sprint1demo/sprint_1_test")
    # url = input("Please input test GEDCOM file url (press ENTER to use default url [./example.ged]): ")

    # Project 02
    # sprint_1_demo.create_arrow_output()
    # sprint_1_demo.print_arrow_records()

    # Project 03

    # test_case.set_output_url("test_output.txt")
    # test_case.print_pretty_table()
    main()
