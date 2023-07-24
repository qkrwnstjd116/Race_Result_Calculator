import pandas
from datetime import date

# BMX Race Result Calculator Base Component
# Robert Park 24/07/2023
# Version 3 (final): Taking Fixed Input for num_race (changed from while to for loop)
# General Refinments; Reducing Redundancy, Text File Formatting, Commenting


# functions


# returns the input that is not blank
def null_checker(question):
    while True:
        try:
            inp = input(question)

            if inp.strip() == "":
                raise ValueError
            else:
                return inp

        except:
            print("Please do not leave this blank\n")


# returns the integer input within the valid range
def integer_checker(question, min, max):
    while True:
        try:
            inp = int(null_checker(question))

            if inp < min or inp > max:
                raise ValueError
            else:
                return inp

        except:
            print(f"Please enter an integer between {min} and {max}\n")


# returns the string input in valid responses
def string_checker(question, valid_responses):
    while True:
        inp = null_checker(question).lower()

        for item in valid_responses:
            if inp == item or inp == item[:1]:
                return item

        print(f"Please choose between {valid_responses}\n")


# returns the corresponding score for a placing
def score_checker(position):
    # compare the position to the podium and return the score
    if position == 1:
        return 5
    elif position == 2:
        return 3
    elif position == 3:
        return 1
    else:
        return 0


# sets up the main dictionary
def dict_setup(name_team, num_race):
    # create the index key and its rider list
    race_result_dict[name_team] = []

    # get number of races and add keys
    for i in range(num_race):
        race_result_dict[f"Race {i+1}"] = []

    # finally add tally list
    race_result_dict["Tally"] = []


# exports the final ouput as a text file
def export():
    # get today's date
    today = date.today()

    # get day, month, and year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    # stringify the table
    race_result_string = pandas.DataFrame.to_string(race_result_frame)

    # create a text file and write the data
    filename = f"Race Results ({day}_{month}_{year})"
    write_to = "{}.txt".format(filename)
    text_file = open(write_to, "a")
    text_file.write(
        f"----- {name_team} Race Results ----\n\n" + race_result_string + "\n\n\n"
    )

    # close file
    text_file.close()


# constants
MAX_POSITION = 50

# variables
total_score = 0

# main dictionary
race_result_dict = {}


# main routine
while True:
    # inputs for program setting
    name_team = null_checker("Please enter the team name\n")
    num_race = integer_checker("Please enter the number of races\n", 1, 10)
    num_rider = integer_checker("Please enter the number of riders\n", 1, 100)

    # adding keys to the empty main dictionary based on the inputs
    dict_setup(name_team, num_race)

    # loop iterating for each rider (each row on the table)
    for i in range(num_rider):
        # get rider name, append rider list
        name_rider = null_checker("Please enter the rider name\n")
        race_result_dict[name_team].append(name_rider)

        # get placings for the rider; loop iterates for each race (columns on the table)
        for i in range(num_race):
            position = integer_checker(
                f"Please enter the placing for Race {i+1}\n", 0, MAX_POSITION
            )
            race_result_dict[f"Race {i+1}"].append(position)

            # get the score, add to the cumulative tally
            total_score += score_checker(position)

        # submit tally to main dictionary
        race_result_dict["Tally"].append(total_score)
        total_score = 0

    # table setup, print
    race_result_frame = pandas.DataFrame(race_result_dict)
    race_result_frame = race_result_frame.set_index(name_team)
    print(race_result_frame)

    # export to text file
    export()

    # program restart / quit
    if (
        string_checker("\nDo you want to restart the program? (y/n)\n", ["yes", "no"])
        == "no"
    ):
        break
    else:
        # if restart, reset the main dictionary
        race_result_dict.clear()
