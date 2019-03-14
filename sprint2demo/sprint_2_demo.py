# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom


if __name__ == '__main__':
    sprint_2_demo = Gedcom("sprint_2_test")
    sprint_2_demo.set_output_url("spirnt_2_demo_output.txt")
    sprint_2_demo.print_pretty_table()
    sprint_2_demo.check_all_objects_sprint_2()
