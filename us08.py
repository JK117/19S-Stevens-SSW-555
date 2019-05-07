# US08 by HL
# Children should be born after marriage of parents,
# and not more than 9 months after their divorce


def check_birth_b4_marriage_of_parents(gedcom):
    for family in gedcom.family_list:
        if family["Children"] is not []:
            for child_id in family["Children"]:
                child_birthday = None
                parent_marriage_date = family["Married"]
                for individual in gedcom.individual_list:
                    if individual["ID"] == child_id:
                        child_birthday = individual["Birthday"]

                if child_birthday <= parent_marriage_date:
                    error_msg = "ERROR: US08: FAMILY: " + family['ID'] + ": Child: " + child_id + \
                                ": Birthday: " + str(child_birthday) + \
                                ": Before his/her parents' Married: " + str(parent_marriage_date)
                    gedcom.error_list.append(error_msg)
