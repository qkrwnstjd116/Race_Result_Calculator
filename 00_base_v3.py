import pandas
from datetime import date

# BMX Race Result Calculator Base Component
# Robert Park 21/07/2023
# Version 2: Improvements in Flexibility

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


def dict_setup(nameTeam, numRace):

    # get team name and add key
    race_result_dict[nameTeam] = []

    # get number of races and add keys
    for i in range(1, numRace+1):
        race_result_dict[f"Race {i}"] = []

    # finally add tally list
    race_result_dict["Tally"] = []


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
maxPosition = 50
totalScore = 0

# main dictionary
race_result_dict = {

}


# main routine
while True:

    # adding keys to the empty main dictionary based on the inputs
    nameTeam = null_checker("Please enter the team name\n")
    numRace = integer_checker("Please enter the number of races\n", 1, 10)
    dict_setup(nameTeam, numRace)

    # loop iterating for each rider (each row on the table)
    while True:

        # get rider name
        try:
            nameRider = null_checker(
                "Please enter the rider name.\nIf you want to stop entering, press 'xxx'\n")

            if nameRider.lower() == 'xxx' and len(race_result_dict[nameTeam]) > 0:
                break
            elif nameRider.lower() == 'xxx':
                raise ValueError
            else:
                race_result_dict[nameTeam].append(nameRider)

            # get placings for the rider
            for i in range(1, numRace+1):

                position = integer_checker(
                    f"Please enter the placing for Race {i}\n", 0, 50)
                race_result_dict[f"Race {i}"].append(position)

                # add to the tally
                totalScore += score_checker(position)

            # submit tally to dictionary
            race_result_dict["Tally"].append(totalScore)
            totalScore = 0

        except:
            print("You need to have at least one rider inputted\n")

    # table setup & print
    race_result_frame = pandas.DataFrame(race_result_dict)
    race_result_frame = race_result_frame.set_index(nameTeam)
    print(race_result_frame)

    # export to text file
    export()

    # program restart / quit
    if string_checker("\nDo you want to restart the program? (y/n)\n", ['yes', 'no']) == "no":
        break
    else:
        race_result_dict.clear()
