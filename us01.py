# US01 by HL
from datetime import datetime


def check_date_b4_current(gedcom):
    today = datetime.today().date()
    for indi in gedcom.individual_list:
        if 'Birthday' in indi.keys():
            if indi["Birthday"] > today:
                error_msg = "ERROR: INDIVIDUAL: US01: " + indi['ID'] + ": Birthday " + \
                            str(indi["Birthday"]) + " occurs before today: " + str(today)
                gedcom.error_list.append(error_msg)
        if "Death" in indi.keys():
            if indi["Death"] > today:
                error_msg = "ERROR: INDIVIDUAL: US01: " + indi['ID'] + ": Death date " + \
                            str(indi["Death"]) + " occurs before today: " + str(today)
                gedcom.error_list.append(error_msg)
    for fami in gedcom.family_list:
        if "Married" in fami.keys():
            if fami["Married"] > today:
                error_msg = "ERROR: FAMILY: US01: " + fami['ID'] + ": Married Date " + \
                            str(fami["Married"]) + " occurs before today: " + str(today)
                gedcom.error_list.append(error_msg)
        if "Divorced" in fami.keys():
            if fami["Divorced"] > today:
                error_msg = "ERROR: FAMILY: US01: " + fami['ID'] + ": Divorced Date " + \
                            str(fami["Divorced"]) + " occurs before today: " + str(today)
                gedcom.error_list.append(error_msg)
