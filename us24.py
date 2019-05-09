# US24: No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
# BY Shan Jiang


def check_unique_families_by_spouses(gedcom):
    dict_spouses_marriage_date = {}
    for family in gedcom.family_list:
        if (family["Married"], family["Husband ID"], family["Wife ID"]) in dict_spouses_marriage_date:
            dict_spouses_marriage_date[(family["Married"], family["Husband ID"], family["Wife ID"])] \
                .append(family["ID"])
        else:
            dict_spouses_marriage_date[(family["Married"], family["Husband ID"], family["Wife ID"])] = [family["ID"]]
    for fam_spouses_marriage_date in dict_spouses_marriage_date.keys():
        if len(dict_spouses_marriage_date[fam_spouses_marriage_date]) > 1:
            error_msg = "ERROR: US24: FAMILY: " + str(dict_spouses_marriage_date[fam_spouses_marriage_date]) + \
                        " are duplicated."
            gedcom.error_list.append(error_msg)
