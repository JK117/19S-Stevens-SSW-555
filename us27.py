# US27 by HL
import prettytable as pt


def list_individual_ages(gedcom):
    indi_pt = pt.PrettyTable()
    indi_pt.field_names = ["ID", "Name", "Age"]
    for individual in gedcom.individual_list:
        indi_pt.add_row([individual['ID'], individual['Name'], individual['Age']])
    print(indi_pt)
    return str(indi_pt)
