# US03: Birth should occur before death of an individual
# BY Shan Jiang


def check_birth_b4_death(gedcom):
    for individual in gedcom.individual_list:
        if 'Death' in individual.keys():
            if individual['Birthday'] > individual['Death']:
                error_msg = "ERROR: INDIVIDUAL: US03: " + individual['ID'] + ": Death date " + \
                            str(individual['Death']) + " occurs before Birthday " + str(individual['Birthday'])
                gedcom.error_list.append(error_msg)
