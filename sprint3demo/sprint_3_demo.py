# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li
# Author: Shan Jiang

from gedcom import Gedcom


if __name__ == '__main__':
    sprint_3_demo = Gedcom("sprint_3_test")
    sprint_3_demo.set_output_url("spirnt_3_demo_output.txt")
    sprint_3_demo.print_pretty_table()
    sprint_3_demo.check_all_objects_sprint_3()
