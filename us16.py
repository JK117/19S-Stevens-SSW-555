# US16 by JF


def male_last_names(gedcom):
    for family in gedcom.family_list:
        husband_id = family['Husband ID']
        for individual in gedcom.individual_list:
            if individual['ID'] == husband_id:
                name = individual['Name'].split()
                last_name = name[-1]
                for child_id in family['Children']:
                    for child_indi in gedcom.individual_list:
                        if child_id == child_indi['ID']:
                            if child_indi['Gender'] == 'M':
                                child_name = child_indi['Name'].split()
                                if child_name[-1] != last_name:
                                    error_msg = "ANOMALY: US16: FAMILY: " + family["ID"] + ": Male member: " + \
                                                child_indi['Name'] + ": has different last names"
                                    gedcom.error_list.append(error_msg)
