# testing data
race_result_dict = {}


# function for setting up the main dictionary beforehand
def dict_setup(name_team, num_race):
    # create the index key and its rider list
    race_result_dict[name_team] = []

    # get number of races and add keys
    for i in range(num_race):
        race_result_dict[f"Race {i+1}"] = []

    # finally add tally list
    race_result_dict["Tally"] = []


# testing code
dict_setup("Red Team", 4)
print(race_result_dict)
