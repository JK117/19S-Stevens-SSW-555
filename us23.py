# US23: No more than one individual with the same name and birth date should appear in a GEDCOM file
# BY Shan Jiang


def check_unique_name_and_birth_date(gedcom):
    dict_name_birth_date = {}
    for individual in gedcom.individual_list:
        if (individual["Name"], individual["Birthday"]) in dict_name_birth_date:
            dict_name_birth_date[(individual["Name"], individual["Birthday"])].append(individual["ID"])
        else:
            dict_name_birth_date[(individual["Name"], individual["Birthday"])] = [individual["ID"]]
    for ind_name_birth_date in dict_name_birth_date.keys():
        if len(dict_name_birth_date[ind_name_birth_date]) > 1:
            error_msg = "ANOMALY: US23: INDIVIDUAL: " + str(dict_name_birth_date[ind_name_birth_date]) + \
                        " are duplicated."
            gedcom.error_list.append(error_msg)
