# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom
import us13
import us14
import us15
import us16
import us17
import us18


if __name__ == '__main__':
    sprint_3_demo = Gedcom("sprint_3_test")
    sprint_3_demo.set_output_url("spirnt_3_demo_output.txt")
    sprint_3_demo.print_pretty_table()

    us13.siblings_spacing(sprint_3_demo)
    us14.multiple_births_less_than_5(sprint_3_demo)
    us15.fewer_than_15_siblings(sprint_3_demo)
    us16.male_last_names(sprint_3_demo)
    us17.check_no_marriages_to_descendants(sprint_3_demo)
    us18.check_siblings_should_not_marry(sprint_3_demo)

    output_stream = open(sprint_3_demo.output_url, "a")
    output_stream.write("Errors:\n")
    for error in sprint_3_demo.error_list:
        print(error)
        output_stream.write(error + '\n')
    output_stream.close()
