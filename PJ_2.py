# Project 02 for SSW-555
# Author: Jiakuan Fan

import re


class Gedcom():
    def __init__(self):
        self.record_arr = []
        self.output_arr = []
        self.tier_0_tag = ['HEAD', 'TRLR', 'NOTE']
        self.tier_1_tag = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        self.tier_2_tag = ['DATE']

    def load_file(self, file_url):
        if file_url == '':
            file_url = "./example.ged"
        f = open(file_url, "r")
        self.record_arr = f.readlines()
        f.close()

        for i in range(len(self.record_arr)):
            self.record_arr[i] = self.record_arr[i].strip('\n')
        # print(lines)

        for line in self.record_arr:
            if len(line) == 0:
                self.record_arr.remove(line)
        # print(lines)

    def create_output(self):
        for i in range(len(self.record_arr)):
            line_arr = self.record_arr[i].split(' ')
            output_str = '<-- '
            # print(line_arr)
            if line_arr[0] == '0':
                if line_arr[1] in self.tier_0_tag and len(line_arr) == 2:
                    output_str += '0|' + line_arr[1] + '|Y'
                elif line_arr[1] in self.tier_0_tag and len(line_arr) > 2:
                    output_str += '0|' + line_arr[1] + '|Y|' + str(' '.join(line_arr[2:]))
                elif len(line_arr) == 3 and line_arr[2] == 'INDI':
                    output_str += '0|INDI|Y|' + line_arr[1]
                elif len(line_arr) == 3 and line_arr[2] == 'FAM':
                    output_str += '0|FAM|Y|' + line_arr[1]
                elif len(line_arr) == 2:
                    output_str += '0|' + line_arr[1] + '|N'
                else:
                    output_str += '0|' + line_arr[1] + '|N|' + str(' '.join(line_arr[2:]))
            if line_arr[0] == '1':
                if line_arr[1] in self.tier_1_tag:
                    output_str += '1|' + line_arr[1] + '|Y|' + str(' '.join(line_arr[2:]))
                else:
                    output_str += '1|' + line_arr[1] + '|N|' + str(' '.join(line_arr[2:]))
            if line_arr[0] == '2':
                if line_arr[1] in self.tier_2_tag:
                    output_str += '2|' + line_arr[1] + '|Y|' + str(' '.join(line_arr[2:]))
                else:
                    output_str += '2|' + line_arr[1] + '|N|' + str(' '.join(line_arr[2:]))
            self.output_arr.append(output_str)

    def print_records(self):
        for i in range(len(self.record_arr)):
            print('--> ' + self.record_arr[i])
            print(self.output_arr[i])


if __name__ == '__main__':
    test_case = Gedcom()
    url = input("Please input test GEDCOM file url (press ENTER to use default url [./example.ged]): ")
    test_case.load_file(url)
    test_case.create_output()
    test_case.print_records()
