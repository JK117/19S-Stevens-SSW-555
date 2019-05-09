# US05: Marriage should occur before death of either spouse
# BY Shan Jiang


def check_marr_b4_death(gedcom):
    for family in gedcom.family_list:
        husband_id = family['Husband ID']
        wife_id = family['Wife ID']
        marr_date = family['Married']
        for individual in gedcom.individual_list:
            if 'Death' in individual.keys():
                if individual['ID'] == husband_id:
                    husband_death = individual['Death']
                    if husband_death < marr_date:
                        error_msg = "ERROR: FAMILY: US03: " + family[
                            'ID'] + ": " + husband_id + ": Death date " + \
                                    str(husband_death) + " occurs before marriage date " + str(marr_date)
                        gedcom.error_list.append(error_msg)

                if individual['ID'] == wife_id:
                    wife_death = individual['Death']
                    if wife_death < marr_date:
                        error_msg = "ERROR: FAMILY: US03: " + family[
                            'ID'] + ": " + wife_id + ": Death date " + \
                                    str(wife_death) + " occurs before marriage date " + str(marr_date)
                        gedcom.error_list.append(error_msg)
