# Null Checker for String Inputs
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


# Main Routine for Testing
print(null_checker("Please enter your name\n"))
