# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom
import us07
import us08
import us09
import us10
import us12
import us22


if __name__ == '__main__':
    sprint_2_demo = Gedcom("sprint_2_test")
    sprint_2_demo.set_output_url("spirnt_2_demo_output.txt")
    sprint_2_demo.print_pretty_table()

    us07.check_less_then_150_years_old(sprint_2_demo)
    us08.check_birth_b4_marriage_of_parents(sprint_2_demo)
    us09.check_birth_b4_death_of_parents(sprint_2_demo)
    us10.check_marriage_after_14(sprint_2_demo)
    us12.check_parents_not_too_old(sprint_2_demo)
    us22.check_unique_id(sprint_2_demo)

    output_stream = open(sprint_2_demo.output_url, "a")
    output_stream.write("Errors:\n")
    for error in sprint_2_demo.error_list:
        print(error)
        output_stream.write(error + '\n')
    output_stream.close()
