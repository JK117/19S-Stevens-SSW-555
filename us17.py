# US17: Parents should not marry any of their descendants
# BY Shan Jiang


def check_no_marriages_to_descendants(self):
    for family1 in self.family_list:
        husband_id1 = family1["Husband ID"]
        wife_id1 = family1["Wife ID"]
        for family2 in self.family_list:
            husband_id2 = family2["Husband ID"]
            wife_id2 = family2["Wife ID"]
            if family1 is not family2:
                if husband_id2 == husband_id1:
                    if wife_id2 in family1["Children"]:
                        error_msg = "ERROR: US17: FAMILY: " + family2['ID'] + ", there is marriage between " \
                                                                              "parents and descendants."
                        self.error_list.append(error_msg)
                if wife_id2 == wife_id1:
                    if husband_id2 in family1["Children"]:
                        error_msg = "ERROR: US17: FAMILY: " + family2['ID'] + ", there is marriage between " \
                                                                              "parents and descendants."
                        self.error_list.append(error_msg)
