# Project for SSW-555
# Author: Jiakuan Fan
# Author: Hangbo Li


class Gedcom():
    def __init__(self):
        self.record_arr = []
        self.output_arr = []
        self.individual = []
        self.families = []
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
        # print(line)

    def record_to_dict(self):
        temp_dict = {}
        for i, line in enumerate(self.record_arr):
            temp_line = line.split(' ')
            if(temp_line[1] != 'HEAD' and temp_line[1] != 'NOTE' and temp_line[1] != 'TRLR'):
                if (temp_line[0] == '0' and (temp_line[2] == 'INDI' )):
                    self.individual.append(temp_dict)
                    temp_dict = {}
                    temp_dict['ID'] = temp_line[1]
                    temp_dict['Alive'] = True
                    temp_dict['Death'] = 'NA'
                elif (temp_line[0] == '0' and  temp_line[2] == 'FAM'):
                    if('Gender' in temp_dict):
                        self.individual.append(temp_dict)
                    else:
                        self.families.append(temp_dict)
                    temp_dict = {}
                    temp_dict['ID'] = temp_line[1]
                    temp_dict['Divorced'] = False
                elif (temp_line[0] == '1' and temp_line[1] == 'NAME'):
                    temp_dict['Name'] = temp_line[2:]
                elif (temp_line[0] == '1' and temp_line[1] == 'SEX'):
                    temp_dict['Gender'] = temp_line[2]
                elif (temp_line[0] == '1' and temp_line[1] == 'BIRT'):
                    temp_dict['Birthday'] = self.record_arr[i+1][2:]
                    temp_dict['Age'] = 2019 - int(self.record_arr[i+1][-1])
                elif (temp_line[0] == '1' and temp_line[1] == 'DEAT'):
                    # print(temp_dict['Birthday'])
                    temp_dict['Age'] = int(self.record_arr[i+1][-1]) - int(temp_dict['Birthday'][-1])
                    temp_dict['Death'] = self.record_arr[i+1][3:]
                elif (temp_line[0] == '1' and temp_line[1] == 'HUSB'):
                    temp_dict['Husband ID'] = temp_line[2]
                elif (temp_line[0] == '1' and temp_line[1] == 'WIFE'):
                    temp_dict['Wife ID'] = temp_line[2]
                elif (temp_line[0] == '1' and temp_line[1] == 'CHIL'):
                    if ('Children' in temp_dict):
                        temp_dict['Children'].append(temp_line[2])
                    else:
                        temp_dict['Children'] = []
                        temp_dict['Children'].append(temp_line[2])
                elif (temp_line[0] == '1' and temp_line[1] == 'MARR'):
                    temp_dict['Married'] = self.record_arr[i+1][2:]

        print(self.families)
        print(self.individual)


    # def create_output(self):
    #     for i in range(len(self.record_arr)):
    #         line_arr = self.record_arr[i].split(' ')
    #         output_str = '<-- '
    #         # print(line_arr)
    #         if line_arr[0] == '0':
    #             if line_arr[1] in self.tier_0_tag and len(line_arr) == 2:
    #                 output_str += '0|' + line_arr[1] + '|Y'
    #             elif line_arr[1] in self.tier_0_tag and len(line_arr) > 2:
    #                 output_str += '0|' + line_arr[1] + '|Y|' + str(' '.join(line_arr[2:]))
    #             elif len(line_arr) == 3 and line_arr[2] == 'INDI':
    #                 output_str += '0|INDI|Y|' + line_arr[1]
    #             elif len(line_arr) == 3 and line_arr[2] == 'FAM':
    #                 output_str += '0|FAM|Y|' + line_arr[1]
    #             elif len(line_arr) == 2:
    #                 output_str += '0|' + line_arr[1] + '|N'
    #             else:
    #                 output_str += '0|' + line_arr[1] + '|N|' + str(' '.join(line_arr[2:]))
    #         if line_arr[0] == '1':
    #             if line_arr[1] in self.tier_1_tag:
    #                 output_str += '1|' + line_arr[1] + '|Y|' + str(' '.join(line_arr[2:]))
    #             else:
    #                 output_str += '1|' + line_arr[1] + '|N|' + str(' '.join(line_arr[2:]))
    #         if line_arr[0] == '2':
    #             if line_arr[1] in self.tier_2_tag:
    #                 output_str += '2|' + line_arr[1] + '|Y|' + str(' '.join(line_arr[2:]))
    #             else:
    #                 output_str += '2|' + line_arr[1] + '|N|' + str(' '.join(line_arr[2:]))
    #         self.output_arr.append(output_str)
    #
    # def print_records(self):
    #     for i in range(len(self.record_arr)):
    #         print('--> ' + self.record_arr[i])
    #         print(self.output_arr[i])


if __name__ == '__main__':
    test_case = Gedcom()
    url = input("Please input test GEDCOM file url (press ENTER to use default url [./example.ged]): ")
    test_case.load_file(url)
    test_case.record_to_dict()
    print(test_case.record_arr)
    # test_case.create_output()
    # test_case.print_records()
