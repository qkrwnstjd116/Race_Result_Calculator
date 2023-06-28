import pandas

# Exporting to a text file


def export():
    race_result_string = pandas.DataFrame.to_string(race_result_frame)

    # write output to file
    # create file to hold data (add .txt extension)
    write_to = "{}.txt".format(f"{nameTeam} Race Results")
    text_file = open(write_to, "w+")
    text_file.write(race_result_string)

    # close file
    text_file.close()
