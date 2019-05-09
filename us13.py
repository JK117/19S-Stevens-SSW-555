# US13 by HL
from datetime import timedelta


def siblings_spacing(gedcom):
    timedelta_temp1 = timedelta(seconds=60, minutes=0, hours=0)
    timedelta_temp2 = timedelta(seconds=60, minutes=59, hours=5759)
    for family in gedcom.family_list:
        if len(family['Children']) >= 2:
            for index, sib_item in enumerate(family['Children']):
                birthday1 = None
                for individual in gedcom.individual_list:
                    if individual["ID"] == family['Children'][index]:
                        birthday1 = individual["Birthday"]
                for index_more_than_above in range(index + 1, len(family['Children'])):
                    for individual2 in gedcom.individual_list:
                        birthday2 = None
                        if individual2["ID"] == family['Children'][index_more_than_above]:
                            birthday2 = individual2["Birthday"]
                        if birthday2 is not None:
                            if birthday2 > birthday1:
                                if timedelta_temp2 > birthday2 - birthday1 >= timedelta_temp1:
                                    error_msg = "ERROR: US13: Siblings: " + \
                                                family['Children'][index_more_than_above] + " and " \
                                                + family['Children'][index] + "s' birthdays are not more than 8 " \
                                                                              "months apart or less than 2 days apart."
                                    gedcom.error_list.append(error_msg)
                            else:
                                if timedelta_temp2 > birthday2 - birthday1 >= timedelta_temp1:
                                    error_msg = "ERROR: US13: Siblings: " + \
                                                family['Children'][index_more_than_above] + " and " \
                                                + family['Children'][index] + "s' birthdays are not more than 8 " \
                                                                              "months apart or less than 2 days apart."
                                    gedcom.error_list.append(error_msg)
