import pandas

# BMX Race Result Calculator Base Component
# Robert Park 27/06/2023
# Version 1; Setting variables, Building framework

# Functions


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
    race_result_string = pandas.DataFrame.to_string(race_result_frame)

    # write output to file
    # create file to hold data (add .txt extension)
    write_to = "{}.txt".format(f"{nameTeam} Race Results")
    text_file = open(write_to, "w+")
    text_file.write(race_result_string)

    # close file
    text_file.close()


# Variables
numRider = 6
numRace = 4
maxPosition = 50
totalScore = 0

while True:

    nameTeam = null_checker("Please enter the team name\n")

    # Main Dictionary
    race_result_dict = {  # it will take input for numRace and use for loop to create keys
        nameTeam: [],
        "Race 1": [],
        "Race 2": [],
        "Race 3": [],
        "Race 4": [],
        "Tally": []
    }

    # Main Routine
    for i in range(1, numRider+1):

        # Name Component
        nameRider = null_checker("Please enter the rider name\n")
        race_result_dict[nameTeam].append(nameRider)

        # Nested Loop for Placings
        for j in range(1, numRace+1):

            position = integer_checker(
                f"Please enter the placing for Race {j}\n", 0, 50)
            race_result_dict[f"Race {j}"].append(position)

            # Cumulative score
            totalScore += score_checker(position)

        # Tally Update
        race_result_dict["Tally"].append(totalScore)
        totalScore = 0

    # Table Setup
    race_result_frame = pandas.DataFrame(race_result_dict)
    race_result_frame = race_result_frame.set_index(nameTeam)
    print(race_result_frame)

    # Program Restart / Quit
    if string_checker("Do you want to restart the program? (y/n)\n", ['yes', 'no']) == "no":
        break

export()