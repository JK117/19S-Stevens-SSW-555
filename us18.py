# US18: Siblings should not marry one another
# BY Shan Jiang


def check_siblings_should_not_marry(self):
    for family1 in self.family_list:
        husband_id1 = family1["Husband ID"]
        wife_id1 = family1["Wife ID"]
        for family2 in self.family_list:
            if husband_id1 in family2["Children"] and wife_id1 in family2["Children"]:
                error_msg = "ERROR: US18: FAMILY: " + family1['ID'] + ", there is marriage " \
                                                                      "between siblings."
                self.error_list.append(error_msg)
