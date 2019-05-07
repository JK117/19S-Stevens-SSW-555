# US25 by JF


def unique_first_names_in_families(gedcom):
    for family in gedcom.family_list:
        children_dict = {}
        for child_id in family["Children"]:
            for individual in gedcom.individual_list:
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
                gedcom.error_list.append(error_msg)
