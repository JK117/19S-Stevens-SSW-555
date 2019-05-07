# US 04 by JF


def check_marr_b4_div(gedcom):
    for family in gedcom.family_list:
        if 'Divorced' in family.keys():
            if family['Divorced'] < family['Married']:
                error_msg = "ERROR: FAMILY: US04: " + family['ID'] + ": Divorce date " + \
                            str(family['Divorced']) + " occurs before marriage date " + str(family['Married'])
                gedcom.error_list.append(error_msg)
                # return False
    # return True
