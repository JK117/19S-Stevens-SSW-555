# US 09 by JK
# Child should be born before death of mother,
# and before 9 months after death of father

from dateutil.relativedelta import relativedelta


def check_birth_b4_death_of_parents(gedcom):
    for family in gedcom.family_list:
        if family["Children"] is not []:
            for child_id in family["Children"]:
                child_birthday = None
                mother_death = None
                father_death = None
                for individual in gedcom.individual_list:
                    if individual["ID"] == child_id:
                        child_birthday = individual["Birthday"]
                    if individual["ID"] == family["Wife ID"]:
                        if "Death" in individual.keys():
                            mother_death = individual["Death"]
                    if individual["ID"] == family["Husband ID"]:
                        if "Death" in individual.keys():
                            father_death = individual["Death"]

                if mother_death is not None and child_birthday > mother_death:
                    error_msg = "ERROR: US09: FAMILY: " + family['ID'] + ": Child: " + child_id + ": Birthday: " + \
                                str(child_birthday) + ": After mother: " + family["Wife ID"] + \
                                ": Death: " + str(mother_death)
                    gedcom.error_list.append(error_msg)
                if father_death is not None and child_birthday > (father_death + relativedelta(months=9)):
                    error_msg = "ERROR: US09: FAMILY: " + family['ID'] + ": Child: " + child_id + ": Birthday: " + \
                                str(child_birthday) + ": After father: " + family["Husband ID"] + \
                                ": Death: " + str(father_death) + ": 9 months later"
                    gedcom.error_list.append(error_msg)
