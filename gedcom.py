import prettytable as pt
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def convert_date(date_arr):
    date_obj = datetime.strptime(' '.join(date_arr), '%d %b %Y').date()
    return date_obj


class Gedcom():
    def __init__(self, input_url):
        self.line_list = []
        self.record_list = []
        self.output_list = []
        self.output_url = ""
        self.individual_list = []
        self.family_list = []
        self.error_list = []
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
                        indi_obj['Age'] = today.year - indi_obj['Birthday'].year \
                                          - ((today.month, today.day)
                                             < (indi_obj['Birthday'].month, indi_obj['Birthday'].day))
                        indi_obj['Alive'] = True
                    if 'Birthday' in indi_obj.keys() and 'Death' in indi_obj.keys():
                        indi_obj['Age'] = indi_obj['Death'].year - indi_obj['Birthday'].year \
                                          - ((indi_obj['Death'].month, indi_obj['Death'].day)
                                             < (indi_obj['Birthday'].month, indi_obj['Birthday'].day))
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

    # Set self.output_url for pretty table and error check output
    def set_output_url(self, output_url):
        self.output_url = output_url

    # Print all objects in self.individual_list and self.family_list
    # On console and store into txt file with PrettyTable
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
            indi_pt.add_row([individual['ID'], individual['Name'], individual["Gender"], str(individual['Birthday']),
                             individual['Age'], individual['Alive'], table_death, table_child, table_spouse])
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

        output_stream = open(self.output_url, "w")
        output_stream.write("Individuals:\n")
        output_stream.write(str(indi_pt))
        output_stream.write("\n")
        output_stream.write("Families:\n")
        output_stream.write(str(fam_pt))
        output_stream.write("\n")
        output_stream.close()

    # US01
    def check_date_b4_current(self):
        today = datetime.today().date()
        for indi in self.individual_list:
            if 'Birthday' in indi.keys():
                if indi["Birthday"] > today:
                    error_msg = "ERROR: INDIVIDUAL: US01: " + indi['ID'] + ": Birthday " + \
                                str(indi["Birthday"]) + " occurs before today: " + str(today)
                    self.error_list.append(error_msg)
            if "Death" in indi.keys():
                if indi["Death"] > today:
                    error_msg = "ERROR: INDIVIDUAL: US01: " + indi['ID'] + ": Death date " + \
                                str(indi["Death"]) + " occurs before today: " + str(today)
                    self.error_list.append(error_msg)
        for fami in self.family_list:
            if "Married" in fami.keys():
                if fami["Married"] > today:
                    error_msg = "ERROR: FAMILY: US01: " + fami['ID'] + ": Married Date " + \
                                str(fami["Married"]) + " occurs before today: " + str(today)
                    self.error_list.append(error_msg)
            if "Divorced" in fami.keys():
                if fami["Divorced"] > today:
                    error_msg = "ERROR: FAMILY: US01: " + fami['ID'] + ": Divorced Date " + \
                                str(fami["Divorced"]) + " occurs before today: " + str(today)
                    self.error_list.append(error_msg)
        # return True

    # US02
    def check_birth_b4_marr(self):
        for family in self.family_list:
            husband_id = family['Husband ID']
            wife_id = family['Wife ID']
            marr_date = family['Married']
            for individual in self.individual_list:
                if individual['ID'] == husband_id:
                    husband_birth = individual['Birthday']
                    if husband_birth > marr_date:
                        error_msg = "ERROR: FAMILY: US02: " + family['ID'] + ": " + husband_id + ": Marriage date " + \
                                    str(marr_date) + " occurs before birthday " + str(husband_birth)
                        self.error_list.append(error_msg)
                        # return False
                if individual['ID'] == wife_id:
                    wife_birth = individual['Birthday']
                    if wife_birth > marr_date:
                        error_msg = "ERROR: FAMILY: US02: " + family['ID'] + ": " + wife_id + ": Marriage date " + \
                                    str(marr_date) + " occurs before birthday " + str(wife_birth)
                        self.error_list.append(error_msg)
                        # return False
        # return True

    # US03
    def check_birth_b4_death(self):
        for individual in self.individual_list:
            if 'Death' in individual.keys():
                if individual['Birthday'] > individual['Death']:
                    error_msg = "ERROR: INDIVIDUAL: US03: " + individual['ID'] + ": Death date " + \
                                str(individual['Death']) + " occurs before Birthday " + str(individual['Birthday'])
                    self.error_list.append(error_msg)
        #             return False
        # return True

    # US04
    def check_marr_b4_div(self):
        for family in self.family_list:
            if 'Divorced' in family.keys():
                if family['Divorced'] < family['Married']:
                    error_msg = "ERROR: FAMILY: US04: " + family['ID'] + ": Divorce date " + \
                                str(family['Divorced']) + " occurs before marriage date " + str(family['Married'])
                    self.error_list.append(error_msg)
                    # return False
        # return True

    # US05
    def check_marr_b4_death(self):
        for family in self.family_list:
            husband_id = family['Husband ID']
            wife_id = family['Wife ID']
            marr_date = family['Married']
            for individual in self.individual_list:
                if 'Death' in individual.keys():
                    if individual['ID'] == husband_id:
                        husband_death = individual['Death']
                        if husband_death < marr_date:
                            error_msg = "ERROR: FAMILY: US03: " + family[
                                'ID'] + ": " + husband_id + ": Death date " + \
                                        str(husband_death) + " occurs before marriage date " + str(marr_date)
                            self.error_list.append(error_msg)
                            # return False
                    if individual['ID'] == wife_id:
                        wife_death = individual['Death']
                        if wife_death < marr_date:
                            error_msg = "ERROR: FAMILY: US03: " + family[
                                'ID'] + ": " + wife_id + ": Death date " + \
                                        str(wife_death) + " occurs before marriage date " + str(marr_date)
                            self.error_list.append(error_msg)
                            # return False
        # return True

    # US06
    def check_div_b4_death(self):
        for indi in self.individual_list:
            if "Death" in indi.keys():
                for fami in self.family_list:
                    if indi["ID"] == fami["Husband ID"] or indi["ID"] == fami["Wife ID"]:
                        if "Divorced" in fami.keys():
                            if indi["Death"] < fami["Divorced"]:
                                error_msg = "ERROR: FAMILY: US06: " + fami['ID'] + ": Divorced date " + \
                                            str(fami["Divorced"]) + " occurs before " + indi["ID"] + " Death date: " + \
                                            str(indi["Death"])
                                self.error_list.append(error_msg)
        # return True

    # US07 by HL
    # Death should be less than 150 years after birth for dead people,
    # and current date should be less than 150 years after birth for all living people
    def check_less_then_150_years_old(self):
        for individual in self.individual_list:
            if individual['Age'] >= 150:
                error_msg = "ERROR: US07: INDIVIDUAL: " + individual[
                    'ID'] + " is more than or equals to 150 years old."
                self.error_list.append(error_msg)

    # US08 by HL
    # Children should be born after marriage of parents,
    # and not more than 9 months after their divorce
    def check_birth_b4_marriage_of_parents(self):
        for family in self.family_list:
            if family["Children"] is not []:
                for child_id in family["Children"]:
                    child_birthday = None
                    parent_marriage_date = family["Married"]
                    for individual in self.individual_list:
                        if individual["ID"] == child_id:
                            child_birthday = individual["Birthday"]

                    if child_birthday <= parent_marriage_date:
                        error_msg = "ERROR: US08: FAMILY: " + family['ID'] + ": Child: " + child_id + \
                                    ": Birthday: " + str(child_birthday) + \
                                    ": Before his/her parents' Married: " + str(parent_marriage_date)
                        self.error_list.append(error_msg)

    # US09 by JK
    # Child should be born before death of mother,
    # and before 9 months after death of father
    def check_birth_b4_death_of_parents(self):
        for family in self.family_list:
            if family["Children"] is not []:
                for child_id in family["Children"]:
                    child_birthday = None
                    mother_death = None
                    father_death = None
                    for individual in self.individual_list:
                        if individual["ID"] == child_id:
                            child_birthday = individual["Birthday"]
                        if individual["ID"] == family["Wife ID"]:
                            if "Death" in individual.keys():
                                mother_death = individual["Death"]
                        if individual["ID"] == family["Husband ID"]:
                            if "Death" in individual.keys():
                                father_death = individual["Death"]

                    if mother_death is not None and child_birthday > mother_death:
                        error_msg = "ERROR: US09: FAMILY: " + family['ID'] + ": Child: " + child_id + ": Birthday: " + \
                                    str(child_birthday) + ": After mother: " + family["Wife ID"] + \
                                    ": Death: " + str(mother_death)
                        self.error_list.append(error_msg)
                    if father_death is not None and child_birthday > (father_death + relativedelta(months=9)):
                        error_msg = "ERROR: US09: FAMILY: " + family['ID'] + ": Child: " + child_id + ": Birthday: " + \
                                    str(child_birthday) + ": After father: " + family["Husband ID"] + \
                                    ": Death: " + str(father_death) + ": 9 months later"
                        self.error_list.append(error_msg)

    # US10 by JK
    # Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
    def check_marriage_after_14(self):
        for family in self.family_list:
            marriage_date = family["Married"]
            husband_married_age = None
            wife_married_age = None
            for individual in self.individual_list:
                if individual["ID"] == family["Husband ID"]:
                    husband_married_age = marriage_date.year - individual['Birthday'].year \
                                          - ((marriage_date.month, marriage_date.day)
                                             < (individual['Birthday'].month, individual['Birthday'].day))
                if individual["ID"] == family["Wife ID"]:
                    wife_married_age = marriage_date.year - individual['Birthday'].year \
                                       - ((marriage_date.month, marriage_date.day)
                                          < (individual['Birthday'].month, individual['Birthday'].day))

            if husband_married_age < 14:
                error_msg = "ANOMALY: US10: FAMILY: " + family["ID"] + ": Husband: " + family["Husband ID"] + \
                            ": Married at age: " + str(husband_married_age) + ": On: " + str(marriage_date)
                self.error_list.append(error_msg)

            if wife_married_age < 14:
                error_msg = "ANOMALY: US10: FAMILY: " + family["ID"] + ": Wife: " + family["Wife ID"] + \
                            ": Married at age: " + str(wife_married_age) + ": On: " + str(marriage_date)
                self.error_list.append(error_msg)

    # US22 by SJ
    # All individual IDs should be unique and all family IDs should be unique
    def check_unique_id(self):
        dict_family_id = {}
        dict_individual_id = {}
        for family in self.family_list:
            if family["ID"] in dict_family_id:
                dict_family_id[family["ID"]] += 1
            else:
                dict_family_id[family["ID"]] = 1
        for fam_id in dict_family_id.keys():
            if dict_family_id[fam_id] > 1:
                error_msg = "ANOMALY: US22: FAMILY: " + fam_id + " is not unique."
                self.error_list.append(error_msg)
        for individual in self.individual_list:
            if individual["ID"] in dict_individual_id:
                dict_individual_id[individual["ID"]] += 1
            else:
                dict_individual_id[individual["ID"]] = 1
        for ind_id in dict_individual_id.keys():
            if dict_individual_id[ind_id] > 1:
                error_msg = "ANOMALY: US22: INDIVIDUAL: " + ind_id + " is not unique."
                self.error_list.append(error_msg)

    # US12 by SJ
    # Mother should be less than 60 years older than her children,
    # and father should be less than 80 years older than his children
    def check_parents_not_too_old(self):
        for family in self.family_list:
            if family["Children"] is not []:
                for child_id in family["Children"]:
                    child_age = None
                    mother_age = None
                    father_age = None
                    for individual in self.individual_list:
                        if individual["ID"] == child_id:
                            child_age = individual["Age"]
                        if individual["ID"] == family["Wife ID"]:
                            mother_age = individual["Age"]
                        if individual["ID"] == family["Husband ID"]:
                            father_age = individual["Age"]

                    if mother_age > child_age + 60:
                        error_msg = "ERROR: US12: FAMILY: " + family['ID'] + ": Mother: " + family["Wife ID"] + \
                                    " is more than 60 years older than her children: " + child_id
                        self.error_list.append(error_msg)
                    if father_age > child_age + 80:
                        error_msg = "ERROR: US12: FAMILY: " + family['ID'] + ": Father: " + family["Husband ID"] + \
                                    " is more than 80 years older than his children: " + child_id
                        self.error_list.append(error_msg)

    # US13 by HL
    def siblings_spacing(self):
        timedelta_temp1 = timedelta(seconds=60, minutes=0, hours=0)
        timedelta_temp2 = timedelta(seconds=60, minutes=59, hours=5759)
        for family in self.family_list:
            if len(family['Children']) >= 2:
                for index, sib_item in enumerate(family['Children']):
                    birthday1 = None
                    for individual in self.individual_list:
                        if individual["ID"] == family['Children'][index]:
                            birthday1 = individual["Birthday"]
                    for index_more_than_above in range(index+1, len(family['Children'])):
                        for individual2 in self.individual_list:
                            birthday2 = None
                            if individual2["ID"] == family['Children'][index_more_than_above]:
                                birthday2 = individual2["Birthday"]
                            if birthday2 is not None:
                                if birthday2 > birthday1:
                                    if timedelta_temp2 > birthday2 - birthday1 >= timedelta_temp1:
                                        error_msg = "ERROR: US13: Siblings: " + \
                                                    family['Children'][index_more_than_above] + " and " \
                                                    + family['Children'][index] + "s' birthdays are not more than 8 " \
                                                    "months apart or less than 2 days apart."
                                        self.error_list.append(error_msg)
                                else:
                                    if timedelta_temp2 > birthday2 - birthday1 >= timedelta_temp1:
                                        error_msg = "ERROR: US13: Siblings: " + \
                                                    family['Children'][index_more_than_above] + " and " \
                                                    + family['Children'][index] + "s' birthdays are not more than 8 " \
                                                    "months apart or less than 2 days apart."
                                        self.error_list.append(error_msg)

    # US14 by HL
    def multiple_births_less_than_5(self):
        for family in self.family_list:
            if len(family['Children']) >= 5:
                temp_birthday_dict = {}
                for index, sib_item in enumerate(family['Children']):
                    for individual in self.individual_list:
                        if individual["ID"] == family['Children'][index]:
                            if individual["Birthday"] not in temp_birthday_dict:
                                temp_birthday_dict[individual["Birthday"]] = 1
                            else:
                                temp_birthday_dict[individual["Birthday"]] += 1
                if max(temp_birthday_dict.values()) >= 5:
                    error_msg = "ERROR: US14: 5 or more Siblings in family: " + family["ID"] + " have same birthdays."
                    self.error_list.append(error_msg)

    # US15 by JF
    def fewer_than_15_siblings(self):
        for family in self.family_list:
            sibling_num = len(family['Children'])
            if sibling_num > 15:
                error_msg = "ANOMALY: US15: FAMILY: " + family["ID"] + " has: " + \
                            str(sibling_num) + " siblings, more than 15"
                self.error_list.append(error_msg)

    # US16 by JF
    def male_last_names(self):
        for family in self.family_list:
            husband_id = family['Husband ID']
            for individual in self.individual_list:
                if individual['ID'] == husband_id:
                    name = individual['Name'].split()
                    last_name = name[-1]
                    for child_id in family['Children']:
                        for child_indi in self.individual_list:
                            if child_id == child_indi['ID']:
                                if child_indi['Gender'] == 'M':
                                    child_name = child_indi['Name'].split()
                                    if child_name[-1] != last_name:
                                        error_msg = "ANOMALY: US16: FAMILY: " + family["ID"] + ": Male member: " + \
                                                    child_indi['Name'] + ": has different last names"
                                        self.error_list.append(error_msg)

    # US17 by SJ
    def check_no_marriages_to_descendants(self):
        for family1 in self.family_list:
            husband_id1 = family1["Husband ID"]
            wife_id1 = family1["Wife ID"]
            for family2 in self.family_list:
                husband_id2 = family2["Husband ID"]
                wife_id2 = family2["Wife ID"]
                if family1 is not family2:
                    if husband_id2 == husband_id1:
                        if wife_id2 in family1["Children"]:
                            error_msg = "ERROR: US17: FAMILY: " + family2['ID'] + ", there is marriage between " \
                                                                                  "parents and descendants."
                            self.error_list.append(error_msg)
                    if wife_id2 == wife_id1:
                        if husband_id2 in family1["Children"]:
                            error_msg = "ERROR: US17: FAMILY: " + family2['ID'] + ", there is marriage between " \
                                                                                  "parents and descendants."
                            self.error_list.append(error_msg)

    # US18 by SJ
    def check_siblings_should_not_marry(self):
        for family1 in self.family_list:
            husband_id1 = family1["Husband ID"]
            wife_id1 = family1["Wife ID"]
            for family2 in self.family_list:
                if husband_id1 in family2["Children"] and wife_id1 in family2["Children"]:
                    error_msg = "ERROR: US18: FAMILY: " + family1['ID'] + ", there is marriage " \
                                                                            "between siblings."
                    self.error_list.append(error_msg)

    # US27 by HL
    def list_individual_ages(self):
        indi_pt = pt.PrettyTable()
        indi_pt.field_names = ["ID", "Name", "Age"]
        for individual in self.individual_list:
            indi_pt.add_row([individual['ID'], individual['Name'], individual['Age']])
        print(indi_pt)
        return (str(indi_pt))

    # US32 by HL List multiple births
    def list_multiple_births(self):
        indi_pt = pt.PrettyTable()
        indi_pt.field_names = ["ID", "Name", "Birthday"]
        for family1 in self.family_list:
            if len(family1['Children']) > 1:
                temp_dict = {}
                for every_sibling in family1['Children']:
                    for individual1 in self.individual_list:
                        if every_sibling == individual1["ID"]:
                            if str(individual1["Birthday"]) not in temp_dict:
                                temp_dict[str(individual1["Birthday"])] = [every_sibling]
                            else:
                                temp_dict[str(individual1["Birthday"])].append(every_sibling)
                for key in temp_dict.keys():
                    if len(temp_dict[key]) > 1:
                        for every_sibling in temp_dict[key]:
                            for individual1 in self.individual_list:
                                if every_sibling == individual1["ID"]:
                                    indi_pt.add_row(
                                        [individual1['ID'], individual1['Name'], str(individual1['Birthday'])])
        print(indi_pt)
        return str(indi_pt)

    # US21 by JF
    def correct_gender_for_role(self):
        for family in self.family_list:
            husband_id = family["Husband ID"]
            wife_id = family["Wife ID"]
            for individual in self.individual_list:
                if individual["ID"] == husband_id:
                    if individual["Gender"] is not 'M':
                        error_msg = "ERROR: US21: FAMILY: " + family['ID'] + \
                                    ": Husband: " + husband_id + ": Gender is not male"
                        self.error_list.append(error_msg)
                if individual["ID"] == wife_id:
                    if individual["Gender"] is not 'F':
                        error_msg = "ERROR: US21: FAMILY: " + family['ID'] + \
                                    ": Wife: " + wife_id + ": Gender is not female"
                        self.error_list.append(error_msg)

    # US25 by JF
    def unique_first_names_in_families(self):
        for family in self.family_list:
            children_dict = {}
            for child_id in family["Children"]:
                for individual in self.individual_list:
                    if individual["ID"] == child_id:
                        name_birth_tuple = (individual["Name"], individual["Birthday"])
                        if name_birth_tuple not in children_dict:
                            children_dict[name_birth_tuple] = [child_id]
                        else:
                            children_dict[name_birth_tuple].append(child_id)
            for name_birth in children_dict:
                if len(children_dict[name_birth]) > 1:
                    error_msg = "ANOMALY: US25: FAMILY: " + family["ID"] + ": Children: " + \
                                str(children_dict[name_birth]) + ": Has duplicated name and birthday"
                    self.error_list.append(error_msg)

    # US23 by SJ
    def check_unique_name_and_birth_date(self):
        dict_name_birth_date = {}
        for individual in self.individual_list:
            if (individual["Name"],individual["Birthday"]) in dict_name_birth_date:
                dict_name_birth_date[(individual["Name"],individual["Birthday"])].append(individual["ID"])
            else:
                dict_name_birth_date[(individual["Name"],individual["Birthday"])] = [individual["ID"]]
        for ind_name_birth_date in dict_name_birth_date.keys():
            if len(dict_name_birth_date[ind_name_birth_date]) > 1:
                error_msg = "ANOMALY: US23: INDIVIDUAL: " + str(dict_name_birth_date[ind_name_birth_date]) + \
                            " are duplicated."
                self.error_list.append(error_msg)

    # US24 by SJ
    def check_unique_families_by_spouses(self):
        dict_spouses_marriage_date = {}
        for family in self.family_list:
            if (family["Married"], family["Husband ID"], family["Wife ID"]) in dict_spouses_marriage_date:
                dict_spouses_marriage_date[(family["Married"], family["Husband ID"], family["Wife ID"])]\
                    .append(family["ID"])
            else:
                dict_spouses_marriage_date[(family["Married"], family["Husband ID"], family["Wife ID"])] = [family["ID"]]
        for fam_spouses_marriage_date in dict_spouses_marriage_date.keys():
            if len(dict_spouses_marriage_date[fam_spouses_marriage_date]) > 1:
                error_msg = "ANOMALY: US24: FAMILY: " + str(dict_spouses_marriage_date[fam_spouses_marriage_date]) + \
                            " are duplicated."
                self.error_list.append(error_msg)

    def check_all_objects_sprint_1(self):
        # US01
        self.check_date_b4_current()
        # US02
        self.check_birth_b4_marr()
        # US03
        self.check_birth_b4_death()
        # US04
        self.check_marr_b4_div()
        # US05
        self.check_marr_b4_death()
        # US06
        self.check_div_b4_death()

        output_stream = open(self.output_url, "a")
        output_stream.write("Errors:\n")
        for error in self.error_list:
            print(error)
            output_stream.write(error + '\n')
        output_stream.close()

    def check_all_objects_sprint_2(self):
        # US07
        self.check_less_then_150_years_old()
        # US08
        self.check_birth_b4_marriage_of_parents()
        # US09
        self.check_birth_b4_death_of_parents()
        # US10
        self.check_marriage_after_14()
        # US22
        self.check_unique_id()
        # US12
        self.check_parents_not_too_old()

        output_stream = open(self.output_url, "a")
        output_stream.write("Errors:\n")
        for error in self.error_list:
            print(error)
            output_stream.write(error + '\n')
        output_stream.close()

    def check_all_objects_sprint_3(self):
        # US13
        self.siblings_spacing()
        # US14
        self.multiple_births_less_than_5()
        # US15
        self.fewer_than_15_siblings()
        # US16
        self.male_last_names()
        # US17
        self.check_no_marriages_to_descendants()
        # US18
        self.check_siblings_should_not_marry()

        output_stream = open(self.output_url, "a")
        output_stream.write("Errors:\n")
        for error in self.error_list:
            print(error)
            output_stream.write(error + '\n')
        output_stream.close()

    # def check_all_objects_sprint_4(self):
        # US19 by HL
        # self.first_cousins_should_not_marry()

        # US20 by HL
        # self.aunts_and_uncles()

        # US21 by JF
        # self.correct_gender_for_role()

        # US25 by JF
        # self.unique_first_names_in_families()

        # US23 by SJ
        # self.check_unique_name_and_birth_date()

        # US24 by SJ
        # self.check_unique_families_by_spouses()

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

# test_case_13_1 = Gedcom("sprint3test/test_example_13_1")
# test_case_13_1.siblings_spacing()
# test_case_14_1 = Gedcom("sprint3test/test_example_14_1")
# test_case_14_1.multiple_births_less_than_5()