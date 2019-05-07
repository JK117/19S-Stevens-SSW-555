# US22: All individual IDs should be unique and all family IDs should be unique
# BY Shan Jiang


def check_unique_id(gedcom):
    dict_family_id = {}
    dict_individual_id = {}
    for family in gedcom.family_list:
        if family["ID"] in dict_family_id:
            dict_family_id[family["ID"]] += 1
        else:
            dict_family_id[family["ID"]] = 1
    for fam_id in dict_family_id.keys():
        if dict_family_id[fam_id] > 1:
            error_msg = "ANOMALY: US22: FAMILY: " + fam_id + " is not unique."
            gedcom.error_list.append(error_msg)
    for individual in gedcom.individual_list:
        if individual["ID"] in dict_individual_id:
            dict_individual_id[individual["ID"]] += 1
        else:
            dict_individual_id[individual["ID"]] = 1
    for ind_id in dict_individual_id.keys():
        if dict_individual_id[ind_id] > 1:
            error_msg = "ANOMALY: US22: INDIVIDUAL: " + ind_id + " is not unique."
            gedcom.error_list.append(error_msg)
