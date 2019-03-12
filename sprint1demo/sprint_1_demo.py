# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom


if __name__ == '__main__':
    sprint_1_demo = Gedcom("sprint_1_test")
    sprint_1_demo.set_output_url("spirnt_1_demo_output.txt")
    sprint_1_demo.print_pretty_table()
    sprint_1_demo.check_all_objects_sprint_1()
