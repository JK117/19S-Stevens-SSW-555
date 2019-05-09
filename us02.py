# US 02 by JF


def check_birth_b4_marr(gedcom):
    for family in gedcom.family_list:
        husband_id = family['Husband ID']
        wife_id = family['Wife ID']
        marr_date = family['Married']
        for individual in gedcom.individual_list:
            if individual['ID'] == husband_id:
                husband_birth = individual['Birthday']
                if husband_birth > marr_date:
                    error_msg = "ERROR: FAMILY: US02: " + family['ID'] + ": " + husband_id + ": Marriage date " + \
                                str(marr_date) + " occurs before birthday " + str(husband_birth)
                    gedcom.error_list.append(error_msg)
                    # return False
            if individual['ID'] == wife_id:
                wife_birth = individual['Birthday']
                if wife_birth > marr_date:
                    error_msg = "ERROR: FAMILY: US02: " + family['ID'] + ": " + wife_id + ": Marriage date " + \
                                str(marr_date) + " occurs before birthday " + str(wife_birth)
                    gedcom.error_list.append(error_msg)
                    # return False
    # return True
