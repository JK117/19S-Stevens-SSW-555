# US32 by HL List multiple births
import prettytable as pt


def list_multiple_births(gedcom):
    indi_pt = pt.PrettyTable()
    indi_pt.field_names = ["ID", "Name", "Birthday"]
    for family1 in gedcom.family_list:
        if len(family1['Children']) > 1:
            temp_dict = {}
            for every_sibling in family1['Children']:
                for individual1 in gedcom.individual_list:
                    if every_sibling == individual1["ID"]:
                        if str(individual1["Birthday"]) not in temp_dict:
                            temp_dict[str(individual1["Birthday"])] = [every_sibling]
                        else:
                            temp_dict[str(individual1["Birthday"])].append(every_sibling)
            for key in temp_dict.keys():
                if len(temp_dict[key]) > 1:
                    for every_sibling in temp_dict[key]:
                        for individual1 in gedcom.individual_list:
                            if every_sibling == individual1["ID"]:
                                indi_pt.add_row(
                                    [individual1['ID'], individual1['Name'], str(individual1['Birthday'])])
    print(indi_pt)
    return str(indi_pt)
