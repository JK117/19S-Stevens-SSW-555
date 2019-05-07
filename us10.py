# US10 by JK
# Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)


def check_marriage_after_14(gedcom):
    for family in gedcom.family_list:
        marriage_date = family["Married"]
        husband_married_age = None
        wife_married_age = None
        for individual in gedcom.individual_list:
            if individual["ID"] == family["Husband ID"]:
                husband_married_age = marriage_date.year - individual['Birthday'].year \
                                      - ((marriage_date.month, marriage_date.day)
                                         < (individual['Birthday'].month, individual['Birthday'].day))
            if individual["ID"] == family["Wife ID"]:
                wife_married_age = marriage_date.year - individual['Birthday'].year \
                                   - ((marriage_date.month, marriage_date.day)
                                      < (individual['Birthday'].month, individual['Birthday'].day))

        if husband_married_age < 14:
            error_msg = "ANOMALY: US10: FAMILY: " + family["ID"] + ": Husband: " + family["Husband ID"] + \
                        ": Married at age: " + str(husband_married_age) + ": On: " + str(marriage_date)
            gedcom.error_list.append(error_msg)

        if wife_married_age < 14:
            error_msg = "ANOMALY: US10: FAMILY: " + family["ID"] + ": Wife: " + family["Wife ID"] + \
                        ": Married at age: " + str(wife_married_age) + ": On: " + str(marriage_date)
            gedcom.error_list.append(error_msg)
