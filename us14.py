# US14 by HL


def multiple_births_less_than_5(gedcom):
    for family in gedcom.family_list:
        if len(family['Children']) >= 5:
            temp_birthday_dict = {}
            for index, sib_item in enumerate(family['Children']):
                for individual in gedcom.individual_list:
                    if individual["ID"] == family['Children'][index]:
                        if individual["Birthday"] not in temp_birthday_dict:
                            temp_birthday_dict[individual["Birthday"]] = 1
                        else:
                            temp_birthday_dict[individual["Birthday"]] += 1
            if max(temp_birthday_dict.values()) >= 5:
                error_msg = "ERROR: US14: 5 or more Siblings in family: " + family["ID"] + " have same birthdays."
                gedcom.error_list.append(error_msg)
