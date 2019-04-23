# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom


if __name__ == '__main__':
    sprint_4_demo = Gedcom("sprint_4_test")
    sprint_4_demo.set_output_url("spirnt_4_demo_output.txt")
    sprint_4_demo.print_pretty_table()
    # sprint_4_demo.check_all_objects_sprint_4()
