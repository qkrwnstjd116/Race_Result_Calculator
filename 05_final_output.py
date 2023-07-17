import pandas
from datetime import date

# Testing Data
race_result_dict = {
    "Red Team": ['Ben', 'Charlie', 'Zach', 'Yujin', 'Robert', 'Nina'],
    "Race 1": [12, 1, 1, 12, 2, 2],
    "Race 2": [3, 23, 2, 3, 1, 2],
    "Race 3": [1, 34, 1, 2, 1, 1],
    "Race 4": [4, 2, 21, 12, 2, 2],
    "Tally": [6, 8, 13, 4, 16, 14]
}

race_result_frame = pandas.DataFrame(race_result_dict)
race_result_frame = race_result_frame.set_index("Red Team")

# Exporting to a text file


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


# main routine
export()
