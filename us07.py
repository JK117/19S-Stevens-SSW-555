# US07 by HL
# Death should be less than 150 years after birth for dead people,
# and current date should be less than 150 years after birth for all living people


def check_less_then_150_years_old(gedcom):
    for individual in gedcom.individual_list:
        if individual['Age'] >= 150:
            error_msg = "ERROR: US07: INDIVIDUAL: " + individual[
                'ID'] + " is more than or equals to 150 years old."
            gedcom.error_list.append(error_msg)
