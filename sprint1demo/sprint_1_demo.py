# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom
import us01
import us02
import us03
import us04
import us05
import us06


if __name__ == '__main__':
    sprint_1_demo = Gedcom("sprint_1_test")
    sprint_1_demo.set_output_url("spirnt_1_demo_output.txt")
    sprint_1_demo.print_pretty_table()

    us01.check_date_b4_current(sprint_1_demo)
    us02.check_birth_b4_marr(sprint_1_demo)
    us03.check_birth_b4_death(sprint_1_demo)
    us04.check_marr_b4_div(sprint_1_demo)
    us05.check_marr_b4_death(sprint_1_demo)
    us06.check_div_b4_death(sprint_1_demo)

    output_stream = open(sprint_1_demo.output_url, "a")
    output_stream.write("Errors:\n")
    for error in sprint_1_demo.error_list:
        print(error)
        output_stream.write(error + '\n')
    output_stream.close()
