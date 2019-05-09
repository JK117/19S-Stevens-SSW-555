# US06 by Hl


def check_div_b4_death(gedcom):
    for indi in gedcom.individual_list:
        if "Death" in indi.keys():
            for fami in gedcom.family_list:
                if indi["ID"] == fami["Husband ID"] or indi["ID"] == fami["Wife ID"]:
                    if "Divorced" in fami.keys():
                        if indi["Death"] < fami["Divorced"]:
                            error_msg = "ERROR: FAMILY: US06: " + fami['ID'] + ": Divorced date " + \
                                        str(fami["Divorced"]) + " occurs before " + indi["ID"] + " Death date: " + \
                                        str(indi["Death"])
                            gedcom.error_list.append(error_msg)
