# function that returns the score corresponding to the placing
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


# testing code
print("Score:", score_checker(int(input("Position:"))))
