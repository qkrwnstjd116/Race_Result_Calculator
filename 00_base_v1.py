import pandas
from datetime import date

# BMX Race Result Calculator Base Component
# Robert Park 27/06/2023
# Version 1: Integrating Components, Structuring Main Routine

# functions


def integer_checker(question, min, max):
    while True:
        try:
            inp = int(input(question))

            if inp < min or inp > max:
                raise ValueError
            else:
                return inp

        except:
            print(f"Please enter an integer between {min} and {max}\n")


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


def string_checker(question, valid_responses):
    while True:
        inp = null_checker(question).lower()

        for item in valid_responses:
            if inp == item or inp == item[:1]:
                return item

        print(f"Please choose between {valid_responses}\n")


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


def export():
    # **** get current date for heading and filename ****
    # get today's date
    today = date.today()

    # get day, month, and year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    # create strings to write
    race_result_string = pandas.DataFrame.to_string(race_result_frame)
    filename = f"Race Results ({day}_{month}_{year})"
    write_to = "{}.txt".format(filename)

    # create a text file and write on
    text_file = open(write_to, "w+")
    text_file.write(race_result_string)

    # close file
    text_file.close()


# variables
num_rider = 6
num_race = 4  # it will take input for numRace in later versions
max_position = 50
total_score = 0


# main routine
while True:
    name_team = null_checker("Please enter the team name\n")

    # main dictionary
    race_result_dict = {
        name_team: [],
        "Race 1": [],
        "Race 2": [],
        "Race 3": [],
        "Race 4": [],
        "Tally": [],
    }

    for i in range(
        1, num_rider + 1
    ):  # this can be changed to while loop for flexibility
        # get rider name
        name_rider = null_checker("Please enter the rider name\n")
        race_result_dict[name_team].append(name_rider)

        # get placings for the rider
        for j in range(1, num_race + 1):
            position = integer_checker(
                f"Please enter the placing for Race {j}\n", 0, max_position
            )
            race_result_dict[f"Race {j}"].append(position)

            # add to the tally
            total_score += score_checker(position)

        # submit tally to dictionary
        race_result_dict["Tally"].append(total_score)
        total_score = 0

    # table setup
    race_result_frame = pandas.DataFrame(race_result_dict)
    race_result_frame = race_result_frame.set_index(name_team)
    print(race_result_frame)

    # export to text file
    export()

    # program restart / quit
    if (
        string_checker("Do you want to restart the program? (y/n)\n", ["yes", "no"])
        == "no"
    ):
        break
