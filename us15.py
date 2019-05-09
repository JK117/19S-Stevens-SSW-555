# US15 by JF


def fewer_than_15_siblings(gedcom):
    for family in gedcom.family_list:
        sibling_num = len(family['Children'])
        if sibling_num > 15:
            error_msg = "ANOMALY: US15: FAMILY: " + family["ID"] + " has: " + \
                        str(sibling_num) + " siblings, more than 15"
            gedcom.error_list.append(error_msg)
