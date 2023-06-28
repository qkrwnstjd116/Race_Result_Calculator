race_result_dictionary = {

}

race_result_dictionary["Tally"] = []

# Function for Tally Calculation Component


def score_checker(position):

    if position == 1:
        score = 5
    elif position == 2:
        score = 3
    elif position == 3:
        score = 1
    else:
        score = 0

    return score
