# US12: Mother should be less than 60 years older than her children
# and father should be less than 80 years older than his children
# BY Shan Jiang


def check_parents_not_too_old(gedcom):
    for family in gedcom.family_list:
        if family["Children"] is not []:
            for child_id in family["Children"]:
                child_age = None
                mother_age = None
                father_age = None
                for individual in gedcom.individual_list:
                    if individual["ID"] == child_id:
                        child_age = individual["Age"]
                    if individual["ID"] == family["Wife ID"]:
                        mother_age = individual["Age"]
                    if individual["ID"] == family["Husband ID"]:
                        father_age = individual["Age"]

                if mother_age > child_age + 60:
                    error_msg = "ANOMALY: US12: FAMILY: " + family['ID'] + ": Mother: " + family["Wife ID"] + \
                                " is more than 60 years older than her children: " + child_id
                    gedcom.error_list.append(error_msg)
                if father_age > child_age + 80:
                    error_msg = "ANOMALY: US12: FAMILY: " + family['ID'] + ": Father: " + family["Husband ID"] + \
                                " is more than 80 years older than his children: " + child_id
                    gedcom.error_list.append(error_msg)
