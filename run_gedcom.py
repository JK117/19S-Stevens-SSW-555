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
import us21
import us23
import us24
import us25


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
            # example_case = Gedcom("example.ged")
            # example_case.set_output_url("example_case_output.txt")
            # example_case.print_pretty_table()
            run_gedcom("example.ged", "example_case_output.txt")
        elif opt in ("-f", "--file"):
            # run_case = Gedcom(arg)
            # run_case.set_output_url("run_case_output.txt")
            # run_case.print_pretty_table()
            run_gedcom(arg, "run_case_output.txt")


def run_gedcom(input_url, output_url):
    run_case = Gedcom(input_url)
    run_case.set_output_url(output_url)
    run_case.print_pretty_table()

    us01.check_date_b4_current(run_case)
    us02.check_birth_b4_marr(run_case)
    us03.check_birth_b4_death(run_case)
    us04.check_marr_b4_div(run_case)
    us05.check_marr_b4_death(run_case)
    us06.check_div_b4_death(run_case)
    us07.check_less_then_150_years_old(run_case)
    us08.check_birth_b4_marriage_of_parents(run_case)
    us09.check_birth_b4_death_of_parents(run_case)
    us10.check_marriage_after_14(run_case)
    us12.check_parents_not_too_old(run_case)
    us22.check_unique_id(run_case)
    us13.siblings_spacing(run_case)
    us14.multiple_births_less_than_5(run_case)
    us15.fewer_than_15_siblings(run_case)
    us16.male_last_names(run_case)
    us17.check_no_marriages_to_descendants(run_case)
    us18.check_siblings_should_not_marry(run_case)
    us21.correct_gender_for_role(run_case)
    us23.check_unique_name_and_birth_date(run_case)
    us24.check_unique_families_by_spouses(run_case)
    us25.unique_first_names_in_families(run_case)

    output_stream = open(run_case.output_url, "a")
    output_stream.write("Errors:\n")
    for error in run_case.error_list:
        print(error)
        output_stream.write(error + '\n')
    output_stream.close()


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
