# US21 by JF


def correct_gender_for_role(gedcom):
    for family in gedcom.family_list:
        husband_id = family["Husband ID"]
        wife_id = family["Wife ID"]
        for individual in gedcom.individual_list:
            if individual["ID"] == husband_id:
                if individual["Gender"] is not 'M':
                    error_msg = "ERROR: US21: FAMILY: " + family['ID'] + \
                                ": Husband: " + husband_id + ": Gender is not male"
                    gedcom.error_list.append(error_msg)
            if individual["ID"] == wife_id:
                if individual["Gender"] is not 'F':
                    error_msg = "ERROR: US21: FAMILY: " + family['ID'] + \
                                ": Wife: " + wife_id + ": Gender is not female"
                    gedcom.error_list.append(error_msg)
