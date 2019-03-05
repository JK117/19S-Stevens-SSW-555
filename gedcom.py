import prettytable as pt
from datetime import datetime


def convert_date(date_arr):
    date_obj = datetime.strptime(' '.join(date_arr), '%d %b %Y').date()
    return date_obj


class Gedcom():
    def __init__(self, input_url):
        self.line_list = []
        self.record_list = []
        self.output_list = []
        self.individual_list = []
        self.family_list = []
        self.tier_0_tag = ['HEAD', 'TRLR', 'NOTE']
        self.tier_1_tag = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        self.tier_2_tag = ['DATE']
        self.load_file(input_url)
        self.separate_line()
        self.create_indi_object()
        self.create_fam_object()

    # Load designated text file by line
    # Store into self.line_list
    def load_file(self, input_url):
        if input_url == '':
            input_url = "./example.ged"
        input_stream = open(input_url, "r")
        self.line_list = input_stream.readlines()
        input_stream.close()

        for i in range(len(self.line_list)):
            self.line_list[i] = self.line_list[i].strip('\n')

        for line in self.line_list:
            if len(line) == 0:
                self.line_list.remove(line)

    # Separate every line in line_list into list
    # Store into self.record_list
    def separate_line(self):
        for idx in range(len(self.line_list)):
            self.record_list.append(self.line_list[idx].split(' '))

    # Identify individuals object in self.record_list
    # Store into self.individual_list
    def create_indi_object(self):
        idx = 0
        today = datetime.today().date()
        while idx < len(self.record_list):
            if self.record_list[idx][0] == '0' and self.record_list[idx][1] != 'HEAD' \
                    and self.record_list[idx][1] != 'NOTE' and self.record_list[idx][1] != 'TRLR' \
                    and self.record_list[idx][2] == 'INDI':
                indi_obj = {}
                indi_obj['ID'] = self.record_list[idx][1]
                idx += 1
                while self.record_list[idx][0] != '0':
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'NAME':
                        indi_obj['Name'] = ' '.join(self.record_list[idx][2:])
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'SEX':
                        indi_obj['Gender'] = self.record_list[idx][2]
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'BIRT':
                        idx += 1
                        if self.record_list[idx][0] == '2' and self.record_list[idx][1] == 'DATE':
                            indi_obj['Birthday'] = convert_date(self.record_list[idx][2:])
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'DEAT':
                        idx += 1
                        if self.record_list[idx][0] == '2' and self.record_list[idx][1] == 'DATE':
                            indi_obj['Death'] = convert_date(self.record_list[idx][2:])
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'FAMC':
                        indi_obj['Child'] = self.record_list[idx][2]
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'FAMS':
                        indi_obj['Spouse'] = self.record_list[idx][2]
                    if 'Birthday' in indi_obj.keys() and 'Death' not in indi_obj.keys():
                        indi_obj['Age'] = today.year - indi_obj['Birthday'].year - ((today.month, today.day) < (indi_obj['Birthday'].month, indi_obj['Birthday'].day))
                        indi_obj['Alive'] = True
                    if 'Birthday' in indi_obj.keys() and 'Death' in indi_obj.keys():
                        indi_obj['Age'] = indi_obj['Death'].year - indi_obj['Birthday'].year - ((indi_obj['Death'].month, indi_obj['Death'].day) < (indi_obj['Birthday'].month, indi_obj['Birthday'].day))
                        indi_obj['Alive'] = False
                    idx += 1
                self.individual_list.append(indi_obj)
                # print(indi_obj)
            else:
                idx += 1

    # Identify family objects in self.record_list
    # Store into self.family_list
    def create_fam_object(self):
        idx = 0
        while idx < len(self.record_list):
            if self.record_list[idx][0] == '0' and self.record_list[idx][1] != 'HEAD' \
                    and self.record_list[idx][1] != 'NOTE' and self.record_list[idx][1] != 'TRLR' \
                    and self.record_list[idx][2] == 'FAM':
                fam_obj = {}
                fam_obj['ID'] = self.record_list[idx][1]
                fam_obj['Children'] = []
                idx += 1
                while self.record_list[idx][0] != '0':
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'HUSB':
                        fam_obj['Husband ID'] = self.record_list[idx][2]
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'WIFE':
                        fam_obj['Wife ID'] = self.record_list[idx][2]
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'CHIL':
                        fam_obj['Children'].append(self.record_list[idx][2])
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'MARR':
                        idx += 1
                        if self.record_list[idx][0] == '2' and self.record_list[idx][1] == 'DATE':
                            fam_obj['Married'] = convert_date(self.record_list[idx][2:])
                    if self.record_list[idx][0] == '1' and self.record_list[idx][1] == 'DIV':
                        idx += 1
                        if self.record_list[idx][0] == '2' and self.record_list[idx][1] == 'DATE':
                            fam_obj['Divorced'] = convert_date(self.record_list[idx][2:])
                    idx += 1
                self.family_list.append(fam_obj)
                # print(fam_obj)
            else:
                idx += 1

    def print_pretty_table(self):
        indi_pt = pt.PrettyTable()
        indi_pt.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
        for individual in self.individual_list:
            if 'Death' in individual.keys():
                table_death = str(individual['Death'])
            else:
                table_death = 'NA'
            if 'Child' in individual.keys():
                table_child = individual['Child']
            else:
                table_child = 'NA'
            if 'Spouse' in individual.keys():
                table_spouse = individual['Spouse']
            else:
                table_spouse = 'NA'
            indi_pt.add_row([individual['ID'], individual['Name'], individual["Gender"], str(individual['Birthday']), individual['Age'], individual['Alive'],
                             table_death, table_child, table_spouse])
        print(indi_pt)

        fam_pt = pt.PrettyTable()
        fam_pt.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
        for family in self.family_list:
            for individual in self.individual_list:
                if individual['ID'] == family['Husband ID']:
                    family['Husband Name'] = individual['Name']
                if individual['ID'] == family['Wife ID']:
                    family['Wife Name'] = individual['Name']
            if 'Children' in family.keys():
                table_children = family['Children']
            else:
                table_children = 'NA'
            if 'Divorced' in family.keys():
                table_divorced = str(family['Divorced'])
            else:
                table_divorced = 'NA'
            fam_pt.add_row([family['ID'], str(family['Married']), table_divorced, family['Husband ID'],
                            family['Husband Name'], family['Wife ID'], family["Wife Name"], table_children])
        print(fam_pt)

        output_url = "pj_03_output.txt"
        output_stream = open(output_url, "w")
        output_stream.write("Individuals:\n")
        output_stream.write(str(indi_pt))
        output_stream.write("\n")
        output_stream.write("Families:\n")
        output_stream.write(str(fam_pt))
        output_stream.close()

    def record_to_dict(self):
        temp_dict = {}
        for i, line in enumerate(self.line_list):
            temp_line = line.split(' ')
            if temp_line[1] != 'HEAD' and temp_line[1] != 'NOTE' and temp_line[1] != 'TRLR':
                if temp_line[0] == '0' and (temp_line[2] == 'INDI'):
                    self.individual_list.append(temp_dict)
                    temp_dict = {}
                    temp_dict['ID'] = temp_line[1]
                    temp_dict['Alive'] = True
                    temp_dict['Death'] = 'NA'
                elif temp_line[0] == '0' and temp_line[2] == 'FAM':
                    if 'Gender' in temp_dict:
                        self.individual_list.append(temp_dict)
                    else:
                        self.family_list.append(temp_dict)
                    temp_dict = {}
                    temp_dict['ID'] = temp_line[1]
                    temp_dict['Divorced'] = False
                elif temp_line[0] == '1' and temp_line[1] == 'NAME':
                    temp_dict['Name'] = temp_line[2:]
                elif temp_line[0] == '1' and temp_line[1] == 'SEX':
                    temp_dict['Gender'] = temp_line[2]
                elif temp_line[0] == '1' and temp_line[1] == 'BIRT':
                    temp_dict['Birthday'] = self.line_list[i + 1][2:]
                    # print(self.line_list[i+1][-4:])
                    temp_dict['Age'] = 2019 - int(self.line_list[i + 1][-4:])
                    # print(temp_dict['Age'])
                    # print(temp_dict['ID'])
                elif temp_line[0] == '1' and temp_line[1] == 'DEAT':
                    # print(temp_dict['Birthday'])
                    temp_dict['Age'] = int(self.line_list[i + 1][-4:]) - int(temp_dict['Birthday'][-4:])
                    # print(temp_dict['Age'])
                    # print(temp_dict['ID'])
                    temp_dict['Death'] = self.line_list[i + 1][3:]
                elif temp_line[0] == '1' and temp_line[1] == 'HUSB':
                    temp_dict['Husband ID'] = temp_line[2]
                elif temp_line[0] == '1' and temp_line[1] == 'WIFE':
                    temp_dict['Wife ID'] = temp_line[2]
                elif temp_line[0] == '1' and temp_line[1] == 'CHIL':
                    if 'Children' in temp_dict:
                        temp_dict['Children'].append(temp_line[2])
                    else:
                        temp_dict['Children'] = []
                        temp_dict['Children'].append(temp_line[2])
                elif temp_line[0] == '1' and temp_line[1] == 'MARR':
                    temp_dict['Married'] = self.line_list[i + 1][6:]
                elif temp_line[0] == '1' and temp_line[1] == 'DIV':
                    temp_dict['Divorced'] = self.line_list[i + 1][6:]

        # print(self.family_list)
        # print(self.individual_list)

    def print_table(self):
        tb = pt.PrettyTable()
        tb.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
        self.individual_list = self.individual_list[1:]
        for item in self.individual_list:
            for family in self.family_list:
                if item['ID'] == family['Husband ID'] or item['ID'] == family['Wife ID']:
                    tempChild = "NA"
                    tempSpouse = family["ID"]
                if item["ID"] in family['Children']:
                    tempChild = family["ID"]
                    tempSpouse = "NA"

            tb.add_row([item['ID'], item['Name'], item["Gender"],item['Birthday'], item['Age'], item['Alive'], item["Death"], tempChild, tempSpouse] )

        print(tb)
        tb2 = pt.PrettyTable()
        tb2.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
        for family in self.family_list:
            for item in self.individual_list:
                if item['ID'] == family['Husband ID']:
                    family['Husband Name'] = item['Name']
                # else:
                #     family['Husband Name'] = "NA"
                if item['ID'] == family['Wife ID']:
                    family['Wife Name'] = item['Name']
                # else:
                #     family['Wife Name'] = 'NA'
            tb2.add_row(
                [family['ID'], family['Married'], family["Divorced"], family['Husband ID'], family['Husband Name'], family['Wife ID'], family["Wife Name"],
                 family['Children']])

        print(tb2)

        outputfile = "pj03_output.txt"
        output = open(outputfile, "w")
        output.write("This is the table of family:\n")
        output.write(str(tb))
        output.write("\n")
        output.write("This is the table of individual_list:\n")
        output.write(str(tb2))
        output.close()

    def check_date_b4_current(self):
        print("HL")

    def check_birth_b4_marr(self):
        for family in self.family_list:
            husband_id = family['Husband ID']
            wife_id = family['Wife ID']
            marr_date = family['Married']
            for individual in self.individual_list:
                if individual['ID'] == husband_id:
                    husband_birth = individual['Birthday']
                    if husband_birth > marr_date:
                        return False
                if individual['ID'] == wife_id:
                    wife_birth = individual['Birthday']
                    if wife_birth > marr_date:
                        return False
        return True

    def check_birth_b4_death(self):
        print("SJ")

    def check_marr_b4_div(self):
        for family in self.family_list:
            if 'Divorced' in family.keys():
                if family['Divorced'] < family['Married']:
                    return False
        return True

    def check_marr_b4_death(self):
        print("SJ")

    def check_div_b4_death(self):
        print("HL")

    def create_arrow_output(self):
        for i in range(len(self.line_list)):
            line_arr = self.line_list[i].split(' ')
            output_str = '<-- '
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
            self.output_list.append(output_str)

    def print_arrow_records(self):
        for i in range(len(self.line_list)):
            print('--> ' + self.line_list[i])
            print(self.output_list[i])
